"""
FastAPI application for the WhatsApp agent.
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request

from agent.utils import send_message
from agent.whatsapp_agent import process_whatsapp_message

load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

app = FastAPI()


# =====================================================
# Webhook Verification: GET (Required by Meta)
# =====================================================
@app.get("/webhook")
async def verify(request: Request):
    """Verify webhook subscription with Meta."""
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ Webhook verified successfully")
        return int(challenge)

    print("❌ Webhook verification failed")
    return {"error": "Verification failed"}


# =====================================================
# Webhook Message Reception: POST
# =====================================================
@app.post("/webhook")
async def receive_webhook(request: Request):
    """Receive and process incoming WhatsApp messages."""
    body = await request.json()
    print("📩 Webhook received:")
    print(body)

    try:
        entry = body["entry"][0]["changes"][0]["value"]

        # Process incoming messages
        if "messages" in entry:
            message = entry["messages"][0]

            sender = message["from"]  # User's phone number
            msg_type = message["type"]

            if msg_type == "text":
                text = message["text"]["body"]
                print(f"💬 Message from {sender}: {text}")

                # Process message with the agent
                agent_response = process_whatsapp_message(sender, text)
                print(f"🤖 Agent response: {agent_response}")

                # Send agent response
                send_message(sender, agent_response)

    except Exception as e:
        print(f"⚠️ Error processing webhook: {e}")

    return {"status": "ok"}
