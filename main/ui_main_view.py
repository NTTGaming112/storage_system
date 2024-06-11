# -*- coding: utf-8 -*-



################################################################################

## Form generated from reading UI file 'main_view.ui'

##

## Created by: Qt User Interface Compiler version 6.7.1

##

## WARNING! All changes made in this file will be lost when recompiling UI file!

################################################################################



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,

    QMetaObject, QObject, QPoint, QRect,

    QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,

    QFont, QFontDatabase, QGradient, QIcon,

    QImage, QKeySequence, QLinearGradient, QPainter,

    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,

    QHBoxLayout, QHeaderView, QLabel, QMainWindow,

    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,

    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

import resources_rc



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():

            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1271, 767)

        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);\n"

"color: rgb(0, 0, 0);")

        MainWindow.setDockNestingEnabled(False)

        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_2 = QGridLayout(self.centralwidget)

        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.icon_only_widget = QWidget(self.centralwidget)

        self.icon_only_widget.setObjectName(u"icon_only_widget")

        self.icon_only_widget.setStyleSheet(u"QWidget{\n"

"	background-color: rgb(31, 159, 239);\n"

"}\n"

"QPushButton{\n"

"	color:white;\n"

"	height:30px;\n"

"	border:none;\n"

"	border-radius:10px\n"

"}\n"

"QPushButton:checked{\n"

"	background-color: #F5FAFE;\n"

"	color: #1F95EF;\n"

"	font-weight:bold;\n"

"}")

        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)

        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.label = QLabel(self.icon_only_widget)

        self.label.setObjectName(u"label")

        self.label.setMinimumSize(QSize(40, 40))

        self.label.setMaximumSize(QSize(40, 40))

        self.label.setPixmap(QPixmap(u":/pic/profile.png"))

        self.label.setScaledContents(True)



        self.verticalLayout_3.addWidget(self.label)



        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.setObjectName(u"verticalLayout")

        self.user_1 = QPushButton(self.icon_only_widget)

        self.user_1.setObjectName(u"user_1")

        icon = QIcon()

        icon.addFile(u":/pic/product_icon.png", QSize(), QIcon.Normal, QIcon.Off)

        self.user_1.setIcon(icon)

        self.user_1.setCheckable(True)

        self.user_1.setChecked(True)

        self.user_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.user_1)



        self.product_1 = QPushButton(self.icon_only_widget)

        self.product_1.setObjectName(u"product_1")

        self.product_1.setIcon(icon)

        self.product_1.setCheckable(True)

        self.product_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.product_1)



        self.order_1 = QPushButton(self.icon_only_widget)

        self.order_1.setObjectName(u"order_1")

        self.order_1.setIcon(icon)

        self.order_1.setCheckable(True)

        self.order_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.order_1)



        self.thongke_1 = QPushButton(self.icon_only_widget)

        self.thongke_1.setObjectName(u"thongke_1")

        self.thongke_1.setIcon(icon)

        self.thongke_1.setCheckable(True)

        self.thongke_1.setAutoExclusive(True)



        self.verticalLayout.addWidget(self.thongke_1)





        self.verticalLayout_3.addLayout(self.verticalLayout)



        self.verticalSpacer = QSpacerItem(17, 467, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)



        self.verticalLayout_3.addItem(self.verticalSpacer)



        self.exit_0 = QPushButton(self.icon_only_widget)

        self.exit_0.setObjectName(u"exit_0")

        icon1 = QIcon()

        icon1.addFile(u":/pic/log_out.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_0.setIcon(icon1)

        self.exit_0.setCheckable(True)

        self.exit_0.setAutoExclusive(True)



        self.verticalLayout_3.addWidget(self.exit_0)





        self.gridLayout_2.addWidget(self.icon_only_widget, 0, 0, 1, 1)



        self.icon_name_widget = QWidget(self.centralwidget)

        self.icon_name_widget.setObjectName(u"icon_name_widget")

        self.icon_name_widget.setStyleSheet(u"QWidget{\n"

"	background-color: rgb(31, 159, 239);\n"

"}\n"

"QPushButton{\n"

"	color:white;\n"

"	text-align: left;	\n"

"	height:30px;\n"

"	border: none;\n"

"	padding-left:10px;\n"

"	border-top-left-radius: 10px;\n"

"	border-bottom-left-radius: 10px;\n"

"}\n"

"QPushButton:checked{\n"

"	background-color: #F5FAFE;\n"

"	color: #1F95EF;\n"

"	font-weight:bold;\n"

"}")

        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)

        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)

        self.horizontalLayout_2 = QHBoxLayout()

        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)

        self.label_2 = QLabel(self.icon_name_widget)

        self.label_2.setObjectName(u"label_2")

        self.label_2.setMinimumSize(QSize(40, 40))

        self.label_2.setMaximumSize(QSize(40, 40))

        self.label_2.setPixmap(QPixmap(u":/pic/profile.png"))

        self.label_2.setScaledContents(True)



        self.horizontalLayout_2.addWidget(self.label_2)



        self.label_3 = QLabel(self.icon_name_widget)

        self.label_3.setObjectName(u"label_3")

        font = QFont()

        font.setPointSize(12)

        font.setBold(True)

        self.label_3.setFont(font)



        self.horizontalLayout_2.addWidget(self.label_3)





        self.verticalLayout_4.addLayout(self.horizontalLayout_2)



        self.verticalLayout_2 = QVBoxLayout()

        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.user_2 = QPushButton(self.icon_name_widget)

        self.user_2.setObjectName(u"user_2")

        self.user_2.setIcon(icon)

        self.user_2.setCheckable(True)

        self.user_2.setChecked(True)

        self.user_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.user_2)



        self.product_2 = QPushButton(self.icon_name_widget)

        self.product_2.setObjectName(u"product_2")

        self.product_2.setIcon(icon)

        self.product_2.setCheckable(True)

        self.product_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.product_2)



        self.order_2 = QPushButton(self.icon_name_widget)

        self.order_2.setObjectName(u"order_2")

        self.order_2.setIcon(icon)

        self.order_2.setCheckable(True)

        self.order_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.order_2)



        self.thongke_2 = QPushButton(self.icon_name_widget)

        self.thongke_2.setObjectName(u"thongke_2")

        self.thongke_2.setIcon(icon)

        self.thongke_2.setCheckable(True)

        self.thongke_2.setAutoExclusive(True)



        self.verticalLayout_2.addWidget(self.thongke_2)





        self.verticalLayout_4.addLayout(self.verticalLayout_2)



        self.verticalSpacer_2 = QSpacerItem(20, 469, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)



        self.verticalLayout_4.addItem(self.verticalSpacer_2)



        self.exit_1 = QPushButton(self.icon_name_widget)

        self.exit_1.setObjectName(u"exit_1")

        self.exit_1.setIcon(icon1)

        self.exit_1.setCheckable(True)

        self.exit_1.setAutoExclusive(True)



        self.verticalLayout_4.addWidget(self.exit_1)





        self.gridLayout_2.addWidget(self.icon_name_widget, 0, 1, 1, 1)



        self.main_menu_widget = QWidget(self.centralwidget)

        self.main_menu_widget.setObjectName(u"main_menu_widget")

        self.main_menu_widget.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_6 = QGridLayout(self.main_menu_widget)

        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.stackedWidget = QStackedWidget(self.main_menu_widget)

        self.stackedWidget.setObjectName(u"stackedWidget")

        font1 = QFont()

        font1.setPointSize(14)

        self.stackedWidget.setFont(font1)

        self.stackedWidget.setStyleSheet(u"")

        self.user = QWidget()

        self.user.setObjectName(u"user")

        self.gridLayout_7 = QGridLayout(self.user)

        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.verticalLayout_6 = QVBoxLayout()

        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.table_user = QTableWidget(self.user)

        if (self.table_user.columnCount() < 7):

            self.table_user.setColumnCount(7)

        __qtablewidgetitem = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(0, __qtablewidgetitem)

        __qtablewidgetitem1 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(1, __qtablewidgetitem1)

        __qtablewidgetitem2 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        __qtablewidgetitem3 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        __qtablewidgetitem4 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(4, __qtablewidgetitem4)

        __qtablewidgetitem5 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(5, __qtablewidgetitem5)

        __qtablewidgetitem6 = QTableWidgetItem()

        self.table_user.setHorizontalHeaderItem(6, __qtablewidgetitem6)

        self.table_user.setObjectName(u"table_user")

        font2 = QFont()

        font2.setPointSize(14)

        font2.setBold(False)

        self.table_user.setFont(font2)

        self.table_user.setStyleSheet(u"color: rgb(0, 0, 0);\n"

"border-color: rgb(0, 0, 0);\n"

"background-color: rgb(204, 204, 204);")

        self.table_user.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table_user.setSortingEnabled(False)

        self.table_user.horizontalHeader().setMinimumSectionSize(100)

        self.table_user.horizontalHeader().setDefaultSectionSize(150)



        self.verticalLayout_6.addWidget(self.table_user)



        self.horizontalLayout_13 = QHBoxLayout()

        self.horizontalLayout_13.setSpacing(40)

        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalSpacer_14 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)



        self.add_user = QPushButton(self.user)

        self.add_user.setObjectName(u"add_user")

        font3 = QFont()

        font3.setPointSize(16)

        self.add_user.setFont(font3)

        self.add_user.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.add_user.setCheckable(False)

        self.add_user.setAutoExclusive(False)



        self.horizontalLayout_13.addWidget(self.add_user)



        self.edit_user = QPushButton(self.user)

        self.edit_user.setObjectName(u"edit_user")

        self.edit_user.setFont(font3)

        self.edit_user.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.edit_user.setCheckable(False)

        self.edit_user.setAutoExclusive(False)



        self.horizontalLayout_13.addWidget(self.edit_user)



        self.delete_user = QPushButton(self.user)

        self.delete_user.setObjectName(u"delete_user")

        self.delete_user.setFont(font3)

        self.delete_user.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.delete_user.setCheckable(False)

        self.delete_user.setAutoExclusive(False)



        self.horizontalLayout_13.addWidget(self.delete_user)



        self.horizontalSpacer_15 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)





        self.verticalLayout_6.addLayout(self.horizontalLayout_13)





        self.gridLayout_7.addLayout(self.verticalLayout_6, 0, 0, 1, 1)



        self.stackedWidget.addWidget(self.user)

        self.product = QWidget()

        self.product.setObjectName(u"product")

        self.gridLayout_9 = QGridLayout(self.product)

        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.verticalLayout_7 = QVBoxLayout()

        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_6 = QHBoxLayout()

        self.horizontalLayout_6.setSpacing(6)

        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalSpacer = QSpacerItem(498, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_6.addItem(self.horizontalSpacer)



        self.label_10 = QLabel(self.product)

        self.label_10.setObjectName(u"label_10")

        font4 = QFont()

        font4.setPointSize(12)

        self.label_10.setFont(font4)

        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_6.addWidget(self.label_10)



        self.comboBox_product = QComboBox(self.product)

        self.comboBox_product.setObjectName(u"comboBox_product")

        self.comboBox_product.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_6.addWidget(self.comboBox_product)





        self.verticalLayout_7.addLayout(self.horizontalLayout_6)



        self.table_product = QTableWidget(self.product)

        if (self.table_product.columnCount() < 5):

            self.table_product.setColumnCount(5)

        __qtablewidgetitem7 = QTableWidgetItem()

        self.table_product.setHorizontalHeaderItem(0, __qtablewidgetitem7)

        __qtablewidgetitem8 = QTableWidgetItem()

        self.table_product.setHorizontalHeaderItem(1, __qtablewidgetitem8)

        __qtablewidgetitem9 = QTableWidgetItem()

        self.table_product.setHorizontalHeaderItem(2, __qtablewidgetitem9)

        __qtablewidgetitem10 = QTableWidgetItem()

        self.table_product.setHorizontalHeaderItem(3, __qtablewidgetitem10)

        __qtablewidgetitem11 = QTableWidgetItem()

        self.table_product.setHorizontalHeaderItem(4, __qtablewidgetitem11)

        self.table_product.setObjectName(u"table_product")

        self.table_product.setFont(font1)

        self.table_product.setStyleSheet(u"color: rgb(0, 0, 0);\n"

"border-color: rgb(0, 0, 0);\n"

"background-color: rgb(204, 204, 204);")

        self.table_product.horizontalHeader().setMinimumSectionSize(100)

        self.table_product.horizontalHeader().setDefaultSectionSize(150)



        self.verticalLayout_7.addWidget(self.table_product)



        self.horizontalLayout_12 = QHBoxLayout()

        self.horizontalLayout_12.setSpacing(40)

        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalSpacer_12 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)



        self.load_product = QPushButton(self.product)

        self.load_product.setObjectName(u"load_product")

        self.load_product.setFont(font3)

        self.load_product.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.load_product.setCheckable(False)

        self.load_product.setAutoDefault(False)



        self.horizontalLayout_12.addWidget(self.load_product)



        self.add_product = QPushButton(self.product)

        self.add_product.setObjectName(u"add_product")

        self.add_product.setFont(font3)

        self.add_product.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.add_product.setCheckable(False)

        self.add_product.setAutoDefault(False)



        self.horizontalLayout_12.addWidget(self.add_product)



        self.edit_product = QPushButton(self.product)

        self.edit_product.setObjectName(u"edit_product")

        self.edit_product.setFont(font3)

        self.edit_product.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_12.addWidget(self.edit_product)



        self.delete_product = QPushButton(self.product)

        self.delete_product.setObjectName(u"delete_product")

        self.delete_product.setFont(font3)

        self.delete_product.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_12.addWidget(self.delete_product)



        self.horizontalSpacer_13 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)





        self.verticalLayout_7.addLayout(self.horizontalLayout_12)





        self.gridLayout_9.addLayout(self.verticalLayout_7, 0, 0, 1, 1)



        self.stackedWidget.addWidget(self.product)

        self.order = QWidget()

        self.order.setObjectName(u"order")

        self.gridLayout_10 = QGridLayout(self.order)

        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.verticalLayout_8 = QVBoxLayout()

        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout_8 = QHBoxLayout()

        self.horizontalLayout_8.setSpacing(20)

        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)



        self.horizontalLayout_4 = QHBoxLayout()

        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.label_8 = QLabel(self.order)

        self.label_8.setObjectName(u"label_8")

        self.label_8.setFont(font4)

        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_4.addWidget(self.label_8)



        self.comboBox_order_nameid = QComboBox(self.order)

        self.comboBox_order_nameid.setObjectName(u"comboBox_order_nameid")

        self.comboBox_order_nameid.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_4.addWidget(self.comboBox_order_nameid)





        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)





        self.verticalLayout_8.addLayout(self.horizontalLayout_8)



        self.table_order = QTableWidget(self.order)

        if (self.table_order.columnCount() < 5):

            self.table_order.setColumnCount(5)

        __qtablewidgetitem12 = QTableWidgetItem()

        self.table_order.setHorizontalHeaderItem(0, __qtablewidgetitem12)

        __qtablewidgetitem13 = QTableWidgetItem()

        self.table_order.setHorizontalHeaderItem(1, __qtablewidgetitem13)

        __qtablewidgetitem14 = QTableWidgetItem()

        self.table_order.setHorizontalHeaderItem(2, __qtablewidgetitem14)

        __qtablewidgetitem15 = QTableWidgetItem()

        self.table_order.setHorizontalHeaderItem(3, __qtablewidgetitem15)

        __qtablewidgetitem16 = QTableWidgetItem()

        self.table_order.setHorizontalHeaderItem(4, __qtablewidgetitem16)

        self.table_order.setObjectName(u"table_order")

        self.table_order.setFont(font1)

        self.table_order.setStyleSheet(u"color: rgb(0, 0, 0);\n"

"border-color: rgb(0, 0, 0);\n"

"background-color: rgb(204, 204, 204);")

        self.table_order.setSortingEnabled(False)

        self.table_order.setWordWrap(True)

        self.table_order.setCornerButtonEnabled(True)

        self.table_order.horizontalHeader().setMinimumSectionSize(100)

        self.table_order.horizontalHeader().setDefaultSectionSize(150)



        self.verticalLayout_8.addWidget(self.table_order)



        self.horizontalLayout_11 = QHBoxLayout()

        self.horizontalLayout_11.setSpacing(40)

        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.horizontalSpacer_10 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)



        self.load_order = QPushButton(self.order)

        self.load_order.setObjectName(u"load_order")

        self.load_order.setFont(font3)

        self.load_order.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.load_order.setChecked(False)



        self.horizontalLayout_11.addWidget(self.load_order)



        self.add_order = QPushButton(self.order)

        self.add_order.setObjectName(u"add_order")

        self.add_order.setFont(font3)

        self.add_order.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.add_order.setChecked(False)



        self.horizontalLayout_11.addWidget(self.add_order)



        self.delete_order = QPushButton(self.order)

        self.delete_order.setObjectName(u"delete_order")

        self.delete_order.setFont(font3)

        self.delete_order.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.horizontalLayout_11.addWidget(self.delete_order)



        self.horizontalSpacer_11 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)





        self.verticalLayout_8.addLayout(self.horizontalLayout_11)





        self.gridLayout_10.addLayout(self.verticalLayout_8, 0, 0, 1, 1)



        self.stackedWidget.addWidget(self.order)

        self.doanhthu = QWidget()

        self.doanhthu.setObjectName(u"doanhthu")

        self.gridLayout = QGridLayout(self.doanhthu)

        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalSpacer_3 = QSpacerItem(810, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)



        self.label_11 = QLabel(self.doanhthu)

        self.label_11.setObjectName(u"label_11")

        self.label_11.setFont(font4)

        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)



        self.comboBox_thongke = QComboBox(self.doanhthu)

        self.comboBox_thongke.addItem("")

        self.comboBox_thongke.addItem("")

        self.comboBox_thongke.addItem("")

        self.comboBox_thongke.setObjectName(u"comboBox_thongke")

        self.comboBox_thongke.setMinimumSize(QSize(80, 30))

        self.comboBox_thongke.setStyleSheet(u"color: rgb(0, 0, 0);")



        self.gridLayout.addWidget(self.comboBox_thongke, 0, 2, 1, 1)



        self.table_thongke = QTableWidget(self.doanhthu)

        self.table_thongke.setObjectName(u"table_thongke")

        self.table_thongke.setFont(font1)

        self.table_thongke.setStyleSheet(u"color: rgb(0, 0, 0);\n"

"border-color: rgb(0, 0, 0);\n"

"background-color: rgb(204, 204, 204);")

        self.table_thongke.horizontalHeader().setMinimumSectionSize(100)

        self.table_thongke.horizontalHeader().setDefaultSectionSize(150)



        self.gridLayout.addWidget(self.table_thongke, 1, 0, 1, 3)



        self.horizontalLayout_9 = QHBoxLayout()

        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.horizontalSpacer_20 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)



        self.load_thongke = QPushButton(self.doanhthu)

        self.load_thongke.setObjectName(u"load_thongke")

        self.load_thongke.setFont(font3)

        self.load_thongke.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.load_thongke.setChecked(False)



        self.horizontalLayout_9.addWidget(self.load_thongke)



        self.horizontalSpacer_21 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)





        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 3)



        self.stackedWidget.addWidget(self.doanhthu)



        self.gridLayout_6.addWidget(self.stackedWidget, 1, 0, 1, 1)



        self.header_widget = QWidget(self.main_menu_widget)

        self.header_widget.setObjectName(u"header_widget")

        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)

        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.menu = QPushButton(self.header_widget)

        self.menu.setObjectName(u"menu")

        self.menu.setStyleSheet(u"border:none;\n"

"")

        icon2 = QIcon()

        icon2.addFile(u":/pic/menu.png", QSize(), QIcon.Normal, QIcon.Off)

        self.menu.setIcon(icon2)

        self.menu.setIconSize(QSize(20, 20))

        self.menu.setCheckable(True)



        self.horizontalLayout_3.addWidget(self.menu)



        self.horizontalSpacer_2 = QSpacerItem(227, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)



        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)



        self.edit_mode_button = QPushButton(self.header_widget)

        self.edit_mode_button.setObjectName(u"edit_mode_button")



        self.horizontalLayout_3.addWidget(self.edit_mode_button)



        self.horizontalLayout = QHBoxLayout()

        self.horizontalLayout.setObjectName(u"horizontalLayout")



        self.horizontalLayout_3.addLayout(self.horizontalLayout)



        self.profile = QPushButton(self.header_widget)

        self.profile.setObjectName(u"profile")

        self.profile.setStyleSheet(u"border:none;")

        icon3 = QIcon()

        icon3.addFile(u":/pic/profile.png", QSize(), QIcon.Normal, QIcon.Off)

        self.profile.setIcon(icon3)



        self.horizontalLayout_3.addWidget(self.profile)





        self.gridLayout_6.addWidget(self.header_widget, 0, 0, 1, 1)





        self.gridLayout_2.addWidget(self.main_menu_widget, 0, 2, 1, 1)



        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)

        self.menu.toggled.connect(self.icon_only_widget.setHidden)

        self.menu.toggled.connect(self.icon_name_widget.setVisible)

        self.order_1.toggled.connect(self.order_2.setChecked)

        self.product_1.toggled.connect(self.product_2.setChecked)

        self.user_1.toggled.connect(self.user_2.setChecked)

        self.exit_0.toggled.connect(self.exit_1.setChecked)

        self.user_2.toggled.connect(self.user_1.setChecked)

        self.product_2.toggled.connect(self.product_1.setChecked)

        self.order_2.toggled.connect(self.order_1.setChecked)

        self.exit_0.toggled.connect(MainWindow.close)

        self.exit_1.toggled.connect(MainWindow.close)

        self.thongke_1.toggled.connect(self.thongke_2.setChecked)

        self.thongke_2.toggled.connect(self.thongke_1.setChecked)



        self.user_1.setDefault(False)

        self.stackedWidget.setCurrentIndex(2)





        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.label.setText("")

        self.user_1.setText("")

        self.product_1.setText("")

        self.order_1.setText("")

        self.thongke_1.setText("")

        self.exit_0.setText("")

        self.label_2.setText("")

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))

        self.user_2.setText(QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng", None))

        self.product_2.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n ph\u1ea9m", None))

        self.order_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ee3n h\u00e0ng", None))

        self.thongke_2.setText(QCoreApplication.translate("MainWindow", u"Doanh thu", None))

        self.exit_1.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))

        ___qtablewidgetitem = self.table_user.horizontalHeaderItem(0)

        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));

        ___qtablewidgetitem1 = self.table_user.horizontalHeaderItem(1)

        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));

        ___qtablewidgetitem2 = self.table_user.horizontalHeaderItem(2)

        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None));

        ___qtablewidgetitem3 = self.table_user.horizontalHeaderItem(3)

        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None));

        ___qtablewidgetitem4 = self.table_user.horizontalHeaderItem(4)

        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"S\u0110T", None));

        ___qtablewidgetitem5 = self.table_user.horizontalHeaderItem(5)

        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email", None));

        ___qtablewidgetitem6 = self.table_user.horizontalHeaderItem(6)

        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Checkbox", None));

        self.add_user.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))

        self.edit_user.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))

        self.delete_user.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Category", None))

        ___qtablewidgetitem7 = self.table_product.horizontalHeaderItem(0)

        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Id", None));

        ___qtablewidgetitem8 = self.table_product.horizontalHeaderItem(1)

        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));

        ___qtablewidgetitem9 = self.table_product.horizontalHeaderItem(2)

        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));

        ___qtablewidgetitem10 = self.table_product.horizontalHeaderItem(3)

        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None));

        ___qtablewidgetitem11 = self.table_product.horizontalHeaderItem(4)

        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Checkbox", None));

        self.load_product.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i", None))

        self.add_product.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))

        self.edit_product.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))

        self.delete_product.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None))

        ___qtablewidgetitem12 = self.table_order.horizontalHeaderItem(0)

        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Id", None));

        ___qtablewidgetitem13 = self.table_order.horizontalHeaderItem(1)

        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y gi\u1edd", None));

        ___qtablewidgetitem14 = self.table_order.horizontalHeaderItem(2)

        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng s\u1ed1 ti\u1ec1n", None));

        ___qtablewidgetitem15 = self.table_order.horizontalHeaderItem(3)

        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin chi ti\u1ebft", None));

        ___qtablewidgetitem16 = self.table_order.horizontalHeaderItem(4)

        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Checkbox", None));

        self.load_order.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i", None))

        self.add_order.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))

        self.delete_order.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Th\u1ed1ng k\u00ea theo", None))

        self.comboBox_thongke.setItemText(0, QCoreApplication.translate("MainWindow", u"ng\u00e0y", None))

        self.comboBox_thongke.setItemText(1, QCoreApplication.translate("MainWindow", u"th\u00e1ng", None))

        self.comboBox_thongke.setItemText(2, QCoreApplication.translate("MainWindow", u"n\u0103m", None))



        self.load_thongke.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i", None))

        self.menu.setText("")

        self.edit_mode_button.setText(QCoreApplication.translate("MainWindow", u"B\u1eadt ch\u1ebf \u0111\u1ed9 ch\u1ec9nh s\u1eeda", None))

        self.profile.setText("")

    # retranslateUi



