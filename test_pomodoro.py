from pomodoro import pomodoro,display

def test_get_time():
    time1=10
    assert pomodoro(time1) == [0, 10]

def test_work_25_reminder():
    start=30*60
    mins=30
    secs=0
    assert display(start,mins,secs) == "Work! 25 minutes"
    

    
