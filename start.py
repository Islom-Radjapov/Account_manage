from auto_login import Change_password
from time import sleep
import csv

email = "yoharo4849@craftapk.com"
pasword = "Asd_1234"
old_password = "0a8YDbX-"
new_password = "ASFAGggsdg323"


while True:
    with open(r'C:\Users\islom\AppData\Roaming\MetaQuotes\Terminal\287469DEA9630EA94D0715D755974F1B\MQL4\Files\daily_loss.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row:
                print(row)
                Change_password(email, pasword, old_password, new_password)
    sleep(3)
    with open(r'C:\Users\islom\AppData\Roaming\MetaQuotes\Terminal\287469DEA9630EA94D0715D755974F1B\MQL4\Files\max_loss.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row:
                print(row)
                Change_password(email, pasword, old_password, new_password)

    sleep(30)
