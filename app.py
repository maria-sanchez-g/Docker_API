from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, Dockerized Flask API!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

