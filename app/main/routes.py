from wsgiref.util import request_uri

from flask import render_template, request, send_file, Response
from . import main
from gtts import gTTS
import os
import io


@main.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        text= request.form.get("text")
        action = request.form.get("action")
        tts = gTTS(text=text, lang='en')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        if action == "download":
            return send_file(mp3_fp, as_attachment=True, download_name="speech.mp3", mimetype='audio/mpeg')
        else:  # play
            return send_file(mp3_fp, mimetype='audio/mpeg')
    return render_template("index.html")