import time
from sys import argv
def pomodoro(time1):
    list_mins_secs=[]
    mins,secs = divmod(time1, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\n')
    #time.sleep(1)
    return [mins,secs]

if __name__== "__main__":
    for t in range(30*60,0,-1):
       clock=pomodoro(t)
       if clock[0] == 30:
           print("Work! 25 minutes")
       elif clock[0] == 15 and clock[1] == 0:
           print("10 minutes left")
       elif clock[0]==5 and clock[1]==1:
           print("TimeUp")
       elif clock[0]==5 and clock[1]==0:
           print("Rest! 5 minutes")
       elif clock[0]==0 and clock[1]==1:
           print("Time up!")





































