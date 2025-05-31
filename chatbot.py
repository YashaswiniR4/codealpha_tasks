from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

qa_pairs = {
    "hi": "Hello! How can I assist you today? 😊",
    "i am happy":"ho what is the reason",
    "hello": "Hi there! What can I do for you? 😊",
    "what is ai": "AI stands for Artificial Intelligence — machines mimicking human intelligence.",
    "how are you": "I'm just code, but thanks for asking! How about you?",
    "bye": "Goodbye! Have a great day! 👋",
    "what is python": "Python is a versatile, easy-to-learn programming language.",
    "what is flask": "Flask is a lightweight Python web framework used to build web apps.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
    "who created you": "I was created by a helpful developer using Python and Flask.",
    "what is machine learning": "Machine learning lets computers learn patterns from data to make predictions.",
    "what is deep learning": "Deep learning is a subset of machine learning using neural networks with many layers.",
    "what is chatbot": "A chatbot is a computer program that can simulate conversation with users.",
    "can you help me": "Absolutely! Ask me anything you want.",
    "what time is it": "Sorry, I can't tell time yet. But you can check your device clock!",
    "thank you": "You're welcome! 😊",
    "how do i learn programming": "Start with basics like Python and practice coding regularly.",
    "what is the weather": "I don't have weather info, but you can check your local forecast online!",
    "who won the football match": "I don't have live sports updates yet.",
    "can you speak other languages": "I understand English, but I can learn more soon!",
    "default": "Sorry, I didn't understand that. Could you please rephrase?"
}

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Smart Chatbot - Dark Multi-Color</title>
<style>
  html, body {
    height: 100%;
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg,
      #ff007f,  /* pink */
      #ff2400,  /* red */
      #4b0082,  /* purple */
      #0000ff,  /* blue */
      #8a2be2   /* violet */
    );
    background-size: 400% 400%;
    animation: colorShift 25s ease infinite;
    color: #eee;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  @keyframes colorShift {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
  }
  #chatbox {
    background: rgba(20,20,20,0.85);
    width: 95vw;
    max-width: 700px;
    height: 85vh;
    border-radius: 25px;
    box-shadow: 0 0 30px 8px rgba(255, 36, 90, 0.8);
    display: flex;
    flex-direction: column;
    border: 3px solid #ff007f;
  }
  #messages {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    border-bottom: 2px solid #8a2be2;
  }
  .message {
    max-width: 70%;
    margin: 10px 0;
    padding: 14px 20px;
    border-radius: 25px;
    font-size: 1.15rem;
    line-height: 1.4;
    word-wrap: break-word;
    clear: both;
  }
  .user {
    background: linear-gradient(45deg, #ff007f, #ff2400);
    color: #fff;
    float: right;
    box-shadow: 0 4px 15px rgba(255, 36, 0, 0.6);
    border-bottom-right-radius: 5px;
  }
  .bot {
    background: linear-gradient(45deg, #4b0082, #0000ff, #8a2be2);
    color: #fff;
    float: left;
    box-shadow: 0 4px 15px rgba(72, 61, 139, 0.6);
    border-bottom-left-radius: 5px;
  }
  #inputArea {
    display: flex;
    padding: 15px 25px;
    background: #111;
    border-radius: 0 0 25px 25px;
    border-top: 2px solid #8a2be2;
  }
  #userInput {
    flex: 1;
    padding: 15px 25px;
    font-size: 1.2rem;
    border-radius: 30px;
    border: 2px solid #ff2400;
    background: #222;
    color: #eee;
    outline: none;
    transition: border-color 0.3s ease;
  }
  #userInput:focus {
    border-color: #8a2be2;
  }
  #sendBtn {
    margin-left: 20px;
    background: #ff007f;
    border: none;
    color: #fff;
    padding: 15px 35px;
    border-radius: 30px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 6px 18px rgba(255, 0, 127, 0.7);
    transition: background-color 0.3s ease;
  }
  #sendBtn:hover {
    background: #d6006c;
  }
  #messages::-webkit-scrollbar {
    width: 10px;
  }
  #messages::-webkit-scrollbar-track {
    background: #111;
  }
  #messages::-webkit-scrollbar-thumb {
    background: #ff007f;
    border-radius: 15px;
  }
</style>
</head>
<body>
  <div id="chatbox" role="main" aria-label="Chatbot conversation">
    <div id="messages" aria-live="polite" aria-relevant="additions"></div>
    <form id="inputArea" onsubmit="sendMessage(event)" aria-label="Chat input form">
      <input id="userInput" autocomplete="off" placeholder="Ask me anything..." aria-label="Message input" required />
      <button type="submit" id="sendBtn" aria-label="Send message">Send</button>
    </form>
  </div>

<script>
  const messagesDiv = document.getElementById("messages");
  const userInput = document.getElementById("userInput");

  function addMessage(text, sender) {
    const div = document.createElement("div");
    div.textContent = text;
    div.classList.add("message", sender);
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  }

  async function sendMessage(e) {
    e.preventDefault();
    const msg = userInput.value.trim();
    if (!msg) return;
    addMessage(msg, "user");
    userInput.value = "";
    const response = await fetch("/get_response", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message: msg})
    });
    const data = await response.json();
    addMessage(data.reply, "bot");
  }

  addMessage("Hi! Ask me anything about AI, tech, programming, or more. 😊", "bot");
</script>
</body>
</html>
    """)

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_msg = data.get("message", "").lower().strip()
    reply = qa_pairs.get(user_msg, qa_pairs["default"])
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
