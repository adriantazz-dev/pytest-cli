import pytest

@pytest.mark.smoke
def test_basic():
    assert pytest.username == "test_username"

@pytest.mark.regression
def test_basic2():
    assert 2 == 2