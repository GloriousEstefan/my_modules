from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException
from getpass import getpass
import sys

def ios_ssh(ip_addr, username, password):

    try:
    
        driver = get_network_driver('ios')
        ios = driver(ip_addr, username, password)
        ios.open()

    except ConnectionException:
        
        sys.exit()

    return ios
