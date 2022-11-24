# Car Game
command = ""
started = False

while command != "quit":
    command = input("Ready? ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print('''
            start - to start car.
            stop - to stop car.
            quit - to end game.
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand, type help for more.")
