from is_ip_valid import is_ip_valid
from ios_ssh import ios_ssh
from napalm_get_mac import napalm_get_mac
import sys

device_ip = is_ip_valid()
ssh_connection = ios_ssh(device_ip)
mac_dict = napalm_get_mac(ssh_connection)
print(mac_dict)
