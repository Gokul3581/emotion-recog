from flask import Flask, render_template, redirect, url_for
import subprocess
import os
import sys


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-opencv', methods=['GET','POST'])
def start_face_detection():
    # subprocess.Popen(["py", "-3.10", "emotion_face.py"])
    subprocess.Popen([sys.executable, "emotion_face.py"])


    return redirect(url_for('index'))

@app.route('/open-gradio')
def open_gradio():
    return redirect("https://huggingface.co/spaces/gokul968/emotion-detection")

@app.route("/debug-version")
def debug_version():
    import sys
    return f"Python Version: {sys.version}"


if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
