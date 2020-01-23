from pomodoro import mins_secs, work, rest
#import pdb; pdb.set_trace()

def test_get_mins_and_secs():
    seconds=25*60
    assert mins_secs(seconds) == [25, 0]
    
def test_work_print_ten_mins():
    seconds=10*60
    assert work(seconds) == "10 minutes left"
    
def test_each_five_min_dot_work():
    seconds=15*60
    assert work(seconds) == "."

def test_each_one_min_dot_rest():
    seconds=1*60
    assert rest(seconds) == "."

