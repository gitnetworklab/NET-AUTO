from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('10.252.248.165', 'robot', 'Automation#987')
device.open()