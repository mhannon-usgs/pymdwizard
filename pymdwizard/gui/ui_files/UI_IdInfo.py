# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_idinfo(object):
    def setupUi(self, fgdc_idinfo):
        fgdc_idinfo.setObjectName("fgdc_idinfo")
        fgdc_idinfo.resize(710, 845)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_idinfo)
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(fgdc_idinfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 25))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(15, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(321, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 1, 110, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(15, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(79, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idinfo_scroll_area = QtWidgets.QScrollArea(fgdc_idinfo)
        self.idinfo_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.idinfo_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.idinfo_scroll_area.setWidgetResizable(True)
        self.idinfo_scroll_area.setObjectName("idinfo_scroll_area")
        self.idinfo_main_widget = QtWidgets.QWidget()
        self.idinfo_main_widget.setGeometry(QtCore.QRect(0, 0, 706, 804))
        self.idinfo_main_widget.setObjectName("idinfo_main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.idinfo_main_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_citation = QtWidgets.QFrame(self.idinfo_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_citation.sizePolicy().hasHeightForWidth())
        self.frame_citation.setSizePolicy(sizePolicy)
        self.frame_citation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_citation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_citation.setObjectName("frame_citation")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_citation)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3.addWidget(self.frame_citation)
        self.two_column = QtWidgets.QFrame(self.idinfo_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_column.sizePolicy().hasHeightForWidth())
        self.two_column.setSizePolicy(sizePolicy)
        self.two_column.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.two_column.setFrameShadow(QtWidgets.QFrame.Raised)
        self.two_column.setObjectName("two_column")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.two_column)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.two_column_left = QtWidgets.QFrame(self.two_column)
        self.two_column_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.two_column_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.two_column_left.setObjectName("two_column_left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.two_column_left)
        self.verticalLayout_5.setContentsMargins(0, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 378, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.two_column_left)
        self.two_column_right = QtWidgets.QFrame(self.two_column)
        self.two_column_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.two_column_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.two_column_right.setObjectName("two_column_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.two_column_right)
        self.verticalLayout_4.setContentsMargins(3, 3, 0, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 378, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4.addWidget(self.two_column_right)
        self.verticalLayout_3.addWidget(self.two_column)
        self.idinfo_scroll_area.setWidget(self.idinfo_main_widget)
        self.horizontalLayout_2.addWidget(self.idinfo_scroll_area)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fgdc_idinfo)
        QtCore.QMetaObject.connectSlotsByName(fgdc_idinfo)

    def retranslateUi(self, fgdc_idinfo):
        _translate = QtCore.QCoreApplication.translate
        fgdc_idinfo.setWindowTitle(_translate("fgdc_idinfo", "Form"))
        self.label_5.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_5.setText(_translate("fgdc_idinfo", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; color:#55aaff;\">Provide general Information about the data set.</span></p></body></html>"))
        self.label_4.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_4.setText(_translate("fgdc_idinfo", "<html><head/><body><p><span style=\" font-size:15pt; color:#55aaff;\">*</span></p></body></html>"))
        self.label_3.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_3.setText(_translate("fgdc_idinfo", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; color:#55aaff;\">= Required</span></p></body></html>"))

