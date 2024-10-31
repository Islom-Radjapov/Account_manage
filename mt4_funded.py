import pyautogui
print("Start checking")
while True:
    try:
        with open(r"C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\2191F4A3D14D7B4B1EBB84F924777883\MQL4\Files\loss.csv", encoding='utf-16') as file:
            print("file open > ", file.read())
            print("bool > ", file.read() is not None)
            if file is not None:
                print("Change password active")
                pyautogui.click(x=914, y=633)
    except:
        pass
