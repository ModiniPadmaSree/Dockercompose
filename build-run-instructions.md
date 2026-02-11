This document explains about build docker custom image, run container from image with the Dockerfile and access the application. \
Prerequisites
1. Machine / EC2 with docker installed.
2. Creating Dockerfile: A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Create a file named Dockerfile in application's root directory.
3. Application(app.py), package(requirements.txt) \
 \
Steps
1. Build the docker image: Navigate to application's root directory and run the docker build command. 
The . at the end tells Docker to look for the Dockerfile in the current directory \
docker build -t python-web-app .
2. Run the Docker container: After image is built, start and run the container from the image. \
docker run -d -p 5000:5000 --name python-web-container python-web-app \
-d: container run in detached mode 
-p: host port:container port \
name: assign name of the container \
python-web-app: image name
3. Verify container: docker ps
4. Access the application: In browser, ip-of-instance:port \
http://52.54.246.144:5000
5. Outputs "Hello from Dockerized Python Web App!"
