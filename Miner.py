import webbrowser
import time

wal = input("Type your Name here: ")

print("Hello " + wal)

chose = input("1.BTC, 2.ETH: ")

if chose == "1":
    webbrowser.open("https://www.google.com/search?q=bitcoin&rlz=1C1BNSD_enGE1032GE1032&oq=bitcoin&aqs=chrome..69i57j0i67i433j0i67i131i433j0i67l3j0i67i131i433j0i67j0i512l2.7091j1j7&sourceid=chrome&ie=UTF-8")
    i = 0
    while i < 248384573:
        print("Mining BTC: 0.00000")
        i + 1
        time.sleep(3)
        while i > 200:
            print("Mining BTC: 0.00001")
            i + 1
            time.sleep(3)
if chose == "2":
    webbrowser.open("https://www.google.com/search?q=Etherium&rlz=1C1BNSD_enGE1032GE1032&oq=Etherium&aqs=chrome..69i57j0i10i67j0i10i433i512j0i10i131i433i512j0i10i512l4j46i10i512j0i10i512.5016j1j9&sourceid=chrome&ie=UTF-8")
    i = 0
    while i < 200:
        print("Mining ETH: 0.00000")
        i + 1
        time.sleep(3)
        while i > 200:
            print("Mining ETH: 0.00001")
            i + 1
            time.sleep(3)
            