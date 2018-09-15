import easyweb.core
from .test_model import Numbers


def test_classmethods():
    num = Numbers()
    assert easyweb.core.classmethods(num) == ["add"]


def test_classname():
    assert easyweb.core.classname(Numbers()) == "Numbers"


def test_modulename():
    assert easyweb.core.modulename(Numbers()) == "tests.test_model"


def test_methods():
    data = easyweb.core.main(Numbers())
    assert data["methods"] == {"add": ["a"]}
