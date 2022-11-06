
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Initalise nornir
nr = InitNornir(config_file="config.yaml")

def pull_ospf(task):

    result = task.run(task=send_command, command='show ip ospf neighbors')
    # Take result and return structured data - then store in host object
    task.host["facts"] = result.scrapli_response.textfsm_parse_output()

    ospf_neighbours = []
    intfs = task.host["facts"]
    # Loop through returned structured data then append neighbours RID to list
    for i in intfs:
        ospf_neighbours.append(i['neighbor_ipaddr'])

results = nr.run(task=pull_ospf)
#import ipdb; ipdb.set_trace()

