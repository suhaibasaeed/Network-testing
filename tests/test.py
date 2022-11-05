
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Initalise nornir
nr = InitNornir(config_file="config.yaml")

show_result = nr.run(task=send_command, command="show version")

print_result(show_result)


