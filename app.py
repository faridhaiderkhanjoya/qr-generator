from flask import Flask, request, render_template, flash
import qrcode
import os
from datetime import datetime, timedelta
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Required for flash messages

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except:
        return False

def delete_old_qr_images():
    folder = 'static'
    now = datetime.now()
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            if now - file_time > timedelta(seconds=5):
                os.remove(filepath)

@app.route('/', methods=['GET', 'POST'])
def index():
    img_filename = None
    if request.method == 'POST':
        data = request.form['data'].strip()
        if is_valid_url(data):
            delete_old_qr_images()
            if not data.startswith('http'):
                data = 'https://' + data
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            img_filename = f"static/qr_{timestamp}.png"
            img = qrcode.make(data)
            img.save(img_filename)
        else:
            flash("❌ Please enter a valid website URL like https://example.com")
    return render_template('index.html', img_filename=img_filename)

@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


os.makedirs('static', exist_ok=True)

