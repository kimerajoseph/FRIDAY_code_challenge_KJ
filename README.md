  <img src='https://coverager.com/wp-content/uploads/2019/10/FRIDAY.png' width='20%' style = "align:center; margin=:auto">
<h1 align='center'>FRIDAY Code Challenge</h1> 
<h2 align='center'>Objective </h2>
Process addresses from an external addresses provider into a format that is compatible with our internal system

## Scope of work
An address provider returns addresses only with concatenated street names and numbers. However, our system has separate fields for street name and street number. We are going to take in the address, process it and return a JSON object with street and housenumber as keys with corresponding values

### Language Used
Python

### Version
Python 3.9

### Procedure
For every address received, the following procedure is followed. We use Regex and conditional statements to match various address patterns and process them accordingly. We use conditional statements to:
1. Check if address starts and ends with a string 
2. Check if the address starts with a number and contains only that number
3. Check if address ends with a number. If so, check for the keyword "No" and whether it contains more numbers
4. Send out an email alert in case the provided address does not match any of the patterns

For every pattern matched, further confirmatory checks are carried out to be sure of correctness of street and housenumber 

### Tools Used
1. Pytest
2. https://regex101.com/ (To check Regex patterns)
3. Flask
4. Pandas

### Tests
I used pytest library to write and run tests against the code
Tests check the following:
1. That the object returned is a dictionary with two key-value pairs
2. That both keys and values are of type string

## Code
The repository contains the following files

1. app.py - Main script for starting and running our Flask app
2. process_addresses.py - Python script containing the address processing functions
3. functions folder - Contains the send_email script that contains a function that sends out email alerts in case of new address patterns and/or errors
4. tests folder - Contains all tests to be run against the application
5. Docker and .dockerignore files to run the app in a docker container (Especially for windows users)

## How to set up and run the code
1. Fork and clone this repository 
2. Change to the root directory of the project folder
3. Create a virtual environemnt (I am assuming you alread have pip/pip3 installed on your computer)

# NOTE:
The final tests for this code were done on a Linux-2 machine. For other operating systems, I advise you run the app in a docker container. All the necessary files and instructions are included in this repository
```
virtualenv <your-virtual-env-name>
```
4. Activate the created virtual environment
#### WINDOWS
```
<your-venv-name>\Scripts\activate
```
#### LINUX
```
source <your-venv-name>/bin/activate
```
5. Install the dependencies 
```
pip install -r requirements.txt 
```
6. Set up your environment variables in .env file.
You have to set up your email first. If you are using gmail, <a href="https://support.google.com/accounts/answer/6010255?hl=en"><p>Check out this link </p></a>
These emails are to be used in sending alerts to team members
```
sending_email_address=<your-sample-email-address>
password=<password-for-your-sample-application>
receiving_email=<put-any-email-address>
```
7. Start the app
```
python app.py
```
8. There are two options for using the app. Through an Aplication Programming Interface (API) or web User interface (UI)
9. To make a request using the API, <a href = "https://github.com/kimerajoseph/FRIDAY_code_challenge_KJ/edit/main/api_call_procedure.txt" target="_blank"><p> Follow this procedure </p><a/>
10. To user the web UI, <a href = "https://github.com/kimerajoseph/FRIDAY_code_challenge_KJ/blob/main/using_the_web_UI.txt" target="_blank"><p> Follow this procedure </p><a/>
11. To run tests, RUN pytest command from the root directory
```
pytest
```

## PROCEDURE FOR RUNNING THE APP USING DOCKER
The repository contains docker files that can be used to build and run images
  
## Prerequisites
Docker already installed. If not,check the official docs <a href="https://docs.docker.com/get-docker/"><p> Here </p></a>
  
1. Run the following command
  ```
  docker build -t <image-name> .
  ```
 2. The above command builds and tags a docker image using the Dockerfile in the current directory
 ```
  docker run <image-name>
  ```
3. Docker starts and runs locally
4. Copy and paste the provided URL in the browser (The URL with the comment CRTL+C. Try both URLs and see which one works)
5. Run the app and test as before
  
## RUNNING TESTS INSIDE A DOCKER CONTAINER
1. Get the container ID by running the command below
  ```
  docker ps
  ```
2. Open a bash session inside the container
  ```
  docker exec -it <container_id> /bin/bash 
  ```
3. Run the following command
  ```
  pytest
  ```
4. After, type exit to close the bash session
  ```
  exit
  ```
