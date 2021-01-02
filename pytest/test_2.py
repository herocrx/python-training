# content of test_sample.py
def func(x):
    return x + 1

class TestClass:

    def test_answer(self):
        assert func(4) == 5
        assert func(5) == 6
        assert func(6) == 7


    def test_answer1(self):    
        assert func(7) == 8
        assert func(8) == 9

    def test_answer2(self):    
        assert func(7) == 8
        assert func(80) == 81

    def test_answer3(self):    
        assert func(7) == 8
        #assert func(80) != 81
        assert func(80) == 81
        print('Executed!')

# On failure without test
#PS D:\Project\TrainingPython\pytest> py .\secondTest.py
#Traceback (most recent call last):
#  File "D:\Project\TrainingPython\pytest\secondTest.py", line 28, in <module>
#    instance.test_answer3()
#  File "D:\Project\TrainingPython\pytest\secondTest.py", line 23, in test_answer3
#    assert func(80) != 81
#AssertionError

instance = TestClass()
instance.test_answer3()