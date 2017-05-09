# -*- coding: utf-8 -*-
from createfile import createrandomfiles
from testkeyword import test

class CustomLibrary(createrandomfiles):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
class CustomLibrary(test):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'