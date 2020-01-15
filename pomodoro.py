import time
from sys import argv
def time(time1):
    list_mins_secs=[]
    time1=time1*60
    for t in range(time1,0,-1):
        mins,secs = divmod(t, 60)
        if secs ==0:
            list_mins_secs.append([mins,secs])
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')  
        #time.sleep(1)
    return list_mins_secs
print(time(10))







































