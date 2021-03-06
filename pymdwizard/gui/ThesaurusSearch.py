#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime

from lxml import etree
import pandas as pd
import requests


from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QTableView, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QToolButton
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint
from PyQt5.QtCore import Qt, QMimeData, QObject, QTimeLine

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QEvent, QCoreApplication
from PyQt5.QtGui import QMouseEvent, QStandardItemModel, QStandardItem, QFont

from pymdwizard.core import taxonomy
from pymdwizard.core import utils

from pymdwizard.gui.ui_files import UI_ThesaurusSearch


class ThesaurusSearch(QWidget):

    def __init__(self, add_term_function=None, parent=None, place=False):
        # QtGui.QMainWindow.__init__(self, parent)
        super(self.__class__, self).__init__()

        self.build_ui()
        self.connect_events()

        self.thesauri_lookup = {}
        self.thesauri_lookup_r = {}

        self.add_term_function = add_term_function

        self.place = place

    def load_iso(self):
        self.ui.label_search_term.hide()
        self.ui.search_term.hide()
        self.ui.button_search.hide()
        self.ui.label_search_results.text = "ISO 19115 Topic Categories"

        self.populate_thesauri_lookup()

        iso_url = "https://www2.usgs.gov/science/term.php?thcode=15&text=ISO 19115 Topic Category"
        results = requests.get(iso_url).json()

        thesaurus_name = "ISO 19115 Topic Category"
        branch = QStandardItem(thesaurus_name)
        branch.setFont(QFont('Arial', 11))
        for item in results['nt']:
            childnode = QStandardItem(item['name'])
            childnode.setFont(QFont('Arial', 9))
            branch.appendRow([childnode])

        model = QStandardItemModel(0, 0)
        # model.setHorizontalHeaderLabels(['Theme Keywords (thesaurus/keywords)'])

        rootNode = model.invisibleRootItem()
        rootNode.appendRow(branch)

        self.ui.treeview_results.setModel(model)
        # self.ui.treeview_results.setColumnWidth(0, 150)
        self.ui.treeview_results.expandAll()

    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_ThesaurusSearch.Ui_ThesaurusSearchWidget()
        self.ui.setupUi(self)

    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.button_search.clicked.connect(self.search_thesaurus)
        self.ui.search_term.returnPressed.connect(self.search_thesaurus)
        self.ui.treeview_results.doubleClicked.connect(self.add_term)
        self.ui.treeview_results.clicked.connect(self.show_details)
        self.ui.btn_add_term.clicked.connect(self.add_term)
        self.ui.btn_close.clicked.connect(self.close)
        # self.ui.button_gen_fgdc.clicked.connect(self.generate_fgdc)
        # self.ui.button_remove_selected.clicked.connect(self.remove_selected)
        # self.ui.table_include.doubleClicked.connect(self.remove_selected)

    def show_details(self, index):
        clicked_item = self.ui.treeview_results.model().itemFromIndex(index)
        parent = clicked_item.parent()

        if clicked_item.hasChildren():
            thcode = self.thesauri_lookup_r[clicked_item.text()]
            thname = clicked_item.text()

            THESAURUS_DETAILS_URL = "https://www2.usgs.gov/science/thesaurus.php?format=json&thcode={}"
            thesaurus_details_url = THESAURUS_DETAILS_URL.format(thcode)
            details = requests.get(thesaurus_details_url).json()

            details_msg = ''
            details_msg += '<b><font size="5" face="arial">{}</font></b><br>'.format(thname)
            uri = details['vocabulary']['uri']
            if uri:
                details_msg += '<a href="{}"><u><i><font size="4" face="arial" style="color:#386EC4">{}</font></i></u></a><br><br>'.format(uri, uri)

            details_msg += details['vocabulary']['scope']
        else:
            thcode = self.thesauri_lookup_r[parent.text()]
            details_url = "https://www2.usgs.gov/science/term.php?thcode={}&text={}".format(thcode, clicked_item.text())
            details = requests.get(details_url).json()
            if type(details) == dict:
                details = [details]

            details_msg = ''
            search_term = self.ui.search_term.text()
            prefered_shown = False
            for detail in details:

                term = detail["term"]
                uf = detail["uf"]
                bt = detail["bt"]
                nt = detail["nt"]
                rt = detail["rt"]

                if term['name'].lower() != search_term and \
                        not prefered_shown:
                    term_count = 0
                    prefered_shown = True
                    for alt_term in uf:
                        if alt_term['name'].lower() in search_term.lower():
                            term_count += 1
                            if term_count == 1:
                                details_msg += "The query matches the following non-preferred terms: "
                            else:
                                details_msg += ', '
                            details_msg += "<u>{}</u>".format(alt_term['name'])

                    if term_count > 0:
                        details_msg += '<br><br>'

                details_msg += '<b><font size="5" face="arial">{}</font></b><br>'.format(term['name'])
                details_msg += '<font size="4" face="arial">{}<br><br>'.format(term['scope'])


                if bt:
                    details_msg += "Broader terms: "
                    details_msg += " > ".join(['<u>{}</u>'.format(item['name']) for item in bt[::-1]])
                    details_msg += '<br>'


                if nt:
                    details_msg += " Narrower terms: "
                    details_msg += ", ".join(['<u>{}</u>'.format(item['name']) for item in nt])
                    details_msg += '<br>'

                if rt:
                    details_msg += " Related terms: "
                    details_msg += ", ".join(['<u>{}</u>'.format(item['name']) for item in rt])
                    details_msg += '<br>'

        self.ui.textBrowser.setText(details_msg)

    def populate_thesauri_lookup(self):
        if not self.thesauri_lookup:
            url = "https://www2.usgs.gov/science/thesaurus.php?format=json"
            result = requests.get(url).json()
            self.thesauri_lookup = {i['thcode']: i['name'] for i in result['vocabulary']}
            self.thesauri_lookup_r = {i['name']: i['thcode'] for i in result['vocabulary']}

    def search_thesaurus(self):

        self.populate_thesauri_lookup()

        search_url = "https://www2.usgs.gov/science/term-search.php?thcode=any&term={}".format(self.ui.search_term.text())
        results = requests.get(search_url).json()

        if not results:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("'{}' Not Found".format(self.ui.search_term.text()))
            msg.setInformativeText("The Metadata Wizard was unable to locate the provided search term in the controlled vocabulary search")
            msg.setWindowTitle("Keyword Not Found")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        branch_lookup = {}
        unique_children = []
        for item in results:
            thesaurus_name = self.thesauri_lookup[item['thcode']]
            if item['thcode'] != '1' and not self.place or \
               item['thcode'] == '1' and self.place:
                branch = branch_lookup.get(thesaurus_name, QStandardItem(thesaurus_name))
                branch.setFont(QFont('Arial', 11))
                childnode = QStandardItem(item['value'])
                childnode.setFont(QFont('Arial', 9))
                if (thesaurus_name, item['value']) not in unique_children:
                    branch.appendRow([childnode])
                    unique_children.append((thesaurus_name, item['value']))

                branch_lookup[thesaurus_name] = branch

        model = QStandardItemModel(0, 0)
        # model.setHorizontalHeaderLabels(['Theme Keywords (thesaurus/keywords)'])

        rootNode = model.invisibleRootItem()
        # branch1 = QStandardItem("Branch 1")
        # branch1.appendRow([QStandardItem("Child A")])
        # childnode = QStandardItem("Child B")
        # branch1.appendRow([childnode])
        #
        # branch2 = QStandardItem("Branch 2")
        # branch2.appendRow([QStandardItem("Child C")])
        # branch2.appendRow([QStandardItem("Child D")])

        for thesaurus_node in branch_lookup.items():
            rootNode.appendRow(thesaurus_node[1])
        # rootNode.appendRow([ branch1])
        # rootNode.appendRow([ branch2])

        self.ui.treeview_results.setModel(model)
        # self.ui.treeview_results.setColumnWidth(0, 150)
        self.ui.treeview_results.expandAll()


    def add_term(self, index):
        model = self.ui.treeview_results.model()
        for i in self.ui.treeview_results.selectedIndexes():
            clicked_item = model.itemFromIndex(i)
            parent = clicked_item.parent()
            keyword = clicked_item.text()

            if clicked_item.hasChildren():
                pass
            else:
                thesaurus = parent.text()
                self.add_term_function(keyword=keyword, thesaurus=thesaurus)

    def close(self):
        self.deleteLater()


if __name__ == '__main__':
    utils.launch_widget(ThesaurusSearch, "Thesaurus Search testing")
