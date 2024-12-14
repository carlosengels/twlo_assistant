from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a simple text message."""
    # Get the message the user sent
    body = request.form['Body']

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    if body.lower() == 'hello':
        resp.message("Hello!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
