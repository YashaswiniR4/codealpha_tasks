from flask import Flask, render_template_string, jsonify
import random
import time

app = Flask(__name__)

# List of public sample MP3 URLs (free, direct links)
PUBLIC_MP3_URLS = [
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
]

generated_music = []

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>🎵 AI Music Generator</title>
<style>
  body {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: center;
    padding: 2rem;
  }
  h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 5px #00000088;
  }
  button {
    background: #ff6a00;
    border: none;
    padding: 1rem 2rem;
    font-size: 1.2rem;
    border-radius: 12px;
    cursor: pointer;
    color: white;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 8px #ff6a0055;
    transition: background 0.3s ease;
  }
  button:hover {
    background: #ff8c38;
  }
  ul {
    list-style-type: none;
    padding: 0;
    max-width: 400px;
    margin: 0 auto;
  }
  li {
    background: #ffffff22;
    margin: 0.6rem 0;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    box-shadow: 0 2px 5px #00000044;
  }
  .play-btn {
    background: #4caf50;
    border: none;
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 2px 5px #2a7a2a88;
  }
  .play-btn:hover {
    background: #66bb6a;
  }
  audio {
    margin-top: 1rem;
    width: 100%;
    max-width: 400px;
    outline: none;
  }
</style>
</head>
<body>
  <h1>🎵 AI Music Generator</h1>
  <button id="generateBtn">Generate Music</button>

  <ul id="musicList"></ul>

  <audio id="audioPlayer" controls></audio>

<script>
  const generateBtn = document.getElementById("generateBtn");
  const musicList = document.getElementById("musicList");
  const audioPlayer = document.getElementById("audioPlayer");

  function refreshList() {
    fetch("/list")
      .then(res => res.json())
      .then(data => {
        musicList.innerHTML = "";
        data.music.forEach((m, i) => {
          const li = document.createElement("li");
          li.textContent = m;
          const playBtn = document.createElement("button");
          playBtn.textContent = "Play";
          playBtn.className = "play-btn";
          playBtn.onclick = () => playMusic(m);
          li.appendChild(playBtn);
          musicList.appendChild(li);
        });
      });
  }

  // On Play: get a remote mp3 url and play it directly
  function playMusic(name) {
    fetch("/play")
      .then(res => res.json())
      .then(data => {
        audioPlayer.src = data.url;
        audioPlayer.play();
      });
  }

  generateBtn.onclick = () => {
    fetch("/generate")
      .then(res => res.json())
      .then(data => {
        alert(data.message);
        refreshList();
      });
  };

  refreshList();
</script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/generate')
def generate():
    new_music_name = f"Music {len(generated_music) + 1} generated at {time.strftime('%H:%M:%S')}"
    generated_music.clear()
    generated_music.append(new_music_name)
    return jsonify({"message": f"🎵 {new_music_name}!"})

@app.route('/list')
def list_music():
    return jsonify({"music": generated_music})

@app.route('/play')
def play():
    chosen_url = random.choice(PUBLIC_MP3_URLS)
    return jsonify({"url": chosen_url})

if __name__ == "__main__":
    print("Running AI Music Generator - using public MP3 URLs")
    app.run(debug=True)
