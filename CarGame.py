command = ""
Started = ""
while True:
    command = input("Choose one from start,stop, help and quit: ").lower()
    if command == "start":
        if Started:
            print("Its already ON!")
        else:
            print("Car has started!")
            Started = True
    elif command == "stop":
        if Started:
            print("Car has stopped!")
            Started = False
        else:
            print("It's OFF already!")
    elif command == "quit":
        print("See you again!")
        break
    else:
        print("Please choose correctly!!!")
        status = input("Choose one from start,stop, help and quit: ").lower()




