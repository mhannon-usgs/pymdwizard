#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Citation <citation> section


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.

Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.

Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""

from lxml import etree

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView, QFormLayout
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit, QRadioButton, QFrame
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle, QScrollArea, QGroupBox
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint



from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_Citation #


class Citation(WizardWidget): #

    drag_label = "Citation <citation>"


    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_Citation.Ui_Form()#.Ui_USGSContactInfoWidgetMain()
        self.ui.setupUi(self)
        self.setup_dragdrop(self)
        self.ui.lworkcite_ext.hide()
        self.ui.series_ext.hide()
        self.ui.pub_ext.hide()


    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.radioButton.toggled.connect(self.include_lworkext_change)
        self.ui.radioButton_3.toggled.connect(self.include_seriesext_change)
        self.ui.radioButton_5.toggled.connect(self.include_pubext_change)


    def include_seriesext_change(self, b):
        if b:
            self.ui.series_ext.show()
        else:
            self.ui.series_ext.hide()

    def include_pubext_change(self, b):
        if b:
            self.ui.pub_ext.show()
        else:
            self.ui.pub_ext.hide()

    def include_lworkext_change(self, b):
        if b:
            self.ui.lworkcite_ext.show()
            #self.ui.main_layout.addWidget(self.cit)
            self.lworkcit = Citation()
            #layout = self.findChild(QFrame, "frame").layout()
            self.lworkcit.findChild(QGroupBox, "fgdc_lworkcit").deleteLater()

            hBoxLayout = QHBoxLayout()
            hBoxLayout.addWidget(self.lworkcit)
            lwork_ext = self.findChild(QFrame, "lworkcit_ext")
            print lwork_ext
            #lwork_ext.setFixedSize(500,500)
            lwork_ext.setLayout(hBoxLayout)
            #########################################
            #scrollarea = QScrollArea(lwork_ext)
            #scrollarea.setWidgetResizable(True)
            #lwork_ext.addWidget(self.lworkcit)
            ####
            #self.lworkcit.
            #self.lworkcit.add_lwork = QGroupBox(self.lworkcit.ui.fgdc_citeinfo)
            # self.fgdc_pubinfo.setTitle("")
            #self.lworkcit.add_lwork.setObjectName("add_lwork")
            #self.lworkcit.ui.horizontalLayout_30.addWidget(self.lworkcit.add_lwork)
            # self.horizontalLayout_30.addWidget(self.fgdc_pubinfo)
            #self.ui.formLayout_2.setLayout(3, QFormLayout.SpanningRole, self.ui.horizontalLayout_30)
        else:
            self.ui.lworkcite_ext.hide()


    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'citation'
        Parameters
        ----------
        e : qt event

        Returns
        -------


        """
        print("pc drag enter")
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element.tag == 'citation':
#                print "element", element.text
#                print "tag", element.tag
                #mime_data.setText(element.text)
                #print mime_data.text()
                #self.Q.setPlainText(_translate("Form", element.text))
                e.accept()
        else:
            e.ignore()


         
                
    def _to_xml(self):
        """
        encapsulates the QLineEdit text in an element tag

        Returns
        -------
        citation element tag in xml tree
        """
        citation = etree.Element('citation')
        citeinfo = etree.Element('citeinfo')
        origin = etree.Element("origin")
        pubdate = etree.Element("pubdate")
        edition = etree.Element("edition")
        geoform = etree.Element("geoform")
        title = etree.Element("title")
        onlink = etree.Element("onlink")
        origin.text = self.findChild(QLineEdit, "fgdc_origin").text()
        pubdate.text = self.findChild(QLineEdit, "fgdc_pubdate").text()
        title.text = self.findChild(QLineEdit, "fgdc_title").text()
        edition.text = self.findChild(QLineEdit, "fgdc_edition").text()
        geoform.text = self.findChild(QComboBox, "fgdc_geoform").currentText()
        onlink.text = self.findChild(QLineEdit, "fgdc_onlink").text()

        citeinfo.append(origin)
        citeinfo.append(pubdate)
        citeinfo.append(title)
        citeinfo.append(edition)
        citeinfo.append(geoform)

        if self.ui.radioButton_3.isChecked():
            serinfo = etree.Element("serinfo")
            sername = etree.Element("sername")
            sername.text = self.findChild(QLineEdit, "fgdc_sername").text()
            issue = etree.Element("issue")
            issue.text = self.findChild(QLineEdit, "fgdc_issue").text()
            serinfo.append(sername)
            serinfo.append(issue)
            citeinfo.append(serinfo)

        else:
            pass

        if self.ui.radioButton_5.isChecked():
            pubinfo = etree.Element("pubinfo")
            pubplace = etree.Element("pubplace")
            pubplace.text = self.findChild(QLineEdit, "fgdc_pubplace").text()
            publish = etree.Element("publish")
            publish.text = self.findChild(QLineEdit, "fgdc_publish").text()
            pubinfo.append(pubplace)
            pubinfo.append(publish)
            citeinfo.append(pubinfo)

        else:
            pass
########################################################################################################
        if self.ui.radioButton.isChecked():
            lworkcit1 = etree.Element('lworkcit')
            citeinfo1 = etree.Element('citeinfo')
            origin1 = etree.Element("origin")
            pubdate1 = etree.Element("pubdate")
            edition1 = etree.Element("edition")
            geoform1 = etree.Element("geoform")
            title1 = etree.Element("title")
            onlink1 = etree.Element("onlink")
            origin1.text = self.lworkcit.findChild(QLineEdit, "fgdc_origin").text()
            pubdate1.text = self.lworkcit.findChild(QLineEdit, "fgdc_pubdate").text()
            title1.text = self.lworkcit.findChild(QLineEdit, "fgdc_title").text()
            edition1.text = self.lworkcit.findChild(QLineEdit, "fgdc_edition").text()
            geoform1.text = self.lworkcit.findChild(QComboBox, "fgdc_geoform").currentText()
            onlink1.text = self.lworkcit.findChild(QLineEdit, "fgdc_onlink").text()

            citeinfo1.append(origin1)
            citeinfo1.append(pubdate1)
            citeinfo1.append(title1)
            citeinfo1.append(edition1)
            citeinfo1.append(geoform1)

            if self.lworkcit.ui.radioButton_3.isChecked():
                serinfo1 = etree.Element("serinfo")
                sername1 = etree.Element("sername")
                sername1.text = self.lworkcit.findChild(QLineEdit, "fgdc_sername").text()
                issue1 = etree.Element("issue")
                issue1.text = self.lworkcit.findChild(QLineEdit, "fgdc_issue").text()
                serinfo1.append(sername1)
                serinfo1.append(issue1)
                citeinfo1.append(serinfo1)

            else:
                pass

            if self.lworkcit.ui.radioButton_5.isChecked():
                pubinfo1 = etree.Element("pubinfo")
                pubplace1 = etree.Element("pubplace")
                pubplace1.text = self.lworkcit.findChild(QLineEdit, "fgdc_pubplace").text()
                publish1 = etree.Element("publish")
                publish1.text = self.lworkcit.findChild(QLineEdit, "fgdc_publish").text()
                pubinfo1.append(pubplace1)
                pubinfo1.append(publish1)
                citeinfo1.append(pubinfo1)

            lworkcit1.append(citeinfo1)
#####################################################################################################################
            citeinfo.append(lworkcit1)
        citeinfo.append(onlink)

        #print "ok"
        citation.append(citeinfo)
        return citation

    def _from_xml(self, citation):
        """
        parses the xml code into the relevant citation elements

        Parameters
        ----------
        citation - the xml element status and its contents

        Returns
        -------
        None
        """
        try:
            if citation.tag == "citation":
                print citation.tag
                #print citation.text
                if citation.findall("citeinfo/origin"):
                    origin_text = citation.findtext("citeinfo/origin")
                    print origin_text

                    origin_box = self.findChild(QLineEdit, 'fgdc_origin')
                    origin_box.setText(origin_text)
                else:
                    print ("No origin tag")

                if citation.findall("citeinfo/pubdate"):
                    pubdate_text = citation.findtext("citeinfo/pubdate")
                    print pubdate_text

                    pubdate_box = self.findChild(QLineEdit, 'fgdc_pubdate')
                    pubdate_box.setText(pubdate_text)
                else:
                    print ("No pubdate tag")

                if citation.findall("citeinfo/title"):
                    title_text = citation.findtext("citeinfo/title")
                    print title_text

                    title_box = self.findChild(QLineEdit, 'fgdc_title')
                    title_box.setText(title_text)
                else:
                    print ("No title tag")

                if citation.findall("citeinfo/edition"):
                    edition_text = citation.findtext("citeinfo/edition")
                    print edition_text

                    edition_box = self.findChild(QLineEdit, 'fgdc_edition')
                    edition_box.setText(edition_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/geoform"):
                    geoform_text = citation.findtext("citeinfo/geoform")
                    print geoform_text

                    geoform_box = self.findChild(QComboBox, 'fgdc_geoform')
                    geoform_box.setCurrentText(geoform_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/onlink"):
                    onlink_text = citation.findtext("citeinfo/onlink")
                    print onlink_text

                    onlink_box = self.findChild(QLineEdit, 'fgdc_onlink')
                    onlink_box.setText(onlink_text)
                else:
                    print ("No onlink tag")

                if citation.findall("citeinfo/serinfo"):
                    self.ui.radioButton_3.setChecked(True)
                    sername_text = citation.findtext("citeinfo/serinfo/sername")
                    print sername_text

                    sername_box = self.findChild(QLineEdit, 'fgdc_sername')
                    sername_box.setText(sername_text)

                    issue_text = citation.findtext("citeinfo/serinfo/issue")
                    print issue_text

                    issue_box = self.findChild(QLineEdit, 'fgdc_issue')
                    issue_box.setText(issue_text)

                else:
                    print ("No series name tag")

                if citation.findall("citeinfo/pubinfo"):
                    self.ui.radioButton_5.setChecked(True)
                    pubplace_text = citation.findtext("citeinfo/pubinfo/pubplace")
                    print pubplace_text

                    pub_box = self.findChild(QLineEdit, 'fgdc_pubplace')
                    pub_box.setText(pubplace_text)

                    publish_text = citation.findtext("citeinfo/pubinfo/publish")
                    print publish_text

                    publish_box = self.findChild(QLineEdit, 'fgdc_publish')
                    publish_box.setText(publish_text)

                else:
                    print ("No pub tag")

                    ##############################################################################################################

                if citation.findall("citeinfo/lworkcit"):
                    self.ui.radioButton.setChecked(True)
                    if citation.findall("citeinfo/lworkcit/citeinfo/origin"):
                        origin_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/origin")
                        print origin_text1

                        origin_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_origin')
                        origin_box1.setText(origin_text1)
                    else:
                        print ("No origin tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/origin"):
                        pubdate_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubdate")
                        print pubdate_text1

                        pubdate_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_pubdate')
                        pubdate_box1.setText(pubdate_text1)
                    else:
                        print ("No pubdate tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/title"):
                        title_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/title")
                        print title_text1

                        title_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_title')
                        title_box1.setText(title_text1)
                    else:
                        print ("No title tag")

                    if citation.findall("lworkcit/citeinfo/edition"):
                        edition_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/edition")
                        print edition_text1

                        edition_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_edition')
                        edition_box1.setText(edition_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/geoform"):
                        geoform_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/geoform")
                        print geoform_text1

                        geoform_box1 = self.lworkcit.findChild(QComboBox, 'fgdc_geoform')
                        geoform_box1.setCurrentText(geoform_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/onlink"):
                        onlink_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/onlink")
                        print onlink_text1

                        onlink_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_onlink')
                        onlink_box1.setText(onlink_text1)
                    else:
                        print ("No onlink tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/serinfo"):
                        self.lworkcit.ui.radioButton_3.setChecked(True)
                        sername_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/serinfo/sername")
                        print sername_text1

                        sername_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_sername')
                        sername_box1.setText(sername_text1)

                        issue_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/serinfo/issue")
                        print issue_text1

                        issue_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_issue')
                        issue_box1.setText(issue_text1)

                    else:
                        print ("No series name tag")

                    if citation.findall("citeinfo/lworkcit/citeinfo/pubinfo"):
                        self.lworkcit.ui.radioButton_5.setChecked(True)
                        pubplace_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubinfo/pubplace")
                        print pubplace_text1

                        pub_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_pubplace')
                        pub_box1.setText(pubplace_text1)

                        publish_text1 = citation.findtext("citeinfo/lworkcit/citeinfo/pubinfo/publish")
                        print publish_text1

                        publish_box1 = self.lworkcit.findChild(QLineEdit, 'fgdc_publish')
                        publish_box1.setText(publish_text1)

                    else:
                        print ("No series issue tag")

                        ###########################################################################################


            else:
                print ("The tag is not citation")



        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(Citation,
                        "Citation testing")

