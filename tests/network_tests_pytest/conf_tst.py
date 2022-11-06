from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir('config.yaml')

result = nr.run(task=send_configs, configs=["vlan 10", "name TEN", "vlan 20", "name TWENTY", "vlan 30", "name THIRTY", "vlan 40", "name FOURTY"])

print_result(result)