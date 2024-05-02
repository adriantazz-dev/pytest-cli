import pytest

# Define a fixture that expects parameters
@pytest.fixture
def setup(request):
    parameter = request.param
    print(f"Setting up with parameter: {parameter}")
    return parameter