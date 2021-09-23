print()

command = ""
started = False
stopped = True 

while True:
    command = input(">  ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:  
            started = True
            print("The Car Started")
            print()
    elif command == "stop":
        if not started : 
            print("Car already stopped")
        else:
            started = False    
            print("The Car Stopped")
            print()
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - quit
        ''')
        print()
    elif command == "quit":
        break
    else:
        print("Sorry wrong input")

