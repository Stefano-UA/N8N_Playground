import os

import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Only allow trusted origins, configurable via environment variable
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})

REQUEST_TIMEOUT = 10  # seconds


def fetch_internal_data(api_url):
    """Fetch JSON data from an internal API with SSL verification enabled."""
    try:
        response = requests.get(api_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        app.logger.error("Error fetching %s: %s", api_url, error)
        return None


@app.route("/health")
def health():
    """Simple health check endpoint."""
    return jsonify(status="ok")



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")))
#commit1