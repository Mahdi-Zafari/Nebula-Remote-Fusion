from PyQt5 import QtCore, QtGui, QtWidgets
from . import core

class Ui_main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_top = QtWidgets.QWidget(self.centralwidget)
        self.widget_top.setGeometry(QtCore.QRect(10, 10, 430, 40))
        self.widget_top.setStyleSheet("QWidget{\n"
"    background-color: #202020;\n"
"    border-top-right-radius:13px;\n"
"    border-top-left-radius:13px;\n"
"}")
        self.widget_top.setObjectName("widget_top")
        self.Button_minimized = QtWidgets.QPushButton(self.widget_top)
        self.Button_minimized.setGeometry(QtCore.QRect(330, 0, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        self.Button_minimized.setFont(font)
        self.Button_minimized.setStyleSheet("QPushButton{\n"
"    background-color: #202020;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #424242;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: #313131;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    color: #fff;\n"
"}")
        self.Button_minimized.setObjectName("Button_minimized")
        self.Button_exit = QtWidgets.QPushButton(self.widget_top)
        self.Button_exit.setGeometry(QtCore.QRect(380, 0, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Button_exit.setFont(font)
        self.Button_exit.setStyleSheet("QPushButton{\n"
"    background-color: #202020;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(170, 0, 0);\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #fff;\n"
"}")
        self.Button_exit.setObjectName("Button_exit")
        self.label_title = QtWidgets.QLabel(self.widget_top)
        self.label_title.setGeometry(QtCore.QRect(49, 10, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #ebe9fc;")
        self.label_title.setObjectName("label_title")
        self.label_icon = QtWidgets.QLabel(self.widget_top)
        self.label_icon.setGeometry(QtCore.QRect(10, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_icon.setFont(font)
        self.label_icon.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/img/img/nebula-RF-logo.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 430, 640))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: #212121;\n"
"    border-bottom-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.btn_open_nav_menu = QtWidgets.QPushButton(self.widget)
        self.btn_open_nav_menu.setGeometry(QtCore.QRect(10, 10, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_open_nav_menu.setFont(font)
        self.btn_open_nav_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open_nav_menu.setStyleSheet("QPushButton{\n"
"    background-color: #2f2f2f;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #424242;\n"
"border-radius:10px;\n"
"}")
        self.btn_open_nav_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_nav_menu.setIcon(icon)
        self.btn_open_nav_menu.setIconSize(QtCore.QSize(30, 30))
        self.btn_open_nav_menu.setObjectName("btn_open_nav_menu")
        self.widget_more = QtWidgets.QWidget(self.widget)
        self.widget_more.setGeometry(QtCore.QRect(0, 0, 430, 640))
        self.widget_more.setStyleSheet("QWidget{\n"
"    background-color: #212121;\n"
"    border-bottom-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget_more.setObjectName("widget_more")
        self.widget_setting_1 = QtWidgets.QWidget(self.widget_more)
        self.widget_setting_1.setGeometry(QtCore.QRect(20, 90, 390, 161))
        self.widget_setting_1.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_setting_1.setObjectName("widget_setting_1")
        self.password_ch_input = QtWidgets.QLineEdit(self.widget_setting_1)
        self.password_ch_input.setGeometry(QtCore.QRect(10, 60, 370, 45))
        self.password_ch_input.setMinimumSize(QtCore.QSize(200, 40))
        self.password_ch_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.password_ch_input.setFont(font)
        self.password_ch_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.password_ch_input.setText("")
        self.password_ch_input.setMaxLength(100)
        self.password_ch_input.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_ch_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_ch_input.setDragEnabled(False)
        self.password_ch_input.setReadOnly(False)
        self.password_ch_input.setObjectName("password_ch_input")
        self.username_ch_input = QtWidgets.QLineEdit(self.widget_setting_1)
        self.username_ch_input.setGeometry(QtCore.QRect(10, 10, 370, 45))
        self.username_ch_input.setMinimumSize(QtCore.QSize(200, 40))
        self.username_ch_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.username_ch_input.setFont(font)
        self.username_ch_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.username_ch_input.setText("")
        self.username_ch_input.setMaxLength(100)
        self.username_ch_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_ch_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username_ch_input.setDragEnabled(False)
        self.username_ch_input.setReadOnly(False)
        self.username_ch_input.setObjectName("username_ch_input")
        self.btn_save_change_username_password = QtWidgets.QPushButton(self.widget_setting_1)
        self.btn_save_change_username_password.setGeometry(QtCore.QRect(10, 110, 370, 40))
        self.btn_save_change_username_password.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_save_change_username_password.setFont(font)
        self.btn_save_change_username_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_change_username_password.setStyleSheet("QPushButton{\n"
"    background-color: #3a31d8;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0600c2;\n"
"border-radius:10px;\n"
"}")
        self.btn_save_change_username_password.setIconSize(QtCore.QSize(30, 30))
        self.btn_save_change_username_password.setObjectName("btn_save_change_username_password")
        self.label_setting_title = QtWidgets.QLabel(self.widget_more)
        self.label_setting_title.setGeometry(QtCore.QRect(30, 60, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_setting_title.setFont(font)
        self.label_setting_title.setStyleSheet("color: #f2f2f2;border: none;")
        self.label_setting_title.setObjectName("label_setting_title")
        self.label_app_v_title = QtWidgets.QLabel(self.widget_more)
        self.label_app_v_title.setGeometry(QtCore.QRect(30, 540, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_app_v_title.setFont(font)
        self.label_app_v_title.setStyleSheet("color: #f2f2f2;border: none;")
        self.label_app_v_title.setObjectName("label_app_v_title")
        self.widget_app_v_1 = QtWidgets.QWidget(self.widget_more)
        self.widget_app_v_1.setGeometry(QtCore.QRect(20, 570, 390, 50))
        self.widget_app_v_1.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_app_v_1.setObjectName("widget_app_v_1")
        self.label_app_v_2 = QtWidgets.QLabel(self.widget_app_v_1)
        self.label_app_v_2.setGeometry(QtCore.QRect(20, 12, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_app_v_2.setFont(font)
        self.label_app_v_2.setStyleSheet("color: #f2f2f2;border: none;")
        self.label_app_v_2.setObjectName("label_app_v_2")
        self.widget_setting_2 = QtWidgets.QWidget(self.widget_more)
        self.widget_setting_2.setGeometry(QtCore.QRect(20, 260, 390, 161))
        self.widget_setting_2.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_setting_2.setObjectName("widget_setting_2")
        self.port_ch_input = QtWidgets.QLineEdit(self.widget_setting_2)
        self.port_ch_input.setGeometry(QtCore.QRect(10, 60, 370, 45))
        self.port_ch_input.setMinimumSize(QtCore.QSize(200, 40))
        self.port_ch_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.port_ch_input.setFont(font)
        self.port_ch_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.port_ch_input.setMaxLength(100)
        self.port_ch_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.port_ch_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.port_ch_input.setDragEnabled(False)
        self.port_ch_input.setReadOnly(False)
        self.port_ch_input.setObjectName("port_ch_input")
        self.ip_ch_input = QtWidgets.QLineEdit(self.widget_setting_2)
        self.ip_ch_input.setGeometry(QtCore.QRect(10, 10, 370, 45))
        self.ip_ch_input.setMinimumSize(QtCore.QSize(200, 40))
        self.ip_ch_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.ip_ch_input.setFont(font)
        self.ip_ch_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.ip_ch_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ip_ch_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ip_ch_input.setDragEnabled(False)
        self.ip_ch_input.setReadOnly(False)
        self.ip_ch_input.setObjectName("ip_ch_input")
        self.btn_save_change_ip_port = QtWidgets.QPushButton(self.widget_setting_2)
        self.btn_save_change_ip_port.setGeometry(QtCore.QRect(10, 110, 370, 40))
        self.btn_save_change_ip_port.setMinimumSize(QtCore.QSize(370, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_save_change_ip_port.setFont(font)
        self.btn_save_change_ip_port.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_change_ip_port.setStyleSheet("QPushButton{\n"
"    background-color: #3a31d8;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0600c2;\n"
"border-radius:10px;\n"
"}")
        self.btn_save_change_ip_port.setIconSize(QtCore.QSize(30, 30))
        self.btn_save_change_ip_port.setObjectName("btn_save_change_ip_port")
        self.widget_setting_3 = QtWidgets.QWidget(self.widget_more)
        self.widget_setting_3.setGeometry(QtCore.QRect(20, 430, 391, 105))
        self.widget_setting_3.setMinimumSize(QtCore.QSize(0, 105))
        self.widget_setting_3.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_setting_3.setObjectName("widget_setting_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_setting_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_options_sec_1 = QtWidgets.QWidget(self.widget_setting_3)
        self.widget_options_sec_1.setMinimumSize(QtCore.QSize(0, 45))
        self.widget_options_sec_1.setObjectName("widget_options_sec_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_options_sec_1)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_auto_open_browser = QtWidgets.QCheckBox(self.widget_options_sec_1)
        self.checkBox_auto_open_browser.setMinimumSize(QtCore.QSize(40, 35))
        self.checkBox_auto_open_browser.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.checkBox_auto_open_browser.setFont(font)
        self.checkBox_auto_open_browser.setStyleSheet("QCheckBox {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    width: 45px;\n"
"    height: 45px;\n"
"    image: url(:/img/img/toggle-on-light.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    width: 45px;\n"
"    height: 45px;\n"
"    image: url(:/img/img/toggle-off-light.png);\n"
"}color: #ebe9fc;")
        self.checkBox_auto_open_browser.setText("")
        self.checkBox_auto_open_browser.setChecked(True)
        self.checkBox_auto_open_browser.setObjectName("checkBox_auto_open_browser")
        self.horizontalLayout_3.addWidget(self.checkBox_auto_open_browser)
        self.label_option_text_1 = QtWidgets.QLabel(self.widget_options_sec_1)
        self.label_option_text_1.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_option_text_1.setFont(font)
        self.label_option_text_1.setStyleSheet("background-color: none;color: #ebe9fc;border: none;")
        self.label_option_text_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_option_text_1.setObjectName("label_option_text_1")
        self.horizontalLayout_3.addWidget(self.label_option_text_1)
        self.verticalLayout.addWidget(self.widget_options_sec_1)
        self.widget_options_sec_2 = QtWidgets.QWidget(self.widget_setting_3)
        self.widget_options_sec_2.setMinimumSize(QtCore.QSize(0, 45))
        self.widget_options_sec_2.setObjectName("widget_options_sec_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_options_sec_2)
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_cache_logging = QtWidgets.QCheckBox(self.widget_options_sec_2)
        self.checkBox_cache_logging.setMinimumSize(QtCore.QSize(45, 35))
        self.checkBox_cache_logging.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.checkBox_cache_logging.setFont(font)
        self.checkBox_cache_logging.setStyleSheet("QCheckBox {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    width: 45px;\n"
"    height: 45px;\n"
"    image: url(:/img/img/toggle-on-light.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    width: 45px;\n"
"    height: 45px;\n"
"    image: url(:/img/img/toggle-off-light.png);\n"
"}color: #ebe9fc;")
        self.checkBox_cache_logging.setText("")
        self.checkBox_cache_logging.setChecked(True)
        self.checkBox_cache_logging.setObjectName("checkBox_cache_logging")
        self.horizontalLayout_4.addWidget(self.checkBox_cache_logging)
        self.label_option_text_2 = QtWidgets.QLabel(self.widget_options_sec_2)
        self.label_option_text_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_option_text_2.setFont(font)
        self.label_option_text_2.setStyleSheet("background-color: none;color: #ebe9fc;border: none;")
        self.label_option_text_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_option_text_2.setObjectName("label_option_text_2")
        self.horizontalLayout_4.addWidget(self.label_option_text_2)
        self.verticalLayout.addWidget(self.widget_options_sec_2)
        self.widget_home = QtWidgets.QWidget(self.widget)
        self.widget_home.setGeometry(QtCore.QRect(0, 0, 430, 640))
        self.widget_home.setStyleSheet("QWidget{\n"
"    background-color: #212121;\n"
"    border-bottom-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget_home.setObjectName("widget_home")
        self.widget_option_1 = QtWidgets.QWidget(self.widget_home)
        self.widget_option_1.setGeometry(QtCore.QRect(20, 60, 390, 181))
        self.widget_option_1.setStyleSheet("border: 2px solid #424242;\n"
"border-radius:16px;\n"
"background-color: #212121;")
        self.widget_option_1.setObjectName("widget_option_1")
        self.ip_v_input = QtWidgets.QLineEdit(self.widget_option_1)
        self.ip_v_input.setGeometry(QtCore.QRect(10, 10, 370, 50))
        self.ip_v_input.setMinimumSize(QtCore.QSize(200, 40))
        self.ip_v_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.ip_v_input.setFont(font)
        self.ip_v_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.ip_v_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ip_v_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ip_v_input.setDragEnabled(False)
        self.ip_v_input.setReadOnly(True)
        self.ip_v_input.setObjectName("ip_v_input")
        self.port_v_input = QtWidgets.QLineEdit(self.widget_option_1)
        self.port_v_input.setGeometry(QtCore.QRect(10, 70, 370, 50))
        self.port_v_input.setMinimumSize(QtCore.QSize(200, 40))
        self.port_v_input.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.port_v_input.setFont(font)
        self.port_v_input.setStyleSheet("QLineEdit{\n"
"    background-color: #222324;\n"
"    border-top-right-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"    color: #ebe9fc;\n"
"    text-align: right;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}")
        self.port_v_input.setMaxLength(100)
        self.port_v_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.port_v_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.port_v_input.setDragEnabled(False)
        self.port_v_input.setReadOnly(True)
        self.port_v_input.setObjectName("port_v_input")
        self.btn_open_browser = QtWidgets.QPushButton(self.widget_option_1)
        self.btn_open_browser.setGeometry(QtCore.QRect(10, 130, 370, 40))
        self.btn_open_browser.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_open_browser.setFont(font)
        self.btn_open_browser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open_browser.setStyleSheet("QPushButton{\n"
"    background-color: #3a31d8;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0600c2;\n"
"border-radius:10px;\n"
"}")
        self.btn_open_browser.setIconSize(QtCore.QSize(30, 30))
        self.btn_open_browser.setObjectName("btn_open_browser")
        self.widget_option_2 = QtWidgets.QWidget(self.widget_home)
        self.widget_option_2.setGeometry(QtCore.QRect(10, 570, 410, 60))
        self.widget_option_2.setStyleSheet("border: 2px solid #424242;\n"
"border-radius:16px;\n"
"background-color: #212121;")
        self.widget_option_2.setObjectName("widget_option_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_option_2)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn_active_inactive = QtWidgets.QPushButton(self.widget_option_2)
        self.Btn_active_inactive.setMinimumSize(QtCore.QSize(120, 40))
        self.Btn_active_inactive.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_active_inactive.setFont(font)
        self.Btn_active_inactive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_active_inactive.setStyleSheet("QPushButton{\n"
"    background-color: #433bff;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #2f27ce;\n"
"border-radius:10px;\n"
"}")
        self.Btn_active_inactive.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/img/img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Btn_active_inactive.setIcon(icon1)
        self.Btn_active_inactive.setIconSize(QtCore.QSize(25, 25))
        self.Btn_active_inactive.setCheckable(True)
        self.Btn_active_inactive.setObjectName("Btn_active_inactive")
        self.gridLayout.addWidget(self.Btn_active_inactive, 0, 1, 1, 1)
        self.label_stats = QtWidgets.QLabel(self.widget_option_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_stats.setFont(font)
        self.label_stats.setStyleSheet("background-color: none;color: #ebe9fc;border: none;")
        self.label_stats.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_stats.setObjectName("label_stats")
        self.gridLayout.addWidget(self.label_stats, 0, 0, 1, 1)
        self.widget_nav_background = QtWidgets.QWidget(self.widget)
        self.widget_nav_background.setGeometry(QtCore.QRect(0, 0, 430, 640))
        self.widget_nav_background.setStyleSheet("QWidget{\n"
"    background-color: rgb(33, 33, 33, 180);\n"
"    border-bottom-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget_nav_background.setObjectName("widget_nav_background")
        self.widget_nav_menu = QtWidgets.QWidget(self.widget_nav_background)
        self.widget_nav_menu.setGeometry(QtCore.QRect(0, 0, 240, 640))
        self.widget_nav_menu.setStyleSheet("QWidget{\n"
"    background-color: #252525;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget_nav_menu.setObjectName("widget_nav_menu")
        self.widget_nav_header = QtWidgets.QWidget(self.widget_nav_menu)
        self.widget_nav_header.setGeometry(QtCore.QRect(10, 10, 220, 70))
        self.widget_nav_header.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_nav_header.setObjectName("widget_nav_header")
        self.label_icon_nav_one = QtWidgets.QLabel(self.widget_nav_header)
        self.label_icon_nav_one.setGeometry(QtCore.QRect(10, 10, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_icon_nav_one.setFont(font)
        self.label_icon_nav_one.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_icon_nav_one.setText("")
        self.label_icon_nav_one.setPixmap(QtGui.QPixmap(":/img/img/nebula-RF-logo.png"))
        self.label_icon_nav_one.setScaledContents(True)
        self.label_icon_nav_one.setObjectName("label_icon_nav_one")
        self.label_title_nav = QtWidgets.QLabel(self.widget_nav_header)
        self.label_title_nav.setGeometry(QtCore.QRect(70, 9, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_title_nav.setFont(font)
        self.label_title_nav.setStyleSheet("color: #ebe9fc;")
        self.label_title_nav.setObjectName("label_title_nav")
        self.label_pcname = QtWidgets.QLabel(self.widget_nav_header)
        self.label_pcname.setGeometry(QtCore.QRect(70, 35, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_pcname.setFont(font)
        self.label_pcname.setStyleSheet("color: #ebe9fc;")
        self.label_pcname.setObjectName("label_pcname")
        self.btn_home = QtWidgets.QPushButton(self.widget_nav_menu)
        self.btn_home.setGeometry(QtCore.QRect(10, 90, 220, 45))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setStyleSheet("QPushButton{\n"
"    background-color: #303030;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    text-align: left;\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #353535;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color:#404040;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/home-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QtCore.QSize(25, 25))
        self.btn_home.setCheckable(True)
        self.btn_home.setObjectName("btn_home")
        self.btn_more = QtWidgets.QPushButton(self.widget_nav_menu)
        self.btn_more.setGeometry(QtCore.QRect(10, 145, 220, 45))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_more.setStyleSheet("QPushButton{\n"
"    background-color: #303030;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    text-align: left;\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #353535;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color:#404040;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/more-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_more.setIcon(icon3)
        self.btn_more.setIconSize(QtCore.QSize(25, 25))
        self.btn_more.setCheckable(True)
        self.btn_more.setObjectName("btn_more")
        self.widget_my_about = QtWidgets.QWidget(self.widget_nav_menu)
        self.widget_my_about.setGeometry(QtCore.QRect(10, 560, 220, 70))
        self.widget_my_about.setMinimumSize(QtCore.QSize(220, 70))
        self.widget_my_about.setStyleSheet("QWidget{\n"
"    background-color: #303030;\n"
"    border-radius: 13px;\n"
"}")
        self.widget_my_about.setObjectName("widget_my_about")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_my_about)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_my_name = QtWidgets.QLabel(self.widget_my_about)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_my_name.setFont(font)
        self.label_my_name.setStyleSheet("color: #ebe9fc;")
        self.label_my_name.setObjectName("label_my_name")
        self.horizontalLayout_5.addWidget(self.label_my_name)
        self.btn_my_github = QtWidgets.QPushButton(self.widget_my_about)
        self.btn_my_github.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_my_github.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_my_github.setFont(font)
        self.btn_my_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_my_github.setStyleSheet("QPushButton{\n"
"    background-color: #353535;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #404040;\n"
"border-radius:10px;\n"
"}")
        self.btn_my_github.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_my_github.setIcon(icon4)
        self.btn_my_github.setIconSize(QtCore.QSize(30, 30))
        self.btn_my_github.setObjectName("btn_my_github")
        self.horizontalLayout_5.addWidget(self.btn_my_github)
        self.btn_close_nav_menu = QtWidgets.QPushButton(self.widget_nav_background)
        self.btn_close_nav_menu.setGeometry(QtCore.QRect(250, 10, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_close_nav_menu.setFont(font)
        self.btn_close_nav_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close_nav_menu.setStyleSheet("QPushButton{\n"
"    background-color: #2f2f2f;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #424242;\n"
"border-radius:10px;\n"
"}")
        self.btn_close_nav_menu.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close_nav_menu.setIcon(icon5)
        self.btn_close_nav_menu.setIconSize(QtCore.QSize(30, 30))
        self.btn_close_nav_menu.setObjectName("btn_close_nav_menu")
        self.widget_error_message = QtWidgets.QWidget(self.widget)
        self.widget_error_message.setGeometry(QtCore.QRect(10, 570, 410, 50))
        self.widget_error_message.setMinimumSize(QtCore.QSize(300, 50))
        self.widget_error_message.setStyleSheet("QWidget{\n"
"    background-color: #f8d7da;\n"
"    border-radius: 13px;\n"
"    border: 2px solid #f5c6cb;\n"
"}")
        self.widget_error_message.setObjectName("widget_error_message")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_error_message)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_text_e_message = QtWidgets.QLabel(self.widget_error_message)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_text_e_message.setFont(font)
        self.label_text_e_message.setStyleSheet("background-color: none;color: #721c24;border: none;")
        self.label_text_e_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_e_message.setObjectName("label_text_e_message")
        self.horizontalLayout_2.addWidget(self.label_text_e_message)
        self.widget_success_message = QtWidgets.QWidget(self.widget)
        self.widget_success_message.setGeometry(QtCore.QRect(10, 570, 410, 50))
        self.widget_success_message.setMinimumSize(QtCore.QSize(400, 50))
        self.widget_success_message.setStyleSheet("QWidget{\n"
"    background-color: #d4edda;\n"
"    border-radius: 13px;\n"
"    border: 2px solid #c3e6cb;\n"
"}")
        self.widget_success_message.setObjectName("widget_success_message")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_success_message)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text_s_message = QtWidgets.QLabel(self.widget_success_message)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_text_s_message.setFont(font)
        self.label_text_s_message.setStyleSheet("background-color: none;color: #155724;border: none;")
        self.label_text_s_message.setTextFormat(QtCore.Qt.AutoText)
        self.label_text_s_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_s_message.setObjectName("label_text_s_message")
        self.horizontalLayout.addWidget(self.label_text_s_message)
        self.widget_more.raise_()
        self.widget_home.raise_()
        self.btn_open_nav_menu.raise_()
        self.widget_nav_background.raise_()
        self.widget_error_message.raise_()
        self.widget_success_message.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_minimized.setText(_translate("MainWindow", "–"))
        self.Button_exit.setText(_translate("MainWindow", "×"))
        self.label_title.setText(_translate("MainWindow", "Nebula Remote Fusion"))
        self.password_ch_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.username_ch_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.btn_save_change_username_password.setText(_translate("MainWindow", "Save change"))
        self.label_setting_title.setText(_translate("MainWindow", "Setting"))
        self.label_app_v_title.setText(_translate("MainWindow", "App Version"))
        self.label_app_v_2.setText(_translate("MainWindow", "V1.0.0"))
        self.port_ch_input.setText(_translate("MainWindow", "8080"))
        self.port_ch_input.setPlaceholderText(_translate("MainWindow", "port"))
        self.ip_ch_input.setText(_translate("MainWindow", "192.0.0.1"))
        self.ip_ch_input.setPlaceholderText(_translate("MainWindow", "ip address"))
        self.btn_save_change_ip_port.setText(_translate("MainWindow", "Save change"))
        self.label_option_text_1.setText(_translate("MainWindow", "Automatic opening of the browser"))
        self.label_option_text_2.setText(_translate("MainWindow", "Cache when Logging in"))
        self.ip_v_input.setText(_translate("MainWindow", "192.0.0.1"))
        self.ip_v_input.setPlaceholderText(_translate("MainWindow", "ip address"))
        self.port_v_input.setText(_translate("MainWindow", "8080"))
        self.port_v_input.setPlaceholderText(_translate("MainWindow", "port"))
        self.btn_open_browser.setText(_translate("MainWindow", "Open Browser"))
        self.label_stats.setText(_translate("MainWindow", "Inactive"))
        self.label_title_nav.setText(_translate("MainWindow", "NRF"))
        self.label_pcname.setText(_translate("MainWindow", "Mahdi Zafari"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_more.setText(_translate("MainWindow", "More"))
        self.label_my_name.setText(_translate("MainWindow", "By Mahdi Zafari"))
        self.label_text_e_message.setText(_translate("MainWindow", "{Message}"))
        self.label_text_s_message.setText(_translate("MainWindow", "{Message}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
