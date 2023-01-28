# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdds30_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:White;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:Black;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_widget = QtWidgets.QWidget(self.centralwidget)
        self.top_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_widget.setStyleSheet("background-color:White;")
        self.top_widget.setObjectName("top_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.top_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.main_heading_label = QtWidgets.QLabel(self.top_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.main_heading_label.setFont(font)
        self.main_heading_label.setStyleSheet("background-color:Black;\n"
"color:White;")
        self.main_heading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_heading_label.setObjectName("main_heading_label")
        self.gridLayout.addWidget(self.main_heading_label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.top_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_widget.setStyleSheet("background-color:White;")
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.bottom_widget)
        self.widget_4.setStyleSheet("background-color:White;")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget_4)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.left_motor_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.left_motor_label.setFont(font)
        self.left_motor_label.setStyleSheet("background-color:black;\n"
"color:White;")
        self.left_motor_label.setLineWidth(1)
        self.left_motor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_motor_label.setObjectName("left_motor_label")
        self.gridLayout_2.addWidget(self.left_motor_label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_4)
        self.frame_2.setStyleSheet("background-color:Black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setStyleSheet("background-color:Black;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_forward_button = QtWidgets.QPushButton(self.frame_7)
        self.left_forward_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.left_forward_button.setFont(font)
        self.left_forward_button.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.left_forward_button.setObjectName("left_forward_button")
        self.horizontalLayout_2.addWidget(self.left_forward_button)
        self.left_reverse_button = QtWidgets.QPushButton(self.frame_7)
        self.left_reverse_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.left_reverse_button.setFont(font)
        self.left_reverse_button.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.left_reverse_button.setObjectName("left_reverse_button")
        self.horizontalLayout_2.addWidget(self.left_reverse_button)
        self.gridLayout_6.addWidget(self.frame_7, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_9.setStyleSheet("background-color:Black;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.left_motor_slider = QtWidgets.QSlider(self.frame_9)
        self.left_motor_slider.setStyleSheet("background-color:White;")
        self.left_motor_slider.setOrientation(QtCore.Qt.Horizontal)
        self.left_motor_slider.setObjectName("left_motor_slider")
        self.gridLayout_7.addWidget(self.left_motor_slider, 0, 0, 1, 1)
        self.left_speed_label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(False)
        self.left_speed_label.setFont(font)
        self.left_speed_label.setStyleSheet("color:white;")
        self.left_speed_label.setObjectName("left_speed_label")
        self.gridLayout_7.addWidget(self.left_speed_label, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_9, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget_4)
        self.frame_3.setStyleSheet("background-color:Black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.left_motor_stop = QtWidgets.QPushButton(self.frame_3)
        self.left_motor_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.left_motor_stop.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.left_motor_stop.setFont(font)
        self.left_motor_stop.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.left_motor_stop.setObjectName("left_motor_stop")
        self.gridLayout_4.addWidget(self.left_motor_stop, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.bottom_widget)
        self.widget_3.setStyleSheet("background-color:White;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.widget_3)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setStyleSheet("background-color:white;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.right_motor_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.right_motor_label.setFont(font)
        self.right_motor_label.setStyleSheet("background-color:black;\n"
"color:White;")
        self.right_motor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_motor_label.setObjectName("right_motor_label")
        self.gridLayout_3.addWidget(self.right_motor_label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.widget_3)
        self.frame_5.setStyleSheet("background-color:Black;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setStyleSheet("background-color:Black;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.right_reverse_button = QtWidgets.QPushButton(self.frame_8)
        self.right_reverse_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.right_reverse_button.setFont(font)
        self.right_reverse_button.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.right_reverse_button.setObjectName("right_reverse_button")
        self.horizontalLayout_3.addWidget(self.right_reverse_button)
        self.right_forward_button = QtWidgets.QPushButton(self.frame_8)
        self.right_forward_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.right_forward_button.setFont(font)
        self.right_forward_button.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.right_forward_button.setObjectName("right_forward_button")
        self.horizontalLayout_3.addWidget(self.right_forward_button)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_10.setStyleSheet("background-color:Black;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.right_motor_slider = QtWidgets.QSlider(self.frame_10)
        self.right_motor_slider.setStyleSheet("background-color:White;")
        self.right_motor_slider.setOrientation(QtCore.Qt.Horizontal)
        self.right_motor_slider.setObjectName("right_motor_slider")
        self.gridLayout_8.addWidget(self.right_motor_slider, 0, 0, 1, 1)
        self.right_speed_label = QtWidgets.QLabel(self.frame_10)
        self.right_speed_label.setStyleSheet("color:White;")
        self.right_speed_label.setObjectName("right_speed_label")
        self.gridLayout_8.addWidget(self.right_speed_label, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.widget_3)
        self.frame_6.setStyleSheet("background-color:Black;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.right_motor_stop = QtWidgets.QPushButton(self.frame_6)
        self.right_motor_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.right_motor_stop.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.right_motor_stop.setFont(font)
        self.right_motor_stop.setStyleSheet("QPushButton{\n"
"border-color: White;\n"
"background-color:#0074a9;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 16px;\n"
"color:Black;\n"
"Font:Bold;\n"
"font-size: 20px\n"
"}\n"
"QPushButton:pressed{ \n"
"   border-color: black;\n"
"background-color:green;\n"
"}\n"
"")
        self.right_motor_stop.setObjectName("right_motor_stop")
        self.gridLayout_5.addWidget(self.right_motor_stop, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.bottom_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_heading_label.setText(_translate("MainWindow", "Motor Control Test"))
        self.left_motor_label.setText(_translate("MainWindow", "Left Motor"))
        self.left_forward_button.setText(_translate("MainWindow", "Forward"))
        self.left_reverse_button.setText(_translate("MainWindow", "Reverse"))
        self.left_speed_label.setText(_translate("MainWindow", "Speed : "))
        self.left_motor_stop.setText(_translate("MainWindow", "Stop"))
        self.right_motor_label.setText(_translate("MainWindow", "Right Motor"))
        self.right_reverse_button.setText(_translate("MainWindow", "Reverse"))
        self.right_forward_button.setText(_translate("MainWindow", "Forward"))
        self.right_speed_label.setText(_translate("MainWindow", "Speed : "))
        self.right_motor_stop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
