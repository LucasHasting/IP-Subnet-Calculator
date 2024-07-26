#import functions and constants
from functions_and_constants import parse_address_from_str
from functions_and_constants import parse_address_single
from functions_and_constants import parse_address_to_str
from functions_and_constants import valid_subnet
from functions_and_constants import valid_ip
from functions_and_constants import THIRTY_TWO_BITS
from functions_and_constants import BROADCAST_SHIFT
from functions_and_constants import NETWORK_SHIFT
from functions_and_constants import STAR_AMOUNT

def main():
    #try and except is used for correct input data type
    try:
        
        #get the numerical address from the user
        ip_address = parse_address_from_str(input("Enter the IP address (in dotted decimal form): "))
        subnet_mask = parse_address_from_str(input("Enter the subnet mask (in dotted decimal form): "))

        #input validation
        if(valid_subnet(subnet_mask) or valid_ip(ip_address)):
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
        
        #calculate network address
        network_address = ip_address & subnet_mask
        
        #calculate usable range and broadcast address
        range_usable = (subnet_mask ^ THIRTY_TWO_BITS) - BROADCAST_SHIFT
        broadcast_address = network_address + range_usable + BROADCAST_SHIFT
        
        #calculate usable address range
        range_min = parse_address_to_str(network_address + NETWORK_SHIFT)
        range_max = parse_address_to_str(broadcast_address - BROADCAST_SHIFT)
        
        #put the addresses back in dotted decimal format
        network_address = parse_address_to_str(network_address)
        broadcast_address = parse_address_to_str(broadcast_address)

        #display the results to the user
        print(f"\nNetwork Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        print(f"Amount of usable addresses: {range_usable}")
        print(f"Range: {range_min} - {range_max}\n")

        #ask the user to go again
        cont = input("Would you like to go again? y for yes, anything else for no: ")
        if(cont.upper() == "Y"):
            print("*" * STAR_AMOUNT)
            main()
    except:
        print("\nUnreadable Data, please try again\n")
        main()

    #program end
    return

main()
print("*" * STAR_AMOUNT)
print("Thank you for using this IP Subnet Calculator program")
