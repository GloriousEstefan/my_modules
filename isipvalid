import sys

#Checking octets
def ip_addr_valid(ip_address):

    ip_address = ip_address.rstrip("\n")
    octet_list = ip_address.split('.')
        
    if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
        continue
             
    else:
        print("{} is not a valid IP address.\n".format(ip_address))
        sys.exit()