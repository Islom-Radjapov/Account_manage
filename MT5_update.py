import subprocess
import sys

from A import balance

subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==1.26.4"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "MetaTrader5"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "msal"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
import MetaTrader5 as mt5
import time
from datetime import datetime, timedelta
from msal import ConfidentialClientApplication
import requests

login = 576500
password = "HzS-Dz2o"
server = 'BlueWhaleMarkets-Server'
TO_EMAIL = "islom.radjapov.1997@mail.ru"
challenge_id = 2
typee = 1# 0-challange 1-funded 3-daily send
def HTML(login, los):
    return f"""
<!DOCTYPE html>
<head>
    <title>Welcome to Dreams Funded</title>
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
            <b>The Dreams Funded Team</b>
        </p>
    </div>
</body>
</html>
"""



TOKEN = "7681078661:AAFa53g5UjVga17KFHI1vJV0GxugrLeM08M"
chat_id = "529408795"

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
CLIENT_ID = "efa87325-5a82-48be-b463-3f50ba0ed6ec"
CLIENT_SECRET = "2dg8Q~FnSeiC.dToAWXedvVEc2go5C60eWUMCdhK"
TENANT_ID = "619ef93b-584c-4cb7-b9c9-1946e5da30d2"
SENDER_EMAIL = "support@dreams-funded.com"

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


def get_profit_loss(balancee):
    result = 0
    if mt5.account_info().equity > balancee:
        result = mt5.account_info().equity - balancee
    elif mt5.account_info().equity < balancee:
        result = -(balancee - mt5.account_info().equity)
    return result

def get_equlity_profit_loss(balancee):
    result = 0
    if mt5.account_info().equity > balancee:
        result = mt5.account_info().equity - balancee
    elif mt5.account_info().equity < balancee:
        result = -(balancee - mt5.account_info().equity)
    return result

def get_balance(balancee):
    result = 0
    if mt5.account_info().balance > balancee:
        result = mt5.account_info().balance - balancee
    elif mt5.account_info().balance < balancee:
        result = -(balancee - mt5.account_info().balance)
    return result

def get_last_trade():
    try:
        a = mt5.history_deals_get(datetime.now() - timedelta(days=365), datetime.now() + timedelta(days=1))
        b = [x for x in a if x.profit != 0][-1]
        d = mt5.history_deals_get(position=b.position_id)[1]
        return datetime.fromtimestamp(d.time)
    except:
        return datetime.utcnow()

def get_first_trade():
    a = mt5.history_deals_get(datetime.now() - timedelta(days=365), datetime.now() + timedelta(days=1))
    b = [x for x in a if x.profit != 0][1]
    d = mt5.history_deals_get(position=b.position_id)[0]
    return datetime.fromtimestamp(d.time)

def get_drowdown_max(loss):
    result = 0
    if mt5.account_info().equity > loss:
        result = mt5.account_info().equity - loss
    return mt5.account_info().equity - loss

def get_profit_target(balancee):
    result = 0
    if mt5.account_info().equity > balancee:
        result = mt5.account_info().equity - balancee
    return result

def get_profit(balancee):
    result = 0
    if mt5.account_info().balance > balancee:
        result = mt5.account_info().balance - balancee
    return result

def update(balanee, status, daily1, max1):
    if typee == 0: # challange
        update_data = {
        "account_status": status,
        "total_profit_or_lose": get_profit_loss(balanee),
        "current_balance": mt5.account_info().balance,
        "daily_draw_down_max": get_drowdown(daily1),
        #"daily_draw_down_current": get_drowdown(daily1),
        #"max_loss_max": max1,
        "max_loss_current": get_drowdown(max1),
        #"profit_target_max": profit,
        "profit_target_current": get_profit_target(balanee),
        #"profit": get_profit(balanc),
        #"lasted_for": get_first_trade()
        }
    elif typee == 1: # funded
        update_data = {
            "account_status": status,
            "total_profit_or_lose": get_profit_loss(balanee),
            "current_balance": mt5.account_info().balance,
            #"daily_draw_down_max": daily1,
            "daily_draw_down_current": get_drowdown(daily1),
            #"max_loss_max": max1,
            "max_loss_current": get_drowdown(max1),
            #"profit_target_max": profit,
            #"profit_target_current": get_profit_target(balanee),
            'profit': get_profit(balanee),
            #"lasted_for": get_first_trade()
        }
    else:
        update_data = {
            #"account_status": status,
            #"total_profit_or_lose": get_profit_loss(balanc),
            #"current_balance": mt5.account_info().balance,
            "daily_draw_down_max": daily,
            "daily_draw_down_current": get_drowdown(daily),
            "max_loss_max": max,
            "max_loss_current": get_drowdown(max),
            "profit_target_max": profit,
            "profit_target_current": get_profit_target(balanc),
            #'profit': get_profit(balanc),
            "lasted_for": get_first_trade()
        }

    requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                   headers={"Content-Type": "application/json"})

initialize = mt5.initialize()

mt5.login(login=login, password=password, server=server)

