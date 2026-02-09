from flask import Flask, request, render_template, flash, send_file
import qrcode
import os
from datetime import datetime, timedelta
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = "mysecretkey"


def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except:
        return False


def delete_old_qr_images():
    folder = os.path.join(app.root_path, "static")
    now = datetime.now()
    if not os.path.exists(folder):
        return
    for filename in os.listdir(folder):
        if filename.startswith("qr_") and filename.endswith(".png"):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                if now - file_time > timedelta(minutes=5):
                    os.remove(filepath)


@app.route("/", methods=["GET", "POST"])
def index():
    img_filename = None
    if request.method == "POST":
        data = request.form.get("data", "").strip()
        if is_valid_url(data):
            delete_old_qr_images()
            if not data.startswith("http"):
                data = "https://" + data
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            img_filename = f"static/qr_{timestamp}.png"
            img_path = os.path.join(app.root_path, img_filename)
            img = qrcode.make(data)
            img.save(img_path)
        else:
            flash("❌ Please enter a valid website URL like https://example.com")
    return render_template("index.html", img_filename=img_filename)


@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# 🔥 FINAL GUARANTEED SITEMAP FIX
@app.route("/sitemap.xml")
def sitemap():
    sitemap_path = os.path.join(app.root_path, "static", "sitemap.xml")
    return send_file(sitemap_path, mimetype="application/xml")


# Ensure static folder exists (safe for Render)
os.makedirs(os.path.join(app.root_path, "static"), exist_ok=True)

