# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daoru.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_daorudialog(object):
    def setupUi(self, daorudialog):
        daorudialog.setObjectName("daorudialog")
        daorudialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(daorudialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtWidgets.QTreeWidget(daorudialog)
        self.treeWidget.setGeometry(QtCore.QRect(40, 50, 301, 171))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")

        self.retranslateUi(daorudialog)
        self.buttonBox.accepted.connect(daorudialog.accept)
        self.buttonBox.rejected.connect(daorudialog.reject)
        QtCore.QMetaObject.connectSlotsByName(daorudialog)

    def retranslateUi(self, daorudialog):
        _translate = QtCore.QCoreApplication.translate
        daorudialog.setWindowTitle(_translate("daorudialog", "导入"))
