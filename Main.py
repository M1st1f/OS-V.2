import os
from calculator import Callculator
from Diary import diary_entry

def cleaning():
    os.system("cls")

print("  /$$$$$$   /$$$$$$        /$$    /$$  /$$$$$$ \n /$$__  $$ /$$__  $$      | $$   | $$ /$$__  $$\n| $$  \ $$| $$  \__/      | $$   | $$|__/  \ $$\n| $$  | $$|  $$$$$$       |  $$ / $$/  /$$$$$$/\n| $$  | $$ \____  $$       \  $$ $$/  /$$____/ \n| $$  | $$ /$$  \ $$        \  $$$/  | $$      \n|  $$$$$$/|  $$$$$$/         \  $//$$| $$$$$$$$\n \______/  \______/           \_/|__/|________/")

print("welcome, What whould you like to open?")
print("1.Calculater \n2.Diary \n3.webbrowser \n4.exit")

choose = int(input(">>> "))

#
#Call programs
#
# TODO: loop program util choose is == 4
if(choose == 1):
    cleaning()
    Callculator()
    # TODO: how do I call back?
elif(choose == 2):
    # TODO: Create a freaking Diary, How?
    cleaning()
    diary_entry()
elif(choose == 3):
    ## TODO: Had already make this, just copy and paste
    cleaning()
elif(choose == 4):
    SystemExit
else:
    print("invalid text")
