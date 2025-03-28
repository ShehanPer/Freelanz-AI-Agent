# Freelanz Assistance Chatbot - Microsoft Edge Extension

## Overview

The **Freelanz Assistance Chatbot** is a Microsoft Edge extension designed for **freelancers** to manage their work efficiently. This chatbot helps freelancers communicate with clients seamlessly, store and retrieve past conversations, and integrate AI-powered assistance. The extension supports **NVIDIA NIM chatbot**, **Firebase storage**, and **short-term memory** for smarter client interactions.

## Features

- 🤖 **AI-Powered Chatbot** – Integrated **NVIDIA NIM chatbot** for intelligent responses.
- 🔄 **Client Data Management** – Automatically stores and retrieves past conversations from **Firebase**.
- 📝 **Short-Term Memory** – Uses past messages for better responses and client tracking.
- 📂 **Client Selection & Addition** – Users can select existing clients or add new ones to the database.
- 📊 **Smart Analysis** – The chatbot analyzes previous interactions to assist in decision-making.
- 🌍 **Microsoft Edge Compatibility** – Runs smoothly as a browser extension.

---

## Installation Guide

### 1️⃣ Prerequisites

- **Microsoft Edge (Latest Version)**
- **Windows/Linux/macOS**
- (Optional) **Python 3+** for backend integration

### 2️⃣ Load Extension into Edge

1. Open **Microsoft Edge**.
2. Go to `edge://extensions/`.
3. Enable **Developer Mode** (toggle in the bottom left corner).
4. Click **"Load unpacked"** and select the project folder.
5. The extension should now be available in the toolbar.

---

## File Structure

```
/project-root
|──Frontend
  │── background.js     # Background script handling events
  │── manifest.json     # Extension metadata
  │── popup.html        # User interface (popup window)
  │── popup.js          # Handles popup actions
  │── styles.css        # Custom styling for UI
  │── agent.png         # Images and icons
│── backend/            # Python backend server
  |──app.py             # main backend sever 
  |──firebase.py        # database handling
  |──chatbot.py         # LLM model handling
```

---

## Usage

1. Click the **Freelanz chatbot icon** in Edge.
2. Select an existing **client** or type a new client name.
3. Start chatting with the AI assistant.
4. The assistant will analyze past interactions and provide context-aware responses.
5. Data is automatically stored and retrieved from **Firebase**.

---

## Backend Setup (Hosted on Raspberry Pi)

The backend is hosted locally on a **Raspberry Pi** to handle chat processing, data storage, and AI-powered interactions.

### 1️⃣ Technologies Used

#### **Frontend**

- **HTML, CSS, JavaScript** – Used for the extension UI.
- **Manifest v3** – Defines permissions and extension behavior.
- **Microsoft Edge API** – Manages extension interactions.

#### **Backend**

- **Flask** – Python-based framework for handling API requests.
- **Firebase** – Stores client chat history and user data.
- **NVIDIA NIM API** – AI chatbot integration for intelligent responses.
- **Python 3** – Core backend logic.
- **Raspberry Pi** – Local hosting environment.

### 2️⃣ Install Dependencies

```sh
pip install flask firebase-admin
```

### 3️⃣ API Endpoints

| Method | Endpoint   | Description                                                |
| ------ | ---------- | ---------------------------------------------------------- |
| `POST` | `/chat`    | Sends user messages to the chatbot and retrieves responses |
| `GET`  | `/clients` | Fetches a list of saved clients from Firebase              |

### 4️⃣ Run the Server

```sh
cd backend
python3 app.py
```

### 5️⃣ Access the Backend

- Locally: `http://127.0.0.1:5000`
- Over Network: `http://<raspberry-pi-ip>:5000`

To expose the backend to the internet, use **Ngrok** or **Cloudflare Tunnel**.

---

## Contribution

Feel free to contribute, suggest improvements, or report issues!

## License

This project is open-source and can be modified as needed.

Developed by **Shehan Perera **🚀

