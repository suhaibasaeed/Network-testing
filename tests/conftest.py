import pytest
from nornir import InitNornir

# Use fixture for entire session - all tests will use this automatically
@pytest.fixture(scope='session', autouse=True)
def nr():
    # Initalise nornir
    nr = InitNornir(config_file="config.yaml")
    # Return nr object
    yield nr
    # What to do after test - i.e. close connections
    nr.close_connections()