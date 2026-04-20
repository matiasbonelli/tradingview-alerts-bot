from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "content" in data:
        mensaje = data["content"]
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})
    return "ok", 200

@app.route("/")
def index():
    return "Bot activo", 200
