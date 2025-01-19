from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def home():
    return render_template("index.html")  # Ganti dengan file HTML Anda

if __name__ == "__main__":
    app.run(debug=True)
