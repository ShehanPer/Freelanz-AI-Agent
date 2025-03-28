chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'chat') {
      fetch('http://localhost:5000/chat', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: request.message }),
      })
          .then((response) => response.json())
          .then((data) => sendResponse(data))
          .catch((error) => console.error(error));
      return true; // Keeps the channel open for async response
  }
});
