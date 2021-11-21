import sys
from is_ip_valid import is_ip_valid
from get_mac import get_mac

device_ip = is_ip_valid()
mac_list = get_mac(device_ip)
print(mac_list)
