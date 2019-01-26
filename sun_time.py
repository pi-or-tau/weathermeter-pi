
class sun:
    def __init__(self):
        pass
    def text2int(self,current_time):
        previous = 0#Previous ':', 1 after ':'
        case = 0
        for ii in current_time:
            if current_time[ii] == ':' and case == 0:
                self.hour = int(current_time[0:(ii-1)])
                previous = ii+1
                case = 1
            elif current_time[ii] == ':' and case == 1:
                self.minute = int(current_time[previous:(ii-1)])
                previous = ii + 1
                case = 2
            elif current_time[ii] == ':' and case == 2:
                self.second = int(current_time[previous:len(current_time)-1])
            return [self.hour,self.minute,self.second]
    def compare(current_time,sun_time):#Returns True if current_time bigger then sun_time
        if (current_time[0] > sun_time[0]) or (current_time[0] == sun_time[0] and current_time[1] > sun_time[1]) or (current_time[0] == sun_time[0] and current_time[1] == sun_time[1] and current_time[2] > sun_time[2]):
            return True
        else: return False
