from flask import Flask, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# SMTP config - replace with your details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_EMAIL = 'rancao20060623@gmail.com'
SMTP_PASSWORD = 'kinx kare ywof cptl'  # Use app password if 2FA is enabled

# Route to serve main page
@app.route('/')
def main():
    # Redirect to static main.html
    return redirect('/static/main.html')

# Route to serve contact page
@app.route('/contact')
def contact():
    # Redirect to static contact.html
    return redirect('/static/contact.html')

# Route to handle form POST from contact page
@app.route('/send', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return "Please fill all fields", 400

    # Compose email
    email_message = EmailMessage()
    email_message['Subject'] = f'New Contact Form Submission from {name}'
    email_message['From'] = SMTP_EMAIL
    email_message['To'] = SMTP_EMAIL
    email_message.set_content(f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}')

    # Send email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
            smtp.send_message(email_message)
        # Redirect back to contact page with success message
        return redirect('/contact')
    except Exception as e:
        return f"Failed to send email: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)