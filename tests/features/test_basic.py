import pytest
import logging

from tests.fixtures.factory_example_fixture import db_connection_factory
from tests.fixtures.indirect_param_fixture import setup

@pytest.mark.smoke
def test_basic():
    assert pytest.username == "test_username"

@pytest.mark.regression
def test_basic2():
    assert 2 == 2

# Test using the factory
@pytest.mark.smoke
def test_database_operations(db_connection_factory):
    # Set up a connection for Test Database as admin
    db_conn = db_connection_factory("Test Database", "admin")
    next(db_conn)  # Proceed to yield the connection
    # Simulate test using the connection
    assert "Test Database" in db_conn and "admin" in db_conn
    logging.info(f"Testing operations with {db_conn}")

# Use pytest.mark.parametrize to send parameters indirectly to the fixture
@pytest.mark.parametrize("setup", ["Hello", "World"], indirect=True)
def test_greet(setup):
    assert setup in ["Hello", "World"]
    logging.info(f"Greeting {setup}!")

# Additional test to demonstrate different parameters
@pytest.mark.parametrize("setup", [1, 2, 3], indirect=True)
def test_numbers(setup):
    assert setup in [1, 2, 3]
    logging.info(f"Number is {setup}")