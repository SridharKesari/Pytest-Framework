import pytest


@pytest.mark.parametrize('test_input', [82, 78, 45, 66])
def test_param01(test_input):  # specify parameter name as a parameter to the test function
    assert test_input > 50
