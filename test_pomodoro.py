from pomodoro import countdown,work,rest

def test_count_time():
    time1=10
    assert countdown(time1) ==  [['00', '10'], ['00', '09'], ['00', '08'], ['00', '07'], ['00', '06'], ['00', '05'], ['00', '04'], ['00', '03'], ['00', '02'], ['00', '01']]
    
def test_work_25_minutes():
    time1=10
    assert work(time1) == "Work! 25 minutes"

def test_work_10_minutes():
    time1=5
    assert work(time1) == "10 minutes left"

def test_rest_time():
    time2=5
    assert rest(time2) == "Rest! 5 minutes"
    

