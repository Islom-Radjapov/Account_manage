import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==1.26.4"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "MetaTrader5"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "msal"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
import MetaTrader5 as mt5
import time
import datetime
from datetime import timedelta
from msal import ConfidentialClientApplication
import requests

server = "*"
login = 12345
password = '*'
TO_EMAIL = "*"

def HTML(login, los):
    return f"""
<!DOCTYPE html>
<head>
    <title>Welcome to *</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="text-align: center; margin-top: 20px;">
        <h1>Dear Trader.</h1>
        <h3>
            We regret to inform you that you have violated one of our trading terms, which has resulted in the loss of your challenge. <br/>
            We understand that trading is a complex and ever-changing market, and setbacks are common. Please don't feel discouraged. <br/>
            We encourage you to continue learning and growing as a trader. <br/>
            Account number: {login} <br/>
            Violation: {los} <br/>
            We encourage you to work on your strategy and once you feel comfortable please come back and try us out again! <br/>

        </h3>
    </div>
    <div style="text-align: center; margin-top: 20px;">
        <p>
            Best Regards <br/>
            <b>The * Team</b>
        </p>
    </div>
</body>
</html>
"""



TOKEN = "***"
chat_id = "*"

def get_access_token(client_id, client_secret, tenant_id):
    """
    Authenticate with Azure AD and retrieve an access token.
    """
    # Initialize the Confidential Client Application
    app = ConfidentialClientApplication(
        client_id=client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret,
    )

    # Acquire a token for the Microsoft Graph API
    token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" in token_response:
        return token_response["access_token"]
    else:
        raise Exception(f"Failed to acquire token: {token_response.get('error_description')}")


def send_email(access_token, sender_email, recipient_email, subject, html_content):
    """
    Send an email using Microsoft Graph API with application permissions.
    """
    # Define the Graph API endpoint
    endpoint = f"https://graph.microsoft.com/v1.0/users/{sender_email}/sendMail"


    # Email payload
    email_data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": html_content
            },
            "toRecipients": [
                {"emailAddress": {"address": recipient_email}}
            ],
        },
        "saveToSentItems": "true",
    }

    # Make the HTTP POST request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(endpoint, headers=headers, json=email_data)

    if response.status_code == 202:
        print("Email sent successfully!")
        return True
    else:
        print(f"Failed to send email: {response.status_code}, {response.text}")
        return False

# Replace these with your Azure AD app details and email settings
CLIENT_ID = "***"
CLIENT_SECRET = "***"
TENANT_ID = "***"
SENDER_EMAIL = "***"

def Send(subject, html):
    while True:
        res = send_email(
            access_token=get_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID),
            sender_email=SENDER_EMAIL,
            recipient_email=TO_EMAIL,
            subject=subject,
            html_content=html
        )
        if res:
            break

initialize = mt5.initialize()

mt5.login(login=login, password=password, server=server)

if initialize:
    print('Connected to MetaTrader5')
    print('Login=>', mt5.account_info().login)
    print('Balance=>', mt5.account_info().balance)
    print('Server=>', mt5.account_info().server)

    daily = mt5.account_info().balance - (mt5.account_info().balance * 0.01 * 5)
    max = mt5.account_info().balance - (mt5.account_info().balance * 0.01 * 12)
    old = datetime.datetime.utcnow()
    last_run_time = None
    print("Daily loss=> ", daily)
    print("Max loss=> ", max)

    while True:
        new = datetime.datetime.utcnow()
        if new.day != old.day and new.hour == 0 and new.minute == 1:
            old = datetime.datetime.utcnow()
            daily = mt5.account_info().equity - (mt5.account_info().equity * 0.01 * 5)
            print("New Daily loss=> ", daily)
            message = f"New Daily loss=> {daily}\nTime {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
            url = f"https://api.telegram.org/bot*/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())


        if mt5.account_info().equity < daily:
            message = f"Done Daily loss!\nTime {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            Send("Account Violation - Max Daily Drawdown", HTML(login, "Max Daily Drawdown"))
            print(requests.get(url).json())
            break
        elif mt5.account_info().equity < max:
            message = f"Done Max loss!\nTime {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            Send("Account Violation - Max Drawdown", HTML(login, "Max Drawdown"))
            print(requests.get(url).json())
            break
        if new.weekday() == 6 and new.hour == 0 and new.minute == 1:
            if not last_run_time or (new - last_run_time) >= timedelta(weeks=1):
                last_run_time = new
                orders = 0
                for sym in mt5.symbols_get():
                    orders += len(mt5.positions_get(symbol=sym.name))
                if orders > 0:
                    message = f"Done Weekly opening orders!\nTime {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
                    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                    Send("Account Violation - Weekly opening orders", HTML(login, "Weekly opening orders"))
                    print(requests.get(url).json())
                    break


        time.sleep(0.1)
else:
    print("NO Connected")
