from getpass import getpass
from netmiko import ConnectHandler

# Create Netmiko connection
def netmiko_conn():
    net_connect = ConnectHandler(
        host="192.168.1.108",
        device_type="cisco_nxos",
        username="admin",
        password="admin",
   ) # Return Netmiko connection object
    return net_connect

# Test function which will see if function will return object which we can do find_prompt() on
def test_find_prompt():
    net_connect = netmiko_conn() # Call the function created above
    assert "NXOS1#" in net_connect.find_prompt() # We’re expecting device prompt to be returned

# Test function to see if send_command method will return correct output from sh ip int br
def test_send_command():
    net_connect = netmiko_conn() # Call the function created above
    output = net_connect.send_command("show ip int brief vrf management")
    assert "192" in output # String has to be in the output returned