if initialize:
    print('Connected to MetaTrader5')
    print('Login=>', mt5.account_info().login)
    balanc =  mt5.account_info().balance
    print('Balance=>', balanc)
    print('Server=>', mt5.account_info().server)

    daily = mt5.account_info().balance - (mt5.account_info().balance * 0.01 * 5)
    max = mt5.account_info().balance - (mt5.account_info().balance * 0.01 * 12)
    profit = mt5.account_info().balance * 0.01 * 8
    old = datetime.utcnow()
    last_run_time = None
    update_time = datetime.utcnow()
    print("Daily loss=> ", daily)
    print("Max loss=> ", max)

    update_data = {
        "account_status": "active",
        "total_profit_or_lose": get_profit_loss(balanc),
        "current_balance": mt5.account_info().balance,
        "daily_draw_down_max": balanc - daily,
        "daily_draw_down_current": get_drowdown(daily),
        "max_loss_max": balanc - max,
        "max_loss_current": get_drowdown(max),
        "profit_target_max": profit,
        "profit_target_current": get_profit_target(balanc),
        'profit': 0,
        "lasted_for": 0
    }
    requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                   headers={"Content-Type": "application/json"})

    while True:
        new = datetime.utcnow()
        if new.day != old.day and new.hour == 0 and new.minute == 1:
            old = datetime.utcnow()
            daily = mt5.account_info().equity - (mt5.account_info().equity * 0.01 * 5)
            update_data = {
                # "account_status": status,
                # "total_profit_or_lose": get_profit_loss(balanc),
                # "current_balance": mt5.account_info().balance,
                "daily_draw_down_max": daily,
                "daily_draw_down_current": get_drowdown(daily),
                "max_loss_max": max,
                "max_loss_current": get_drowdown(max),
                "profit_target_max": profit,
                "profit_target_current": get_profit_target(balanc),
                # 'profit': get_profit(balanc),
                "lasted_for": get_first_trade()
            }
            requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                           headers={"Content-Type": "application/json"})
            print("New Daily loss=> ", daily)
            message = f"New Daily loss=> {daily}\nTime {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
            url = f"https://api.telegram.org/bot7587623547:AAE_AIFaFF2UF3-Et-HRs09nJgZgHYeaSUc/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())


        if mt5.account_info().equity < daily:
            update_data = {
                "account_status": "Daily loss",
                "total_profit_or_lose": get_profit_loss(balanc),
                "current_balance": mt5.account_info().balance,
                "daily_draw_down_max": daily,
                "daily_draw_down_current": get_drowdown(daily),
                "max_loss_max": max,
                "max_loss_current": max,
                #"profit_target_max": profit,
                #"profit_target_current": get_profit_target(balanc),
                #'profit': 0,
                #"lasted_for": 0
            }
            requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                           headers={"Content-Type": "application/json"})
            message = f"Done Daily loss!\nTime {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            Send("Account Violation - Max Daily Drawdown", HTML(login, "Max Daily Drawdown"))
            print(requests.get(url).json())
            break
        elif mt5.account_info().equity < max:
            update_data = {
                "account_status": "Max loss",
                "total_profit_or_lose": get_profit_loss(balanc),
                "current_balance": mt5.account_info().balance,
                "daily_draw_down_max": daily,
                "daily_draw_down_current": daily,
                "max_loss_max": max,
                "max_loss_current": get_drowdown(max),
                # "profit_target_max": profit,
                # "profit_target_current": get_profit_target(balanc),
                # 'profit': 0,
                # "lasted_for": 0
            }
            requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                           headers={"Content-Type": "application/json"})
            message = f"Done Max loss!\nTime {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
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
                    update_data = {
                        "account_status": "Weekly opening orders",
                        #"total_profit_or_lose": get_profit_loss(balanc),
                        #"current_balance": mt5.account_info().balance,
                        #"daily_draw_down_max": daily,
                        #"daily_draw_down_current": get_drowdown(daily),
                        #"max_loss_max": max,
                        #"max_loss_current": get_drowdown(max),
                        # "profit_target_max": profit,
                        # "profit_target_current": get_profit_target(balanc),
                        # 'profit': 0,
                        # "lasted_for": 0
                    }
                    requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                                   headers={"Content-Type": "application/json"})
                    message = f"Done Weekly opening orders!\nTime {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
                    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                    Send("Account Violation - Weekly opening orders", HTML(login, "Weekly opening orders"))
                    print(requests.get(url).json())
                    break
        if mt5.positions_total() == 0:
            if get_last_trade() + timedelta(days=29) < new:
                update_data = {
                    "account_status": "30 days of inactivity",
                    # "total_profit_or_lose": get_profit_loss(balanc),
                    # "current_balance": mt5.account_info().balance,
                    # "daily_draw_down_max": daily,
                    # "daily_draw_down_current": get_drowdown(daily),
                    # "max_loss_max": max,
                    # "max_loss_current": get_drowdown(max),
                    # "profit_target_max": profit,
                    # "profit_target_current": get_profit_target(balanc),
                    # 'profit': 0,
                    # "lasted_for": 0
                }
                requests.patch(f"https://dreams-funded.com/api/challenges/{challenge_id}/", json=update_data,
                               headers={"Content-Type": "application/json"})
                message = f"Done 30 days of inactivity!\nTime {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\nName {mt5.account_info().name}\nLogin {mt5.account_info().login}"
                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                Send("Account Violation - 30 days of inactivity", HTML(login, "30 days of inactivity"))
                print(requests.get(url).json())
                break


        if update_time + timedelta(seconds=10) < datetime.utcnow():
            update(balanc, "Activate", daily, max)
        time.sleep(0.1)
else:
    print("NO Connected")
