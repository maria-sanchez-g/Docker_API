from flask import Flask, jsonify, redirect, request, session, url_for
import msal
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.getenv("SECRET_KEY") # Or replace with os.getenv("SECRET_KEY") from .env file if you prefer

# Load the values from the .env file
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORITY = os.getenv("AUTHORITY")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = ["User.Read"]

# MSAL client instance
msal_client = msal.ConfidentialClientApplication(
    CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY
)

@app.route("/")
def home():
    return jsonify(message="Hello, Dockerized Flask API!")

@app.route("/login")
def login():
    # Construct authorization URL using MSAL
    auth_url = msal_client.get_authorization_request_url(
        scopes=SCOPE,
        redirect_uri=REDIRECT_URI
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    # Retrieve the authorization code from the URL
    code = request.args.get("code")
    if code:
        # Exchange the authorization code for a token
        token_response = msal_client.acquire_token_by_authorization_code(
            code,
            scopes=SCOPE,
            redirect_uri=REDIRECT_URI
        )
        if "access_token" in token_response:
            # Store token in session
            session['access_token'] = token_response["access_token"]
            return jsonify(token_response)
        else:
            return jsonify(error="Authentication failed", details=token_response.get("error_description"))
    return jsonify(error="No authorization code received")

# Middleware-like function to check access token in session
@app.before_request
def check_auth_token():
    if 'access_token' not in session and request.endpoint != 'login' and request.endpoint != 'callback':
        return redirect(url_for('login'))  # Redirect to login if no access token is found
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




