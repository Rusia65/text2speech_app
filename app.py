# Flask Web App for Text-to-Speech using gTTS
from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        lang = request.form.get("lang", "en")
        filename = "output.mp3"

        if text:
            try:
                tts = gTTS(text=text, lang=lang)
                tts.save(filename)
                return send_file(filename, as_attachment=True)
            except Exception as e:
                return f"<h3>Error: {e}</h3>"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
