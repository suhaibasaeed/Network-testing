from pyats import aetest
from genie.conf import Genie


class DeviceTestCase(aetest.Testcase):
    @aetest.setup
    # Define how to connect to devices
    def setup(self):
        self.parameters["testbed"].connect(log_stdout=False) # Turn off console logging

    # Use test decorator
    @aetest.test
    def show_version(self):
        for device in self.parameters["testbed"].devices.values():
            # Send command to the device and parse the output then assert
            show_version = device.parse('show version')
            assert show_version["platform"]["software"]["system_version"] == "9.2(3)"

# Initalise testbed and pass into aetest
topology = Genie.init("testbed.yaml")
aetest.main(testbed=topology)