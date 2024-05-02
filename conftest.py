import pytest
import os
from dotenv import load_dotenv

def pytest_configure(config):
    # Load the .env file
    load_dotenv()

    # Access environment variables
    pytest.username = os.getenv('TEST_USERNAME')
    pytest.password = os.getenv('TEST_PASSWORD')
    pytest.base_url = os.getenv('TEST_BASE_URL')