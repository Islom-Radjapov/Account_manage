import MetaTrader5 as mt5
from datetime import datetime, timedelta
import pandas as pd
login = 572534
password = "-cXiW7Rm"
server = 'BlueWhaleMarkets-Server'
TO_EMAIL = "islom.radjapov.1997@mail.ru"

def get_profit_loss():
    result = 0
    if mt5.account_info().equity > balance:
        result = mt5.account_info().equity - balance
    elif mt5.account_info().equity < balance:
        result = -(balance - mt5.account_info().equity)
    return result

def get_equlity_profit_loss():
    result = 0
    if mt5.account_info().equity > balance:
        result = mt5.account_info().equity - balance
    elif mt5.account_info().equity < balance:
        result = -(balance - mt5.account_info().equity)
    return result

def get_balance():
    result = 0
    if mt5.account_info().balance > balance:
        result = mt5.account_info().balance - balance
    elif mt5.account_info().balance < balance:
        result = -(balance - mt5.account_info().balance)
    return result


def get_last_trade():
    a = mt5.history_deals_get(datetime.now() - timedelta(days=365), datetime.now() + timedelta(days=1))
    b = [x for x in a if x.profit != 0][-1]
    d = mt5.history_deals_get(position=b.position_id)[1]
    return datetime.fromtimestamp(d.time)

def get_first_trade():
    a = mt5.history_deals_get(datetime.now() - timedelta(days=365), datetime.now() + timedelta(days=1))
    b = [x for x in a if x.profit != 0][1]
    d = mt5.history_deals_get(position=b.position_id)[0]
    return datetime.fromtimestamp(d.time)

initialize = mt5.initialize()
mt5.login(login=login, password=password, server=server)
if initialize:

    print('Connected to MetaTrader5')
    print('Login=>', mt5.account_info().login)
    print('Balance=>', mt5.account_info().balance)
    print('Server=>', mt5.account_info().server)


    balance = 10_000
    print("Account Size ", balance)

    while True:

        print("Account Status ", "Activate", "Daily loss incurred", "Max loss incurred", "Weekly opening order incurred")

        print("Days Traded ", (datetime.now() - get_first_trade()).days)
        print("Total Profit/Loss ", get_profit_loss())

        # chart
        print("Balance ", mt5.account_info().balance)
        print("EQUITY BALANCE ", mt5.account_info().equity)

        # Account Details
        print("Server ", mt5.account_info().server)
        print("Account Type ", "challange", "funded")
        print("Login  ", mt5.account_info().login)
        print("Starting Balance ", balance)
        print("Current Balance ", mt5.account_info().balance)

        #Goal Meter
        print("Daily Drawdown ", )
        print("Max Loss ", )
        print("Your Funded Program Lasted For ", datetime.now() - get_first_trade() )
        update_data = {
            "current_balance": mt5.account_info().balance,
            "total_profit_or_lose": get_profit_loss(),
            "balance": mt5.account_info().balance,
            "equity_balance": mt5.account_info().equity,
            "daily_draw_down": -25.00,
            "max_loss": -150.00,
            "start_date_trade": datetime.now().strftime("%Y-%m-%d"),
            "lasted_for": datetime.now().strftime("%Y-%m-%d"),
        }
        break

else:
    print("NO Connected")
