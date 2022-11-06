from nornir_scrapli.tasks import send_command
import pytest
from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir(config_file='config.yaml')

def check_ospf_neighbours_get_data(task):

    result = task.run(task=send_command, command='show ip ospf neighbors')
    # Take result and return structured data - then store in host object
    task.host["ospf_neighbour_data"] = result.scrapli_response.textfsm_parse_output()

# Use another instance of nornir to get device names from inventory - different from pytestnr instance
def get_nxos_device_names():
    devices = nr.filter(F(groups__contains='nxos'))
    # Get device names only - for parametise to loop through
    devices = devices.inventory.hosts.keys()
    return devices

# Good to group multiple tests together under a class
class TestOSPFNeigbours:
    # pytestnr is fixture from conftest file
    @pytest.fixture(scope='class', autouse=True)
    def setup_teardown(self, pytestnr):
        pytestnrfiltered = pytestnr.filter(F(groups__contains='nxos'))
        pytestnrfiltered.run(task=check_ospf_neighbours_get_data)
        yield
        for host in pytestnrfiltered.inventory.hosts.values():
            # Remove key from all host obj after test completed - essentially clean up
            host.data.pop("ospf_neighbour_data")

    # Use parameterise so we can get results back for each device - iterates over devices
    @pytest.mark.parametrize("device_name", get_nxos_device_names())
    def test_ospf_neighbour_count(self, pytestnr, device_name):
        ospf_neighbours = []
        # Get the host name of the device
        nr_host = pytestnr.inventory.hosts[device_name]
        interfaces = nr_host["ospf_neighbour_data"]
        # # Loop through returned structured data then append neighbours RID to list
        for i in interfaces:
            ospf_neighbours.append(i['neighbor_ipaddr'])

        num_neighbours = len(ospf_neighbours)

        assert num_neighbours == 2, f"{device_name} does not has 2 neighbors"

