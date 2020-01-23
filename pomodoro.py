import time
def mins_secs(seconds):
        mins=seconds//60
        secs=0
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        return [mins,secs]
            

