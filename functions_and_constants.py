# constants
THIRTY_TWO_BITS = 4294967295
BROADCAST_SHIFT = NETWORK_SHIFT = 1
ADDRESS_POSITIONS = 4
NULL = 0
BITS_IN_BYTE = 8
MAX_SUBNET = 254
MAX_ADDRESS = 255
LAST_DOTTED_DECIMAL_POSITION = 3
END_OF_STR_SHIFT = 1
STAR_AMOUNT = 68
SUBNET_POSSIBILITIES = [128, 192, 224, 240, 248, 252, 254, 255]

'''
Name:         parse_address_from_str
Description:  takes in an IP address in dotted decimal format and converts it 
              to a list containing each decimal
'''
def parse_address_from_str(address):
    address = address.split(".")
    return [int(i) for i in address]

'''
Name:         parse_address_single
Description:  takes in an IP address in list form and converts it to a single 
              integer representing the binary value of the address 
'''
def parse_address_single(address):
    result = NULL
    for i in range(ADDRESS_POSITIONS):
        result |= address[LAST_DOTTED_DECIMAL_POSITION-i] << BITS_IN_BYTE*i
        
    return result

'''
Name:         parse_address_to_str
Description:  takes in an IP address as a single integer and puts the address
              back into a dotted decimal formatted address as a string
'''
def parse_address_to_str(address):
    # create empty list to contain the address
    result = [NULL] * ADDRESS_POSITIONS

    # put the single integer into list form
    for i in range(ADDRESS_POSITIONS):
        value = address >> BITS_IN_BYTE*(LAST_DOTTED_DECIMAL_POSITION-i)
        result[i] |= value
        address -= value << BITS_IN_BYTE*(LAST_DOTTED_DECIMAL_POSITION-i)

    # turn the list into dotted decimal form as a string
    to_str = ""
    for i in result:
        to_str += str(i) + "."

    #returns the string except the last character which is an extra dot
    return to_str[:len(to_str)-END_OF_STR_SHIFT]

'''
Name:         valid_subnet
Description:  takes in a subnet address in list form and validates the address
'''
def valid_subnet(subnet):
    return not all(x in SUBNET_POSSIBILITIES for x in subnet) 
    

'''
Name:         valid_ip
Description:  takes in a IP address in list form and validates the address
'''
def valid_ip(ip):
    return not all(x < MAX_ADDRESS for x in ip)
