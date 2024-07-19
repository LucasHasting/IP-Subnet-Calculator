#import functions and constants
from functions_and_constants import parse_address_from_str
from functions_and_constants import parse_address_single
from functions_and_constants import parse_address_to_str
from functions_and_constants import valid_subnet
from functions_and_constants import valid_ip
from functions_and_constants import THIRTY_TWO_BITS

def main():
    #try and except is used for correct input data type
    try:
        
        #get the numerical address from the user
        ip_address = parse_address_from_str(input("Enter the IP address: "))
        subnet_mask = parse_address_from_str(input("Enter the subnet mask: "))

        #input validation
        if(valid_subnet(subnet_mask) and valid_ip(ip_address)):
            print("\nNo usable addresses, the subnet is impossible, or an address is out of range")
            print("Please pick something different\n")

            #run the program again
            main()
            return

        ##############################################################
        #PROGRAM PROCESSING STARTS HERE
        
        #get the addresses as a single numerical value
        ip_address = parse_address_single(ip_address)
        subnet_mask = parse_address_single(subnet_mask)
        
        #calculate network/broadcast address and total addresses
        network_address = ip_address & subnet_mask
        
        #calculate usable range and broadcast address
        range_usable = THIRTY_TWO_BITS - subnet_mask - 1
        broadcast_address = network_address + range_usable + 1
        
        #calculate usable address range
        range_min = parse_address_to_str(network_address + 1)
        range_max = parse_address_to_str(broadcast_address - 1)
        
        #put the addresses back in dotted decimal format
        network_address = parse_address_to_str(network_address)
        broadcast_address = parse_address_to_str(broadcast_address)

        #display the results to the user
        print(f"\nNetwork Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        print(f"Amount of usable addresses: {range_usable}")
        print(f"Range: {range_min} - {range_max}")
    except:
        print("Unreadable Data, please try again\n")
        main()

    #program end
    return

main()
