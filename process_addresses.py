import re
from functions import send_email
import copy

processed_address_list = []

# ALL MY REGEX EXPRESSIONS
re_number_at_end = "[0-9]+$"
re_number_at_start = '^[0-9]+'
starts_with_string = "^[a-zA-Z]+"
ends_with_string = "[a-zA-Z]+$"


#=============================================================
# Function that processes a single address
#=============================================================

def process_address(address):
    try:
        # CHECK IF ADDRESS STARTS AND ENDS WITH A STRING
        if re.search(starts_with_string,address) and re.search(ends_with_string,address):
                # check if last word contains a digit
                if re.search(r'\d',address.split(' ')[-1]):
                        street =  re.sub("[^a-zA-Z0-9]+", "",address.rsplit(' ', 1)[0])                    
                        housenumber = address.split(" ")[-1]
                        return str({"street":street,"housenumber":str(housenumber)})

                # check if second last word is numeric
                elif address.split(' ')[-2].isnumeric:
                        street  = address.rsplit(" ",2)[0]
                        housenumber = f"{address.split(' ')[-2]} {address.split(' ')[-1]}"
                        return str({"street":street,"housenumber":str(housenumber)})

        # CHECK IF ADDRESS ENDS WITH A NUMBER AND DOES NOT START WITH NUMBER
        elif re.search(re_number_at_end,address) and not re.search(re_number_at_start,address):
                # Check if the addess contains another number
                if "No" in address and [word.isnumeric for word in address.split(" ")[:-1]]:
                        street  = address.rsplit(" ",2)[0]
                        housenumber = f"{address.split(' ')[-2]} {address.split(' ')[-1]}"
                        return str({"street":street,"housenumber":str(housenumber)})
                
                else:
                        street =  address.rsplit(' ', 1)[0]                     
                        housenumber =  address.split(" ")[-1]
                        #return str({"address":address,"processed_address":{"street":street,"housenumber":str(housenumber)}})
                        return str({"street":street,"housenumber":str(housenumber)})

        # CHECK IF ADDRESS STARTS WITH A NUMBER AND CONTAINS ONLY THAT NUMBER AT THE START
        elif re.search(re_number_at_start,address) and [not word.isnumeric for word in address.strip(" ")[1:]]:
                street  = address.split(' ', 1)[1]              
                housenumber = re.sub("[^a-zA-Z0-9]+", "",address.split(" ")[0])  
                return str({"street":street,"housenumber":str(housenumber)})

        else:
                # Send an email informing the team of the new unseen address pattern
                # call the email send function  
                print("NEW ADDRESS DETECTED: ",address)
                send_email.send_new_address_email_alert(address)
                return str({"street":"undetermined","housenumber":"undetermined"})

    except Exception as err:
        # Send an email informing the team of the error. I think a text message or slack is more appropriate
        send_email.send_error_email_alert(err)


#==========================================================================================
# Function that processes a list of addresses
# =========================================================================================     
def process_multiple_addresses_func(my_addresses):
        for address in my_addresses:
                # call function that processes a single address
                single_processed_address = process_address(address)
                processed_address_list.append(single_processed_address)
        final_processes_address = copy.deepcopy(processed_address_list)
        processed_address_list.clear()
        print("FINAL LIST: ",final_processes_address)
        return str(final_processes_address)



#==========================================================================================
# UNCOMNET THE MAIN FUNCTION IF THIS PROGRAM IS TO BE RUN WITH THIS AS THE MAIN SCRIPT 
#==========================================================================================

# if __name__ == "__main__":
#     for address in addresses:
#         print(process_address(address))
    