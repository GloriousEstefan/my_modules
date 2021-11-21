import sys

#Checking octets
def is_ip_valid():

    ip_addr = input("\nEnter IP address:\n")
    ip_addr = ip_addr.rstrip("\n")
    octet_list = ip_addr.split('.')
        
    if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
        print("\n{} is a valid IP address.".format(ip_addr))
             
    else:
        print("\n{} is not a valid IP address.".format(ip_addr))
        sys.exit()

    return ip_addr