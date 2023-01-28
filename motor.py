import pigpio

class Motor:
    pi = pigpio.pi()
    def __init__(self,dutycycle):  # dutycycle set from 0-100
        self.initialize()
        self.dutycycle = dutycycle
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
    def left_cw(self):  # left motor clock wise
        self.pi.write(self.IN1,self.dir_cw)
        self.pi.hardware_PWM(self.pwm_pin_left, self.freq, self.dutycycle*10000)
        pass   # end of forward motor left_cw function
    def left_ccw(self):  # left motor counter clock wise
        self.pi.write(self.IN1,self.dir_ccw)
        self.pi.hardware_PWM(self.pwm_pin_left, self.freq, self.dutycycle*10000)
        pass   # end of forward motor left_ccw function
    def right_cw(self):  # left motor clock wise
        self.pi.write(self.IN2,self.dir_cw)
        self.pi.hardware_PWM(self.pwm_pin_right, self.freq, self.dutycycle*10000)
        pass   # end of forward motor right_cw function
    def right_ccw(self):  # left motor counter clock wise
        self.pi.write(self.IN2,self.dir_ccw)
        self.pi.hardware_PWM(self.pwm_pin_right, self.freq, self.dutycycle*10000)
        pass   # end of forward motor function
    
if __name__ == "__main__":
    motor = Motor(50)
    motor.left_cw()
    motor.left_ccw()
    motor.right_cw()
    motor.right_ccw()
    print("cheking")
    