from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir('config.yaml')

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
    print(vlan_list)

results = nr.run(task=get_vlans)
#import ipdb; ipdb.set_trace()