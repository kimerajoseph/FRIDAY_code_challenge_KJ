import re
from functions import send_email

# test all provided addresses
addresses = ["Winterallee 3","Musterstrasse 45","Blaufeldweg 123B","Am Bächle 23","Auf der Vogelwiese 23 b",
"4, rue de la revolution","200 Broadway Av","Calle Aduana, 29","Calle 39 No 1540"]


# ALL MY REGEX EXPRESSIONS
re_number_at_end = "[0-9]+$"
re_number_at_start = '^[0-9]+'
starts_with_string = "^[a-zA-Z]+"
ends_with_string = "[a-zA-Z]+$"

def process_address(address):
    print("ADDRESS IS: ",address)
    try:
        # CHECK IF ADDRESS STARTS AND ENDS WITH A STRING
        if re.search(starts_with_string,address) and re.search(ends_with_string,address):
                # check if last word contains a digit
                if re.search(r'\d',address.split(' ')[-1]):
                        street =  re.sub("[^a-zA-Z0-9]+", "",address.rsplit(' ', 1)[0])                    
                        housenumber = address.split(" ")[-1]
                        return {"street":street,"housenumber":str(housenumber)}

                # check if second last word is numeric
                elif address.split(' ')[-2].isnumeric:
                        street  = address.rsplit(" ",2)[0]
                        housenumber = f"{address.split(' ')[-2]} {address.split(' ')[-1]}"
                        return {"street":street,"housenumber":str(housenumber)}

        # CHECK IF ADDRESS ENDS WITH A NUMBER
        elif re.search(re_number_at_end,address):
                # Check if the addess contains another number
                if "No" in address and [word.isnumeric for word in address.split(" ")[:-1]]:
                        street  = address.rsplit(" ",2)[0]
                        housenumber = f"{address.split(' ')[-2]} {address.split(' ')[-1]}"
                        return {"street":street,"housenumber":str(housenumber)}
                
                else:
                        street =  address.rsplit(' ', 1)[0]                     
                        housenumber =  address.split(" ")[-1] 
                        return {"street":street,"housenumber":str(housenumber)}

        # CHECK IF ADDRESS STARTS WITH A NUMBER AND CONTAINS ONLY THAT NUMBER AT THE START
        elif re.search(re_number_at_start,address) and [not word.isnumeric for word in address.strip(" ")[1:]]:
                street  = address.split(' ', 1)[1]              
                housenumber = re.sub("[^a-zA-Z0-9]+", "",address.split(" ")[0])  
                return {"street":street,"housenumber":str(housenumber)}

        else:
                # Send an email informing the team of the new unseen address pattern
                # call the email send function  
                print("NEW ADDRESS DETECTED: ",address)
                send_email.send_new_address_email_alert(address)

    except Exception as err:
        # Send an email informing the team of the error. I think a text message or slack is more appropriate
        send_email.send_error_email_alert(err)

if __name__ == "__main__":
    for address in addresses:
        print(process_address(address))
    