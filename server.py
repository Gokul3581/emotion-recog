from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-opencv', methods=['GET','POST'])
def start_face_detection():
    subprocess.Popen(["py", "-3.10", "emotion_face.py"])
    return redirect(url_for('index'))

@app.route('/open-gradio')
def open_gradio():
    return redirect("https://f46f657adc2f8c609c.gradio.live/")

if __name__ == '__main__':
    app.run(debug=True)
