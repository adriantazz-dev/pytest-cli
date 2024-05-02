import pytest
import logging

# Define a fixture that expects parameters
@pytest.fixture
def setup(request):
    parameter = request.param
    logging.info(f"Setting up with parameter: {parameter}")
    return parameter