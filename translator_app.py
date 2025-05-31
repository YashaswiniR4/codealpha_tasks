from flask import Flask, request, render_template_string
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    source_text = ""
    if request.method == "POST":
        source_text = request.form["text"]
        dest_lang = request.form["lang"]
        translated = translator.translate(source_text, dest=dest_lang)
        translated_text = translated.text

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Language Translator</title>
        <style>
            body {
                background: #f3f4f6;
                font-family: Arial;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 { color: #333; }
            form {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
                width: 400px;
            }
            textarea, select, button {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                font-size: 16px;
            }
            .output {
                margin-top: 20px;
                background: #e0f7fa;
                padding: 15px;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>🌐 Language Translator</h1>
        <form method="POST">
            <textarea name="text" placeholder="Enter text here..." required>{{source_text}}</textarea>
            <select name="lang">
                <option value="hi">Hindi</option>
                <option value="kn">Kannada</option>
                <option value="ta">Tamil</option>
                <option value="te">Telugu</option>
                <option value="fr">French</option>
                <option value="es">Spanish</option>
            </select>
            <button type="submit">Translate</button>
        </form>
        {% if translated_text %}
        <div class="output">
            <strong>Translated:</strong> {{ translated_text }}
        </div>
        {% endif %}
    </body>
    </html>
    """, translated_text=translated_text, source_text=source_text)

if __name__ == "__main__":
    app.run(debug=True)
