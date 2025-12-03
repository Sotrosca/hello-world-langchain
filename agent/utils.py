# =====================================================
# Send Message via WhatsApp Cloud API
# =====================================================
import requests
from main import PHONE_NUMBER_ID, WHATSAPP_TOKEN


def send_message(to: str, message: str) -> dict:
    """
    Send a WhatsApp message via Cloud API.

    Args:
        to: Recipient's phone number
        message: Message content to send
        phone_number_id: WhatsApp phone number ID
        whatsapp_token: WhatsApp API token

    Returns:
        dict: API response
    """
    url = f"https://graph.facebook.com/v24.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message},
    }

    response = requests.post(url, json=data, headers=headers)

    print(f"📤 Message sent response: {response.json()}")
    return response.json()


# =====================================================
