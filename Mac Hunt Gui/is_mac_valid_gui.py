import sys
import re

def is_mac_valid(mac_address):

    mac_check = re.compile('^([0-9a-fA-F]{2}[-:]){5}([0-9a-fA-F]{2})$|^([0-9a-fA-F]{4}[.]){2}([0-9a-fA-F]{4})$')
    is_mac_valid = mac_check.match(mac_address)

    if is_mac_valid == None:
        print("\n{} is not a valid MAC.\n".format(mac_address))
        sys.exit()
    
    else:
        pass