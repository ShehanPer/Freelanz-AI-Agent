// Grab elements
const homePage = document.getElementById("home-page");
const chatPage = document.getElementById("chat-page");
const startChatBtn = document.getElementById("start-chat");
const backHomeBtn = document.getElementById("back-home");
const chatDisplay = document.getElementById("chat-display");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const clientInput = document.getElementById("client-input"); 
const clientDatalist = document.getElementById("clients"); 
const closeButton = document.getElementById("close-button");
const container = document.getElementById("container");


// Navigation between pages
startChatBtn.addEventListener("click", () => {
    const selectedClient = clientInput.value.trim(); // Allow manual input
    if (selectedClient) {
        homePage.classList.remove("active");
        chatPage.classList.add("active");
    } else {
        alert("Please select or type a client name to start chat");
    }
});


backHomeBtn.addEventListener("click", () => {
    chatPage.classList.remove("active");
    homePage.classList.add("active");
});

// Event listener for sending messages
sendButton.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevents newline in textarea
        sendMessage();
    }
});

closeButton.addEventListener("click",()=>{
    window.close();
})


// Send message function
function sendMessage() {
    const message = userInput.value.trim();
    const selectedClient = clientInput.value.trim(); // Updated to use input

    if (!message || !selectedClient) return;

    // Display user's message
    appendMessage("User", message);

    // Send message to backend
    sendMessageToBackend(message, selectedClient);

    // Clear input field
    userInput.value = "";
}

// Append a message to the chat display
function appendMessage(sender, message) {
    const msgDiv = document.createElement("div");

    if (sender === "User") {
        msgDiv.classList.add("user-message");
    } else {
        msgDiv.classList.add("bot-message");
    }

    msgDiv.innerHTML = message;
    chatDisplay.appendChild(msgDiv);
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Auto-scroll
}

// Send the user's message to the backend
function sendMessageToBackend(message, client) {
    fetch("http://192.168.43.127:5000/chat", {//http://127.0.0.1:5000/chat
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message, client: client })
    })
    .then((response) => {
        if (!response.ok) throw new Error("Backend error");
        return response.json();
    })
    .then((data) => {
        appendMessage("FreelanZ", data.response);
    })
    .catch((error) => {
        console.error("Error:", error);
        appendMessage("FreelanZ", " Error: Unable to connect to backend.");
    });
}

// Fetch clients from backend
function fetchClientNames() {
    fetch("http://192.168.43.127:5000/clients", {//http://127.0.0.1:5000/clients
        method: "GET",
        headers: { "Content-Type": "application/json" }
    })
    .then(response => {
        if (!response.ok) throw new Error("Backend error");
        return response.json();
    })
    .then(data => {
        populateClientDatalist(data.clients);
    })
    .catch(error => {
        console.error("Error:", error);
        clientDatalist.innerHTML = "<option value=''> Error: Unable to fetch client names.</option>";
    });
}

function populateClientDatalist(clients) {
    clientDatalist.innerHTML = ""; // Clear existing options
    clients.forEach(client => {
        const option = document.createElement("option");
        option.value = client; // Datalist uses value, not textContent
        clientDatalist.appendChild(option);
    });
}

document.addEventListener("DOMContentLoaded", fetchClientNames);

