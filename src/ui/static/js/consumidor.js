window.addEventListener("DOMContentLoaded", () => {
  const messages = document.getElementById("mensajes");

  if(typeof(EventSource) !== "undefined") {
    var source = new EventSource("https://8003-misw4406-tutorial9bff-cgv6a3r2t9h.ws-eu86.gitpod.io/stream");
    source.onmessage = function(event) {
      const message = document.createElement("li");
      const content = document.createTextNode(event.data);
      message.appendChild(content);
      messages.appendChild(message);
    }
  }
});