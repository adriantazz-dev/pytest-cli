import pytest

# Optional teardown fixture example
@pytest.fixture
def resource():
    context = {'cleanup_needed': True}
    print("Setting up resource")
    yield context
    if context['cleanup_needed']:
        print("Performing cleanup")
    else:
        print("Skipping cleanup")
