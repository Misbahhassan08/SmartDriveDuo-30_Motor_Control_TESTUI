import pigpio

class Motor:
    pi = pigpio.pi()
    def __init__(self):  # dutycycle set from 0-100
        self.initialize()
        self.pi.set_mode(self.IN1, pigpio.OUTPUT)  # set mode IN1
        self.pi.set_mode(self.IN2, pigpio.OUTPUT)  # set mode IN2
        pass   # end of motor constructor
    def initialize(self):
        self.IN1 = 5   # left motor direction pin 5
        self.IN2 = 6   # right motor direction pin 6
        self.dir_cw = 0  #  set direction for clock wise
        self.dir_ccw = 1  # set direction for counter clock wise
        self.pwm_pin_left = 12  # pwm_pin_left motor with PWM0
        self.pwm_pin_right = 13  # pwm_pin_right motor with PWM1
        self.freq = 800  #    set frequency 800Hz by default
        pass   #   end of initialize function
    def left_cw(self,dutycycle):  # left motor clock wise and duty cycle set from 0-100
        self.pi.write(self.IN1,self.dir_cw)
        self.pi.hardware_PWM(self.pwm_pin_left, self.freq, dutycycle*10000)
        pass   # end of forward motor left_cw function
    def left_ccw(self,dutycycle):  # left motor counter clock wise and duty cycle set from 0-100
        self.pi.write(self.IN1,self.dir_ccw)
        self.pi.hardware_PWM(self.pwm_pin_left, self.freq, dutycycle*10000)
        pass   # end of forward motor left_ccw function
    def right_cw(self,dutycycle):  # left motor clock wise and duty cycle set from 0-100
        self.pi.write(self.IN2,self.dir_cw)
        self.pi.hardware_PWM(self.pwm_pin_right, self.freq, dutycycle*10000)
        pass   # end of forward motor right_cw function
    def right_ccw(self,dutycycle):  # left motor counter clock wise and duty cycle set from 0-100
        self.pi.write(self.IN2,self.dir_ccw)
        self.pi.hardware_PWM(self.pwm_pin_right, self.freq, dutycycle*10000)
        pass   # end of forward motor function
    
if __name__ == "__main__":
    motor = Motor()
    motor.left_cw(50)  # dutycycle set
    motor.left_ccw(50)  # dutycycle set
    motor.right_cw(50)  # dutycycle set
    motor.right_ccw(50)  # dutycycle set
    print("cheking")
    