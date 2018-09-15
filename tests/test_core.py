import easyweb.core
import pytest


class Numbers(object):
    def __init__(self):
        self.n = 0

    def add(self, a):
        self.n += a
        return self.n


def test_classmethods():
    num = Numbers()
    assert easyweb.core.classmethods(num) == ["add"]


def test_classname():
    num = Numbers()
    assert easyweb.core.classname(num) == "Numbers"
