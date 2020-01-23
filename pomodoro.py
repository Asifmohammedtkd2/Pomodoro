import time
def mins_secs(seconds):
        mins=seconds//60
        secs=0
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        return [mins,secs]
            
def work(seconds):
   if seconds%300==0: 
       five_min=mins_secs(seconds)
       if seconds!=None:
           mins=five_min[0]
           secs=five_min[1]
       if mins==10:
           return "10 minutes left"
       elif mins%5==0:
           return "."
       
def rest(seconds):
    if seconds%60==0:
        one_min=mins_secs(seconds)
        if seconds!=None:
           mins=one_min[0]
           secs=one_min[1]
        if mins%1==0:
            return "."
