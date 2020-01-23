from pomodoro import mins_secs

def test_get_mins_and_secs():
    seconds=25*60
    assert mins_secs(seconds) == [25, 0]



