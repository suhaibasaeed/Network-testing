from nornir_scrapli.tasks import send_command
from pytest_check import check_func

@check_func
def pull_ospf(task):

    result = task.run(task=send_command, command='show ip ospf neighbors')
    # Take result and return structured data - then store in host object
    task.host["facts"] = result.scrapli_response.textfsm_parse_output()

    ospf_neighbours = []
    intfs = task.host["facts"]
    # Loop through returned structured data then append neighbours RID to list
    for i in intfs:
        ospf_neighbours.append(i['neighbor_ipaddr'])

    num_neighbours = len(ospf_neighbours)

    assert num_neighbours == 2, f"{task.host.name} does not has 2 neighbors"

def test_nornir(nr):
    nr.run(task=pull_ospf)



