from pytest_check import check_func
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# We don't want assertions to end on first fail
@check_func
def get_vlans(task):

    result = task.run(task=send_command, command='show vlan')
    # Store results of show vlan structured data in host obj
    task.host['facts'] = result.scrapli_response.genie_parse_output()
    vlans = task.host['facts']['vlans']

    # Loop through vlans, parse and return dict - then add to list
    vlan_list = []
    for vlan in vlans:
        vlan_id = int(vlan)
        name = vlans[vlan]['name']
        vlan_dict = {"id": vlan_id, "name": name}
        vlan_list.append(vlan_dict)

    assert len(vlan_list) == 5, f"{task.host.name} doesn't have the correct VLANs configured"

def test_nornir(nr):
    nr.run(task=get_vlans)

#import ipdb; ipdb.set_trace()