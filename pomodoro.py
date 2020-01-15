import time
from sys import argv

def countdown(time1):
    list_time=[]
    list_mins_secs=[]
    for times in [time1]:
        for t in range(times,0,-1):
            mins,secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            #print(timeformat, end='\n')  
            list_time.append(timeformat)
            for i in list_time:
                sub=i.split(':')
            list_mins_secs.append(sub)
            #time.sleep(1)            
    return list_mins_secs

def work(time1):
    times=countdown(time1)
    for i in times:
        mins=int(i[0])
        secs=int(i[1])
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #time.sleep(1)            
        print(timeformat)
        if mins == 0 and secs == 10:
            return "Work! 25 minutes"
        elif mins == 0 and secs == 5:
            return "10 minutes left"
        else:
            return "."

def rest(time1):
    times=countdown(time1)
    for i in times:
        mins=int(i[0])
        secs=int(i[1])
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #time.sleep(1)            
        print(timeformat)
        if mins == 0 and secs == 5:
            return "Rest! 5 minutes"
        else:
            return "."
        
if __name__ == "__main__":
    time1=10
    for i in range(time1,0,-1):
        print(work(i))
    print("TimeUp")
    time2=5
    for i in range(time2,0,-1):
        print(rest(i))
    print("TimeUp")
    

