import time
from sys import argv
def pomodoro(time1):
    list_mins_secs=[]
    mins,secs = divmod(time1, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\n')
    #time.sleep(1)
    return [mins,secs]

def display(start,mins,secs):
    t=start
    clock=pomodoro(t)
    mins=clock[0]
    secs=clock[1]
    if mins == 30 and secs ==0:
           return "Work! 25 minutes"
   
if __name__== "__main__":
    for t in range(30*60,0,-1):
       dis=display(t,0,0)
       print(dis)





































