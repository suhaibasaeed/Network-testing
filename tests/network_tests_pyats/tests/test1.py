from genie.testbed import load

# Load testbed file
testbed = load('testbed.yaml')

# Get device object and connect to nxos1 device
nxos1 = testbed.devices['nxos1']
# Turn off logging to console
nxos1.connect(log_stdout=False)
# get OSPF neighbours as structured data via genie and print
ospf_neighbours = nxos1.parse('show ip ospf neighbors detail')
print(ospf_neighbours)
