from genie.testbed import load
from rich import print
from json import dumps
# Load testbed file
testbed = load('testbed.yaml')

# Loop through device objects and connect to devices serially
for name in testbed.devices.keys():
    dev = testbed.devices[name]
    # Turn off logging to console
    dev.connect(log_stdout=False)
    # get intf info as structured data via genie and print
    intfs = dev.parse('show interface')
    pretty_intfs = dumps(intfs, indent=3)
    print(f"{name}\n{pretty_intfs}")
