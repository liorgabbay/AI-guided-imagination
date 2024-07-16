from flask import Flask, render_template, send_file
from svc_imagination import generate_guided_imagery

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/generate', methods=['POST'])
def generate():
    return generate_guided_imagery()


@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
