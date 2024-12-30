import requests
from datetime import datetime


def update(challenge_id, current_balance, total_profit_or_lose, balance):
    # API URL
    url = f"https://dreams-funded.com/api/challenges/{challenge_id}/"

    # Headers
    headers = {
        # "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        # Update data
        update_data = {
            "current_balance": current_balance,
            "total_profit_or_lose": total_profit_or_lose,
            "balance": balance,
            "equity_balance": 1650.50,
            "daily_draw_down": -25.00,
            "max_loss": -150.00,
            "start_date_trade": datetime.now().strftime("%Y-%m-%d"),
            "lasted_for": datetime.now().strftime("%Y-%m-%d"),
        }

        # Send PATCH request
        response = requests.patch(url, json=update_data, headers=headers)
        response.raise_for_status()

        print("\nUpdate successful!")
        print("Updated data:", response.json())
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {str(e)}")
        if hasattr(e.response, 'json'):
            print("Error details:", e.response.json())
        return None


CHALLENGE_ID = 1  # o'zingizni challenge ID raqamingiz
result = update(CHALLENGE_ID)
for x, y in result.items():
    print(x, y)