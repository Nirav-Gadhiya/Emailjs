import requests

def send_email_via_proxy(proxy_url, service_id, template_id, user_id, template_params):
    payload = {
        "service_id": service_id,
        "template_id": template_id,
        "user_id": user_id,
        "template_params": template_params,
    }
    try:
        response = requests.post(proxy_url, json=payload)
        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    PROXY_URL = "http://localhost:3000/send-email"
    SERVICE_ID = "service_u4ljh4s"  # Replace with your EmailJS service ID
    TEMPLATE_ID = "template_upocbdj"  # Replace with your EmailJS template ID
    USER_ID = "UC03U0UrwWCwb79Uz"  # Replace with your EmailJS public key

    # Example data for the email
    TEMPLATE_PARAMS = {
        "to_name": "John Doe",
        "from_name": "Your Name",
        "message": "Hello! This is a test email.",
    }

    send_email_via_proxy(PROXY_URL, SERVICE_ID, TEMPLATE_ID, USER_ID, TEMPLATE_PARAMS)
