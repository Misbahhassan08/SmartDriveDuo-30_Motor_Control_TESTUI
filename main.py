import sys
import threading
from motor import Motor
from mdds30_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class UI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)
        pass    # end of ui constructor
    pass   # end of UI class

class Main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ui = UI()
        self.motor = Motor()
        self.initialize()
        self.ui.showMaximized()
        self.buttons_function()
        pass   # end of Main class constructor
    def initialize(self):
        pass   # end of initialize function
    def buttons_function(self):
        self.ui.left_forward_button.clicked.connect(self.left_motor_cw)
        self.ui.left_reverse_button.clicked.connect(self.left_motor_ccw)
        self.ui.right_forward_button.clicked.connect(self.right_motor_cw)
        self.ui.right_reverse_button.clicked.connect(self.right_motor_ccw)
        self.ui.left_motor_stop.clicked.connect(self.left_motor_stop)
        self.ui.right_motor_stop.clicked.connect(self.right_motor_stop)
        
        pass   # end of buttons_function
    def left_motor_cw(self):
        speed = self.ui.left_motor_slider.value()
        self.motor.left_cw(speed)  # set dutycycle 0-100
        self.ui.left_speed_label.setText(f"Speed : {speed}")
        pass   # end of left_motor_cw
    def left_motor_ccw(self):
        speed = self.ui.left_motor_slider.value()
        self.motor.left_ccw(speed)  # set dutycycle 0-100
        self.ui.left_speed_label.setText(f"Speed : {speed}")
        pass   # end of left_motor_ccw
    
    def right_motor_cw(self):
        speed = self.ui.right_motor_slider.value()
        self.motor.right_cw(speed)  # set dutycycle 0-100
        self.ui.right_speed_label.setText(f"Speed : {speed}")
        pass   # end of right_motor_cw
    def right_motor_ccw(self):
        speed = self.ui.right_motor_slider.value()
        self.motor.right_ccw(speed)  # set dutycycle 0-100
        self.ui.right_speed_label.setText(f"Speed : {speed}")
        pass   # end of right_motor_ccw
    
    def left_motor_stop(self):
        self.motor.left_cw(0)  # stop motor
        self.ui.left_speed_label.setText("Speed : Stop")
        pass   # end of left motor stop
    def right_motor_stop(self):
        self.motor.right_cw(0)  # stop motor
        self.ui.right_speed_label.setText("Speed : Stop")
        pass   # end of right motor stop
    pass   # end of main class

def _main():
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.start()
    sys.exit(app.exec_())
    
    pass   # end of _main function
if __name__ == "__main__":
    _main()
    pass   # end of  __main__