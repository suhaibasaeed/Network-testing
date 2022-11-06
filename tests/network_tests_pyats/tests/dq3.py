import json
from rich import print
from genie.testbed import load
from pyats.async_ import pcall
from genie.utils import Dq

def get_ospf_routes(hostname, device):
    routes_parsed =  device.parse('show ip route')
    #print(routes_parsed)
    # Parse dictionary to get routes from OSPF and get route itself - We get list back
    get_routes = Dq(routes_parsed).contains('ospf').get_values('routes')
    num_routes = len(get_routes)
    print(f"{hostname} has {num_routes} OSPF routes in it's routing table")

# Load testbed and connect to devices
testbed = load("testbed.yaml")
testbed.connect(log_stdout=False)
# Call pcall to run function passing in testbed device names and objs - We're returned tuple with 3 elements
results = pcall(get_ospf_routes, hostname=testbed.devices.keys(),device=testbed.devices.values())
#from ipdb import set_trace; set_trace()