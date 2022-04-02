from flask import Flask,request, render_template, jsonify
import os
from os.path import join, dirname, realpath
import process_addresses
import pandas as pd

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("home.html")


#===================================================================================================
# Process address(es) from an API request
#==================================================================================================
@app.route('/process_address_api',methods=['POST'])
def process_address_api():
    raw_address = request.get_json(force=True)
    print(type(raw_address))
    try:
        if isinstance(raw_address, dict):
            processed_address = process_addresses.process_address(raw_address["address"])
            processed_address = eval(processed_address)
            print(processed_address)
            print(jsonify(processed_address))
            return jsonify(processed_address)

        elif isinstance(raw_address,list):
            list_of_api_addresses_requested = []
            for item in raw_address:
                processed_address = process_addresses.process_address(item["address"])
                processed_address = eval(processed_address)
                list_of_api_addresses_requested.append(processed_address)
            return jsonify(list_of_api_addresses_requested)

    except Exception as err:
        instruction = "Please send either a dictionary or list eg {'streeat':'200 broadway'} or \
            [{'address':'address1'},{'address':'address2'}]"
        return jsonify(instruction)


#================================================================================
# Process a address(es) from web app front end
#================================================================================
@app.route('/process_addresses_func',methods=['POST'])
def process_addresses_func():
    final_processed_list = []
    addresses = [x for x in request.form.values()]
    print(addresses)
    if len(addresses) == 1:
        processed_address = process_addresses.process_address(addresses[0])
        processed_address = eval(processed_address)
        processed_address["address"] = addresses[0]
        final_processed_address = {"address": addresses[0],"street":processed_address["street"],"housenumber":processed_address["housenumber"]}
        return render_template("address_return.html", returned_address=final_processed_address)
    
    elif len(addresses) > 1:
        list_of_processed_addresses = process_addresses.process_multiple_addresses_func(addresses)
        list_of_processed_addresses = eval(list_of_processed_addresses)
        print(type(list_of_processed_addresses))
        for item in list_of_processed_addresses:
            item = eval(item)
            print(type(item))
            final_processed_list.append(item)
        return jsonify(final_processed_list)


#======================================================================
# Process addresses from a CSV file
#======================================================================
@app.route('/process_address_csv',methods=['POST'])
def process_address_csv():
    csv_final_processed_list = []
    # get the uploaded file
    uploaded_file = request.files['csv_file']
    if uploaded_file.filename != '':
        # set the file path and save the file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)        
        uploaded_file.save(file_path)
    csv_address_file = pd.read_csv(file_path)

    # check if address column is included in csv file
    csv_columns = [column.lower() for column in csv_address_file.columns]
    csv_address_file.columns = csv_columns
    if "addresses" not in csv_columns:
        error = "Please upload a CSV file containing a column 'addresses'"
        return render_template("home.html", data=error)
        
    print(csv_address_file.columns)
    my_addresses = csv_address_file["addresses"].tolist()
    if len(my_addresses) == 1:
        processed_address = process_addresses.process_address(my_addresses[0])
        processed_address = eval(processed_address)
        return render_template("address_return.html", returned_address=processed_address)
    
    elif len(my_addresses) > 1:
        list_of_processed_addresses = process_addresses.process_multiple_addresses_func(my_addresses)
        list_of_processed_addresses = eval(list_of_processed_addresses)
        return jsonify(list_of_processed_addresses)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)