# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(697, 403)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setStyleSheet(_fromUtf8(""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.webView = QtWebKit.QWebView(self.widget)
        self.webView.setStyleSheet(_fromUtf8(""))
        self.webView.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_4.addWidget(self.webView, 0, 0, 1, 1)
        self.tool = QtGui.QWidget(self.widget)
        self.tool.setGeometry(QtCore.QRect(10, 10, 245, 280))
        self.tool.setAutoFillBackground(True)
        self.tool.setStyleSheet(_fromUtf8(""))
        self.tool.setObjectName(_fromUtf8("tool"))
        self.gridLayout = QtGui.QGridLayout(self.tool)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolBox = QtGui.QFrame(self.tool)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.formLayout = QtGui.QFormLayout(self.toolBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox = QtGui.QGroupBox(self.toolBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(185, 156))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_1 = QtGui.QLabel(self.groupBox)
        self.label_1.setToolTip(_fromUtf8(""))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.lcdNumber_sent = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_sent.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_sent.setObjectName(_fromUtf8("lcdNumber_sent"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lcdNumber_sent)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setToolTip(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lcdNumber_speed = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_speed.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_speed.setObjectName(_fromUtf8("lcdNumber_speed"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lcdNumber_speed)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setToolTip(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lcdNumber_last = QtGui.QLCDNumber(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_last.sizePolicy().hasHeightForWidth())
        self.lcdNumber_last.setSizePolicy(sizePolicy)
        self.lcdNumber_last.setDigitCount(8)
        self.lcdNumber_last.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_last.setObjectName(_fromUtf8("lcdNumber_last"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lcdNumber_last)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.toolBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(185, 125))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioButtonChat = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonChat.setCheckable(True)
        self.radioButtonChat.setChecked(True)
        self.radioButtonChat.setObjectName(_fromUtf8("radioButtonChat"))
        self.gridLayout_2.addWidget(self.radioButtonChat, 0, 0, 1, 1)
        self.pushButtonconfig = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonconfig.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonconfig.setIcon(icon)
        self.pushButtonconfig.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonconfig.setFlat(True)
        self.pushButtonconfig.setObjectName(_fromUtf8("pushButtonconfig"))
        self.gridLayout_2.addWidget(self.pushButtonconfig, 0, 1, 2, 1)
        self.radioButtonFav = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonFav.setEnabled(False)
        self.radioButtonFav.setObjectName(_fromUtf8("radioButtonFav"))
        self.gridLayout_2.addWidget(self.radioButtonFav, 1, 0, 1, 1)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.groupBox_2)
        self.splitter = QtGui.QSplitter(self.toolBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pushButtonStart = QtGui.QPushButton(self.splitter)
        self.pushButtonStart.setAutoDefault(True)
        self.pushButtonStart.setDefault(True)
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.pushButtonStop = QtGui.QPushButton(self.splitter)
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.splitter)
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.toolButton = QtGui.QToolButton(self.tool)
        self.toolButton.setMaximumSize(QtCore.QSize(24, 24))
        self.toolButton.setStyleSheet(_fromUtf8(""))
        self.toolButton.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton.setArrowType(QtCore.Qt.LeftArrow)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.webView.raise_()
        self.tool.raise_()
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.on_hide)
        QtCore.QObject.connect(self.pushButtonStart, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.on_start)
        QtCore.QObject.connect(self.radioButtonChat, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.toolbarModeSelected)
        QtCore.QObject.connect(self.pushButtonconfig, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.configWindow)
        QtCore.QObject.connect(self.pushButtonStop, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.on_stop)
        QtCore.QObject.connect(self.radioButtonFav, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.toolbarModeSelected)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.groupBox.setTitle(_translate("MainWindow", "|Statistics", None))
        self.label_1.setText(_translate("MainWindow", "Sent", None))
        self.lcdNumber_sent.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Число отправленных сообщений</span></p></body></html>", None))
        self.lcdNumber_sent.setWhatsThis(_translate("MainWindow", "Количество отправленных сообщений (или писем)", None))
        self.label_2.setText(_translate("MainWindow", "Speed", None))
        self.lcdNumber_speed.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Скорость отправки</span></p></body></html>", None))
        self.lcdNumber_speed.setWhatsThis(_translate("MainWindow", "Скорость отправки сообщений (писем) штук в секунду.", None))
        self.label_3.setText(_translate("MainWindow", "Remains", None))
        self.lcdNumber_last.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Оставшееся время до конца рассылки</span></p></body></html>", None))
        self.lcdNumber_last.setWhatsThis(_translate("MainWindow", "Оставшееся время до завершения рассылки.", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "|Mode", None))
        self.radioButtonChat.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Режим рассылки в чат</span></p></body></html>", None))
        self.radioButtonChat.setWhatsThis(_translate("MainWindow", "Выбор режима рассылки в чат", None))
        self.radioButtonChat.setText(_translate("MainWindow", "& Chat", None))
        self.pushButtonconfig.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Настройки программы</span></p></body></html>", None))
        self.radioButtonFav.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Режим рассылки для поклонников</span></p></body></html>", None))
        self.radioButtonFav.setWhatsThis(_translate("MainWindow", "Выбор режима рассылки по поклонникам", None))
        self.radioButtonFav.setText(_translate("MainWindow", "&Friends", None))
        self.pushButtonStart.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Запуск рассылки</span></p></body></html>", None))
        self.pushButtonStart.setWhatsThis(_translate("MainWindow", "Запуск рассылки", None))
        self.pushButtonStart.setText(_translate("MainWindow", "&Start", None))
        self.pushButtonStop.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Остановить рассылку</span></p></body></html>", None))
        self.pushButtonStop.setWhatsThis(_translate("MainWindow", "Остановка рассылки", None))
        self.pushButtonStop.setText(_translate("MainWindow", "&Stop", None))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Скрыть панель инструментов</span></p></body></html>", None))

from PyQt4 import QtWebKit
import resource_rc
