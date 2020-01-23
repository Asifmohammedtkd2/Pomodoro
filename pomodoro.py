import time
from sys import argv
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
if __name__=="__main__":
   works,rests=25,5
   count=int(argv[1])
   for i in range(count):
       print("Work!",works,"minutes")
       for seconds in range(works*60,0,-1):
           view_work=work(seconds)
           if view_work!=None:
               print(view_work)
       print("TimeUp\n\n\n")
       print("Rest!",rests," minutes")
       for seconds in range(rests*60,0,-1):
           view_rest=rest(seconds)
           if view_rest!=None:
               print(view_rest)
       print("TimeUp")

