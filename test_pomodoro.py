from pomodoro import time

def test_get_time():
    time1=10
    assert time(time1) ==  [[10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]

    
