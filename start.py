from auto_login import Change_password
from generate_password import generate_password
from time import sleep
import psutil

# Close MetaTrader using the process name
def close_MT5():
    for proc in psutil.process_iter():
        try:
            print(proc)
            # Check if process name matches MetaTrader
            if proc.name() == "terminal64.exe":  # This is the name for both MT4 and MT5
                proc.terminate()  # or proc.kill() for a forced termination
                print("MetaTrader closed successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass



email = "wofes94415@advitize.com"
pasword = "Asd_1234"
old_password = "ASsdg4e5h_dEDF"
new_password =  "asasgaggd" #generate_password(11)
Change_password(email, pasword, old_password, new_password)


print("Start checking")

while True:
    try:
        with open("\loss.csv", encoding='utf-16') as file:
            print("file open > ", file.read())
            print("bool > ", file.read() is not None)
            if file is not None:
                print("Change password active")
                close_MT5()
                Change_password(email, pasword, old_password, new_password)
    except:
        pass
    sleep(15)

