import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

class mover:
    freq = 60
    pwm.set_freq(freq)
    total = 4096#Total number of bits
    def __init__(self):
        pass
    def bit_low(percent):#Taken as a percent decimal
        return percent * total
    def bit_high(percent):
        return (total - (total * percent))
    def drive(motor,percent):
        pwm.set_pwm(motor,self.bit_low(percent),self.bit_high(percent))

def mapping(val,min_i,max_i,min_o,max_o):
    del_i = max_i - min_i
    del_o = max_o - min_o
    return (val - min_i) / del_i
