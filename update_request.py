import requests
from datetime import datetime


def update(challenge_id):
    update_data = {
        "current_balance": 1000,
        "total_profit_or_lose": -150,
        "balance": 10_000,
        "equity_balance": 1650.50,
        "daily_draw_down": -25.00,
        "max_loss": -150.00,
        "start_date_trade": datetime.now().strftime("%Y-%m-%d"),
        "lasted_for": datetime.now().strftime("%Y-%m-%d"),
    }
    requests.patch(f"https://*.com/api/challenges/{challenge_id}/", json=update_data, headers={"Content-Type": "application/json"})



result = update(1)