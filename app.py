from flask import Flask, request, jsonify
import requests
from requests_oauthlib import OAuth1

app = Flask(__name__)

@app.route("/")
def home():
    return "Twitter Poster API is running."

@app.route("/tweet", methods=["POST"])
def tweet():
    data = request.get_json()
    status = data.get("text", "Hello from Render!")

    auth = OAuth1(
        "V2XSmTQILxP5tY7FWsy38mBJ1",
        "cY2WzOReypHsgqP7anXHaA4ho72wKhAM1bEVbLOqqBcklARRgP",
        "1927337849675829248-9rBdH3f8ykuahONvbWejQWhbULEwHH",
        "ZcYvU4AUEIDBuKgVc8A0Q57J25ltS7g7BqD8BNLtYIUWf"
    )

    response = requests.post(
        "https://api.twitter.com/1.1/statuses/update.json",
        auth=auth,
        data={"status": status}
    )

    if response.status_code == 200:
        return jsonify({"success": True, "response": response.json()})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code
