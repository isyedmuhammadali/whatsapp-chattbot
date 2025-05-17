from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.form.get('Body').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['1', 'about me']:
        msg.body("👤 About Me:\nI am Syed Muhammad Ali, a Computer Scientist passionate about software development and AI.")
    elif incoming_msg in ['2', 'skills']:
        msg.body("🛠 Skills:\n- Python\n- Java\n- Android Development\n- Machine Learning\n- Chatbot Development")
    elif incoming_msg in ['3', 'projects']:
        msg.body("📁 Projects:\n1. WhatsApp Chatbot\n2. Android Login App\n3. Machine Learning Classifier\n(…more coming!)")
    elif incoming_msg in ['4', 'contact']:
        msg.body("📞 Contact:\nEmail: syed@example.com\nPhone: +92-XXX-XXXXXXX")
    else:
        msg.body(
            "Syed Muhammad Ali – Computer Scientist 👨‍💻\n\n"
            "Please choose an option:\n"
            "1. About Me\n"
            "2. Skills\n"
            "3. Projects\n"
            "4. Contact"
        )

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
