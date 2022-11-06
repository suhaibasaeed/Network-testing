import json
from rich import print
from genie.testbed import load
from pyats.async_ import pcall

def get_ospf(device_name, testbed_value):
    # Call sh ip ospf nei command on device object and parse
    routing_table = testbed_value.parse("show ip route")
    pretty_ospf = json.dumps(routing_table, indent=2)
    print(f"{device_name}\n{pretty_ospf}")
    return routing_table

# Load testbed and connect to devices
testbed = load("testbed.yaml")
testbed.connect(log_stdout=False)
# Call pcall to run function passing in testbed device names and objs - We're returned tuple with 3 elements
results = pcall(get_ospf, device_name=testbed.devices.keys(),testbed_value=testbed.devices.values())
#from ipdb import set_trace; set_trace()