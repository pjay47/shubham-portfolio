from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        full_message = f"New message from {name} <{email}>:\n\n{message}"

        send_email("jpatel4224@gmail.com", full_message)
        # Pass a flag to show the success message and trigger redirect
        return render_template("contact.html", success=True, redirect_home=True)

    return render_template("contact.html", success=False, redirect_home=False)

def send_email(to_email, body):
    sender_email = "jpatel4224@gmail.com"       # Replace
    sender_password = "zxxqtcyxtwmxbnwa"           # Replace

    msg = MIMEText(body)
    msg["Subject"] = "New Contact Message"
    msg["From"] = sender_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
