PyTest is pretty interesting testing framework
to get this working for the whole directory the tests have to be named in a following way: 'test_*', otherwise the test would not be found


PS D:\Project\TrainingPython\pytest> py.test .
==================================================================================================== test session starts ======================================================================================================
platform win32 -- Python 3.9.0, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: D:\Project\TrainingPython\pytest
collected 5 items

test_1.py .                                                                                                                                                                                                               [ 20%] 
test_2.py ....                                                                                                                                                                                                            [100%] 
