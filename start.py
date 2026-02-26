import MetaTrader5 as mt5
from _datetime import datetime
login = 123456
password = "*"
server = '*'

initialize = mt5.initialize()
mt5.login(login=login, password=password, server=server)
if initialize:
    print('Connected to MetaTrader5')
    print('Login=>', mt5.account_info().login)
    print('Balance=>', mt5.account_info().balance)
    print('Server=>', mt5.account_info().server)


    while True:
        positions = mt5.positions_get(symbol="EURUSDp")
        print("Account Size ", positions[0])
        close_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": "EURUSDp",
            "volume": 1.0,
            "type": 1,
            "position": positions[0].ticket,
            "price": mt5.symbol_info_tick("EURUSDp").bid,
            "deviation": 10,
            "magic": 0,
            "comment": "",
            "type_time": mt5.ORDER_TIME_GTC,  # good till cancelled
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        # send a close request
        result = mt5.order_send(close_request)
        #tick = mt5.symbol_info_tick("EURUSDp").bid
        print("result", result, "    ", mt5.last_error())
        break


else:
    print("NO Connected")
