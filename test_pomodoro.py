from pomodoro import mins_secs,work

def test_get_mins_and_secs():
    seconds=25*60
    assert mins_secs(seconds) == [25, 0]
def test_work_print_ten_mins():
    seconds=10*60
    assert work(seconds) == "10 minutes left"


