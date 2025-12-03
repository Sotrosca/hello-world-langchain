"""
Custom tools for the WhatsApp agent.
"""

from langchain_core.tools import tool

from agent.utils import send_message


@tool
def send_whatsapp_message(phone_number: str, message: str) -> str:
    """
    Send a WhatsApp message to initiate a conversation.

    Args:
        phone_number: Recipient's phone number (with country code, e.g., 5491112345678)
        message: Message content to send

    Returns:
        str: Operation result (success or error)
    """
    try:
        result = send_message(phone_number, message)
        message_id = result.get("messages", [{}])[0].get("id", "N/A")
        return f"Message sent successfully to {phone_number}. ID: {message_id}"

    except Exception as e:
        error_msg = f"Error sending message: {str(e)}"
        print(f"❌ {error_msg}")
        return error_msg
