from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    direction = data["direction"]
    symbol = data["symbol"]
    entry = data["entry"]
    sl = data["sl"]
    tp1 = data["tp1"]
    tp2 = data["tp2"]

    emoji = "🟢 LONG" if direction == "LONG" else "🔴 SHORT"
    
    message = f"""
{emoji} <b>ADVANCED TOPSTEP ALERT</b> {emoji}

📍 <b>{symbol}</b>
Entry → <code>{entry}</code>
SL → <code>{sl}</code>
TP1 → <code>{tp1}</code>
TP2 → <code>{tp2}</code>

Reason: Advanced EMA Pullback + Filters
    """

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    requests.post(url, json=payload)
    return {"status": "ok"}
