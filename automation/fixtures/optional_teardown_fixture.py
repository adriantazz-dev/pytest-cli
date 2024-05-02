import pytest
import logging

# Optional teardown fixture example
@pytest.fixture
def resource():
    context = {'cleanup_needed': True}
    logging.info("Setting up resource")
    yield context
    if context['cleanup_needed']:
        logging.info("Performing cleanup")
    else:
        logging.info("Skipping cleanup")
