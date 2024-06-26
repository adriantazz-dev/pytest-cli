import pytest
import logging

# Fixture factory with yield for setup and teardown
@pytest.fixture
def db_connection_factory():
    connections = []

    def create_connection(database, user):
        # Simulating a database connection setup
        connection = f"Connection to {database} as {user}"
        logging.info(f"Setting up {connection}")
        connections.append(connection)
        yield connection
        # Simulating closing the database connection
        logging.info(f"Tearing down {connection}")

    return create_connection


