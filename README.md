  <img src='https://coverager.com/wp-content/uploads/2019/10/FRIDAY.png' width='20%' style = "align:center; margin=:auto">
<h1 align='center'>FRIDAY Code Challenge</h1> 
<h2 align='center'>Objective </h2>
Process addresses from an external addresses provider into a format that is compatible with our system

## Scope of work
An address provider returns addresses only with concatenated street names and numbers. However, our system has separate fields for street name and street number. We are going to take in the address, process it and return a JSON object with street and houseumber as keys with corresponding values

### Language Used
Python

### Procedure
For every address received, the following procedure is followed. We use Regex, IF and ELSE statements to match various address patterns and process them accordingly. We use conditional statements to:
1. Check if address starts and ends with a string 
2. Check if the address starts with a number and contains only that number
3. Check if address ends with a number. If so, check for the keyword "No" and whether it contains more numbers

For every pattern matched, further confirmatory checks are carried out to be sure of correctness of street and housenumber 

### Tools Used
1. Pytest
2. https://regex101.com/ (To check Regex patterns)
3. Flask
4. Pandas

### Tests
I used pytest library to write and run tests against the code

## Code
The repository contains the following files

1. app.py - Main script for starting and running our Flask app
2. process_addresses.py - Python script containing the address processing functions
3. functions folder - Contains the send_email script that contains a function that sends out email alerts in case of new address patterns and/or errors
4. tests folder - Contains all tests to be run against the application

## How to set up and run the code
1. Fork and clone this repository 
2. Change to the root directory of the project folder
3. Create a virtual environemnt (I am assuming you alread have pip/pip3 installed on your computer)
```
virtualenv <your-virtual-env-name>
```
4. Activate the created virtual environment
### WINDOWS
```
<your-venv-name>\Scripts\activate
```
### LINUX
```
source <your-venv-name>/bin/activate
```
5. Install the dependencies 
```
pip install -r requirements.txt 
```
6. Start the app
```
python app.py
```
7. There are two options for using the app. Through an Aplication Programming Interface (API) or web User interface (UI)
8. To make a request using the API, <a href = "https://github.com/kimerajoseph/FRIDAY_code_challenge_KJ/edit/main/api_call_procedure.txt" target="_blank"><p> Follow this procedure </p><a/>
9. To user the web UI, <a href = "https://github.com/kimerajoseph/FRIDAY_code_challenge_KJ/blob/main/using_the_web_UI.txt" target="_blank"><p> Follow this procedure </p><a/>
9. To run tests, RUN pytest command from the root directory
```
pytest
```


