from napalm import get_network_driver

def napalm_get_config(ssh):

    ios_output = ssh.get_config()
    
    return ios_output