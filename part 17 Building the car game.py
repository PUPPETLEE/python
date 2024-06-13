comand = ''
started = False

while True:
    command = input(">").lower()
    if command.__eq__("start"):
        if started:
            print("Car is Already started")
        else:
            started = True
            print("Car started Ready to go")
    elif command.__eq__("stop"):
        if not started:
            print("Car is Already stoped")
        else:
            started = False
            print("Car Stoped")
    elif command.__eq__("quit"):
        break
    else:
        print("i don't understand that...")





