import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timezone
import re


cred_path = os.path.join(os.path.dirname(__file__), 'freelanz-7b495-firebase-adminsdk-fbsvc-9f4b64c5af.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to add a message to the chat
def add_message(client_name, message):
    client_ref = db.collection("Fivver_Clients").document(client_name)

    # Ensure the client document exists
    if not client_ref.get().exists:
        client_ref.set({"created_at": datetime.now(timezone.utc).isoformat()})  # Create an empty doc
    
    chat_ref = client_ref.collection("messages")
    chat_ref.add({
        "message": message,
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


# Function to get all messages for a client
def get_messages(client_name):
    chat_ref = db.collection("Fivver_Clients").document(client_name).collection("messages")
    chats = chat_ref.order_by("timestamp").stream()  # Fetch messages sorted by timestamp

    messages = []
    for chat in chats:
        chat_data = chat.to_dict()
        if chat_data:  # Ensure the document contains data
            messages.append(chat_data)

    return messages

#Function to get all client name list
def get_name_lst():
    chat_ref = db.collection("Fivver_Clients")
    clients = chat_ref.stream()  # Fetch all clients
    client_names = []

    for client in clients:
        client_data = client.to_dict()
        client_names.append(client.id)  # Use client.id to get the document ID (client name)
            
    return client_names



def simplify_bot_responses(history):
   
    """
    Formats past conversation history into a structured list of messages.
    Ensures each entry has timestamp, user_message, and bot_response.
    """
    formatted_history = []

    if isinstance(history, list):  
        for entry in history:
            if isinstance(entry, dict) and all(k in entry for k in ["timestamp", "user_message", "bot_response"]):
                formatted_history.append(
                    {"role": "user", "content": f"[{entry['timestamp']}] {entry['user_message']}"}
                )
                formatted_history.append(
                    {"role": "assistant", "content": f"[{entry['timestamp']}] {entry['bot_response']}"}
                )

    return formatted_history


clients = get_name_lst()

