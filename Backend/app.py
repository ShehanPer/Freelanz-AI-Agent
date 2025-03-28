from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import os
from chatbot import get_response
from firebase import add_message, get_messages, get_name_lst, simplify_bot_responses

app = Flask(__name__)

# Initialize Firebase Admin SDK


def save_chat_to_firebase(client_name,user_message, bot_response):
    """
    Saves the user-bot conversation to Firebase Realtime Database.
    """
    if(user_message):
        add_message(client_name, "user_message" + user_message)
    if(bot_response):
        add_message(client_name, "bot_response" + bot_response)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Debugging statement

        user_message = data.get('message')
        print(f"User message: {user_message}")  # Debugging statement

        client_name = data.get('client')
        print(f"Client name: {client_name}")  # Debugging statement
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Prepare messages for the NVIDIA API
        messages = [{"role": "user", "content": user_message}]
        history = get_messages(client_name)
       
        # Send user message to Nvidia API
        bot_response = get_response(messages,history,client_name)
        print(f"Bot response: {bot_response}")  # Debugging statement

        # Save chat log to Firebase
        save_chat_to_firebase(client_name,user_message, bot_response)

        # Respond back to the client
        return jsonify({"response": bot_response}), 200

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging statement
        return jsonify({"error": str(e)}), 500

@app.route('/clients', methods=['GET'])
def clients():
    try:
        client_names = get_name_lst()
        return jsonify({"clients": client_names}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)