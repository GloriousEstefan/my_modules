from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException
from getpass import getpass
import sys

def ios_ssh(ip_addr):
    
    username,password = input("\nUsername:\n"),getpass("Password:\n", stream=None)

    print("Attempting to connect to {}\n".format(ip_addr))

    try:
    
        driver = get_network_driver('ios')
        ios = driver(ip_addr, username, password)
        ios.open()

    except ConnectionException:

        print("Unable to connect to device {}\n".format(ip_addr))
        sys.exit()

    print("Connection to {} successful\n".format(ip_addr))

    return ios
