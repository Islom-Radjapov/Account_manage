import MetaTrader5 as mt5
from _datetime import datetime
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

initialize = mt5.initialize()
mt5.login(login=login, password=password, server=server)
if initialize:
    print('Connected to MetaTrader5')
    print('Login=>', mt5.account_info().login)
    print('Balance=>', mt5.account_info().balance)
    print('Server=>', mt5.account_info().server)

    balance = mt5.account_info().balance
    print("Account Size ", balance)

    while True:

        print("Account Status ", "Activate", "Daily loss incurred", "Max loss incurred", "Weekly opening order incurred")
        orders = 0
        for sym in mt5.symbols_get():
            orders += len(mt5.positions_get(symbol=sym.name))
        if orders > 0:
            print("Days Traded ", + 1)
        print("Total Profit/Loss ", get_profit_loss())

        print("Balance ", balance - mt5.account_info().balance)
        print("Account Size ", mt5.account_info().equity)


else:
    print("NO Connected")
