# The docker image is built on top of the python3.7 image
FROM python:3.7
# Copy all files and folders to a folder named "app" inside the #image
COPY . /app
# change working directory to our main folder
WORKDIR /app
# install all libraries and dependencies
RUN pip install -r requirements.txt
# expose port 5000 to external connections
EXPOSE 5000
# if you are running the image locally
ENTRYPOINT ["python", "app.py"]