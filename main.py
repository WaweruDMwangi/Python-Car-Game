# CAR GAME

guess = 0

while guess < 40:
    user_input = input("> ")
    guess += 1

    if user_input.lower() == 'help':
        print('''
        Start -to start the car
        Stop - to stop the car
        quit - to exit
        ''')
    elif user_input.lower() == 'start':
        print("Car started...Ready to go!!!")
    elif user_input.lower() == 'stop':
        print("Car stopped.")
    elif user_input.lower() == 'quit':
        print("Quitting...")
        break
    elif guess == 4:
        print("Sorry, you finished your attempts!!!")
    else:
        print("I don't understand that...")
