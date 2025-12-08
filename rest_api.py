"""
Simple REST API for Smart Door Alert

- Reads door event history from ../data/events.csv
- Exposes two endpoints:
    GET /events        -> all events as JSON
    GET /events/latest -> most recent event
- Uses a very simple API key check via X-API-Key header
  (course requirement: basic authentication / key management).
"""

from flask import Flask, jsonify, request, abort
import csv
import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]   # project root
DATA_FILE = BASE_DIR / "data" / "events.csv"

# Very simple API key (for demo only)
API_KEY = "smartdoor123"

app = Flask(__name__)


def check_api_key():
    """
    Basic API key check using X-API-Key header.
    This is NOT production security, but demonstrates key-based access.
    """
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        abort(401, description="Invalid or missing API key")


def load_events():
    """Load all door events from the CSV file as a list of dicts."""
    events = []
    if not DATA_FILE.exists():
        return events

    with DATA_FILE.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            events.append(row)
    return events


@app.get("/events")
def get_events():
    """
    Return all recorded door events.

    Example:
      curl -H "X-API-Key: smartdoor123" http://localhost:5000/events
    """
    check_api_key()
    events = load_events()
    return jsonify(events)


@app.get("/events/latest")
def get_latest_event():
    """
    Return the most recent door event or 404 if there are none.

    Example:
      curl -H "X-API-Key: smartdoor123" http://localhost:5000/events/latest
    """
    check_api_key()
    events = load_events()
    if not events:
        return jsonify({"message": "no events yet"}), 404
    return jsonify(events[-1])


if __name__ == "__main__":
    # Run on all interfaces so you can test from Postman
    app.run(host="0.0.0.0", port=5000, debug=True)
