from auto_login import Change_password
import csv

email = "siwanac556@qodiq.com"
pasword = "Asd_1234"
old_password = "32tk2kgVG"
new_password = "ASFAGggsdg323"

with open(r'C:\Users\islom\AppData\Roaming\MetaQuotes\Terminal\287469DEA9630EA94D0715D755974F1B\MQL4\Files\find.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if row:
            Change_password(email, pasword, old_password, new_password)







