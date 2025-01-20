from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    emailjs_url = "https://api.emailjs.com/api/v1.0/email/send"
    try:
        response = requests.post(emailjs_url, json=data)
        return jsonify({"status": response.status_code, "response": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000)
