from pomodoro import pomodoro,display

def test_get_time():
    time1=10
    assert pomodoro(time1) == [0, 10]

def test_work_25_reminder():
    start=30*60
    mins=30
    secs=0
    assert display(start,mins,secs) == "Work! 25 minutes"

def test_10_minutes_left():
    start=15*60
    mins=15
    secs=0
    assert display(start,mins,secs) == "10 minutes left"
def test_Time_up_display():
    start=6*60
    mins=6
    secs=0
    assert display(start,mins,secs) == 'Time up!'
    
