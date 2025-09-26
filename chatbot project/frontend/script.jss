async function sendMessage() {
  let input = document.getElementById("user-input");
  let message = input.value.trim();
  if (!message) return;

  let chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="message user"><b>You:</b> ${message}</div>`;

  let response = await fetch("http://127.0.0.1:8000/agent-chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message })
  });

  let data = await response.json();
  chatBox.innerHTML += `<div class="message bot"><b>Bot:</b> ${data.answer}</div>`;

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}