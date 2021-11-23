from napalm import get_network_driver

def napalm_get_mac(ssh):

    ios_output = ssh.get_mac_address_table()
    mac_addresses, interfaces = [a_dict['mac'] for a_dict in ios_output], [a_dict['interface'] for a_dict in ios_output]
    data = dict(zip(mac_addresses, interfaces))

    print("Data retrieved successfully")
    
    return data