import pytest


@pytest.fixture()
def setup_list():   # before running test, setup
    print("\n in fixtures..\n")
    city = ['New York', 'London', 'Bengaluru', 'Washington', 'Hubli']
    return city


def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Bengaluru', 'Hubli']


def myReverse(lst):
    lst.reverse()
    return lst


def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Hubli', 'Bengaluru', 'New York']
    assert setup_list[::-1] == myReverse(setup_list)