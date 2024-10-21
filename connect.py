from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.1.205', '*', '*')
device.open()
device.close()