import os
import sys
from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key'

# Gunakan threading untuk menghindari fcntl
socketio = SocketIO(app, async_mode="threading")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_camera')
def set_camera():
    """Mengatur URL kamera"""
    session['url'] = '0'  # Default URL kamera perangkat
    return redirect(url_for('index'))

@app.route('/set_youtube', methods=['POST'])
def set_youtube():
    """Mengatur URL YouTube"""
    youtube_url = request.form.get('youtube_url')
    if youtube_url:
        session['url'] = youtube_url  # Simpan URL di session
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Menggunakan 8080 sebagai fallback
    app.run(host='0.0.0.0', port=port)
