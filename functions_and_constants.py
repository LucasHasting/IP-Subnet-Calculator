THIRTY_TWO_BITS = 4294967295
SUBNET_POSSIBILITIES = [128, 192, 224, 240, 248, 252, 254, 255]

def parse_address_from_str(address):
    address = address.split(".")
    return [int(i) for i in address]

def parse_address_single(address):
    result = 0
    for i in range(4):
        result |= address[3-i] << 8*i
        
    return result

def parse_address_to_str(address):
    result = [0] * 4
    
    for i in range(4):
        value = address >> 8*(3-i)
        result[i] |= value
        address -= (value << 8*(3-i))

    to_str = ""
    for i in result:
        to_str += str(i) + "."

    return to_str[:len(to_str)-1]

def valid_subnet(subnet):
    return subnet[3] >= 254 or not all(x in SUBNET_POSSIBILITIES for x in subnet) or all(x > 255 for x in subnet)

def valid_ip(ip):
    return all(x > 255 for x in ip)
