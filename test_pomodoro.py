from pomodoro import pomodoro

def test_get_time():
    time1=10
    assert pomodoro(time1) == [0, 10]



    
