import json
from rich import print
from genie.testbed import load
from pyats.async_ import pcall
from genie.utils import Dq

def get_up_intf(hostname, device):
    intfs_parsed = device.parse('show interface')
    # Parse dictionary to get interfaces that are up and return names
    oper_up = intfs_parsed.q.contains_key_value('oper_status', 'up').get_values('[0]')
    print(oper_up)

# Load testbed and connect to devices
testbed = load("testbed.yaml")
testbed.connect(log_stdout=False)
# Call pcall to run function passing in testbed device names and objs - We're returned tuple with 3 elements
results = pcall(get_up_intf, hostname=testbed.devices.keys(),device=testbed.devices.values())
