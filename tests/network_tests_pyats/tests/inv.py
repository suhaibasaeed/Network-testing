from genie.testbed import load

# Load testbed file
testbed = load('testbed.yaml')

# Get devices attribute
devices = testbed.devices
# Print devices
for k, v in devices.items():
    print(k, v)