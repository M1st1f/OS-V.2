def diary_entry():
    print("Welco to your diary what would like to see?")
    action = int(input("1. see old entries\n2. create new entry \n3.exit \n>>> "))

    if(action == 1):
        print("Old entries")
    elif(action == 2):
        print("creating new entry")
    elif(action == 3):
        print("going back to start")
    else:
        print("invalid action")
