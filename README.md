# Dockerized Flask API
This project is a Dockerized API application that combines Flask and FastAPI. It includes Microsoft Authentication and provides a way to secure the APIs using OAuth2.

## 1.Setup Python environment
### Prerequisites

- Open Docker desktop
- Python 3.9 installed

```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
```bash

pip freeze > requirements.txt
```
**To reactivate the environment
.\.venv\Scripts\Activate**

## 2.Built Flask API
#### Test
```bash
python app.py
http://127.0.0.1:5000
```

### 3.Add Dockerfile and docker-compose.yml
#### Test
```bash
Docker-compose up –build
http://127.0.0.1:5000
```

## 4.Create a test_app.py file

## 5.Create a FastAPI fastapi_app.py
Update Dockerfile and docker-compose.yml
#### Test
```bash
docker-compose up –build
 `http://localhost:8000`
 ```

## 6.Check for dependencies conflicts
```bash
pip check
```

## 7.Contributing guide
1. Create/Clone a new repository in Git Hub

2. Create a pull request
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/maria-sanchez-g/Docker_API.git
git branch -M main
git push -u origin main
```
3. Create a new branch
```bash
git checkout -b feature-branch
git add .
git commit -m
git push origin feature-branch
```

## 8.Create an API request in Postman
1. New Collection called Docker_API
```bash
Add request
URL http://localhost:5000/ for Flask or http://localhost:8000/ for FastAPI
GET request
Body:
{
    "key": "value"
}

SEND
SAVE
```
2. Export Postman request
```bash
Colections / Export / Collection v2.1 / Save file into the project directory in Visual Studio Code
```
## 9.Microsoft Authentication using OAuth2.0 
1. Register application in Azure
```bash
Azure / Active Directory / App registration / New registration
Set up name: Docker_API Authentication
Set up URI: http://localhost:5000/callback
Register
Copy the details of: Application (client) ID / Directory (tenant) ID / Value / Secret ID
```
```bash
2. Install python lbraries in Visual Studio
pip install msal flask
```
```bash
3. Configure Environment Variables
Create an .env file/copy the .env.example / add: 
CLIENT_ID=<Your Application (client) ID>
CLIENT_SECRET=<Your Client Secret>
TENANT_ID=<Your Directory (tenant) ID>
```
4. Load Variables
```bash
pip install python-dotenv
```
5. Update requirements file
```bash
pip install python-dotenv
pip freeze > requirements.txt
```
6. Modify the app.py file

7. Modify Gitignore file

#### Test
```bash
python app.py
http://localhost:5000/login
Save the Token field
```
## 10.Postman for Authentication
1. Collection / Docker_API / Authorization
```bash
Bearer Token
In the Token field, paste the access token you received from the /callback endpoint
SEND request
```

## 11.README file
1. Createa README file
