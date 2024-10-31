# Dockerized Flask API
This project is a Dockerized API application that combines Flask and FastAPI. It includes Microsoft Authentication and provides a way to secure the APIs using OAuth2. 

## Setup Visual Studio
1. Shell
python -m venv venv
.\venv\Scripts\activate
pip freeze > requirements.txt

To reactivate the environment
.\.venv\Scripts\Activate

2. Built Flask API
#Test
python app.py
http://127.0.0.1:5000

3. Add Dockerfile and docker-compose.yml
#Test
Docker-compose up –build
http://127.0.0.1:5000

4.Create a test_app.py file

5. Create a FastAPI fastapi_app.py
Update Dockerfile and docker-compose.yml
#Test
docker-compose up –build
 http://localhost:8000

6.Check for dependencies conflicts
pip check

## Set up Git Hub
1. Create a new repository in Git Hub

2. Create a pull request
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/maria-sanchez-g/Docker_API.git
git branch -M main
git push -u origin main

3. Create a new branch
git checkout -b feature-branch
git add .
git commit -m
git push origin feature-branch

## Create an API request in Postman
New Collection called Docker_API
Add request
URL http://localhost:5000/ for Flask or http://localhost:8000/ for FastAPI
GET request
Body:
{
    "key": "value"
}

SEND
SAVE

2. Export Postman request
Colections / Export / Collection v2.1 / Save file into the project directory in Visual Studio Code

## Microsoft Authentication using OAuth2.0 
1. Register application in Azure
Azure / Active Directory / App registration / New registration
Set up name: Docker_API Authentication
Set up URI: http://localhost:5000/callback
Register
Copy the details of: Application (client) ID / Directory (tenant) ID / Value / Secret ID

2. Install python lbraries in Visual Studio
pip install msal flask

3. Configure Environment Variables
Create an .env file / add: 
CLIENT_ID=<Your Application (client) ID>
CLIENT_SECRET=<Your Client Secret>
TENANT_ID=<Your Directory (tenant) ID>

4. Load Variables
pip install python-dotenv

5. Update requirements file
pip install python-dotenv
pip freeze > requirements.txt

6. Modify the app.py file

7. Modify Gitignore file
# .gitignore
.env

8.#Test
python app.py
http://localhost:5000/login
Save the Token field

## Postman for Authentication
1. Collection / Docker_API / Authorization
Bearer Token
In the Token field, paste the access token you received from the /callback endpoint
SEND request

## README file
1. Createa README file
