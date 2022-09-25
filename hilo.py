# ***Beginning of program***
while True:
    # A random number should be entered here.
    import random
# Greeting the user.
    print("Hello, What is your name?")
    name = input()
# The user will pick how big they want the number to be.
# If the user inputs anything else than a number it will
# come back invalid and keep asking "What should be the
# maximum number be?: " until it receives a number
    flag = True
    while flag:
     num = input("What should be the maximum number be?: ")
# If the input is a number it will proceed.
    if num.isdigit():
     print("Alright!", name, "Let's play!")
     num = int(num)
     flag = False
else:
    print("Invalid input! Try again.")

# Now the random number will be generated here
# out of how big of a number the user picked.
    ans = random.randint(1, num)
    guess = None
# Here is where the user inputs their guesses.
# If the number they guess is low it will come out "Guess is to low"
# If guess is high it will come to "Guess is to high"
# If the guess they enter is correct it will say "Congratulations! *users name
# Else the user will keep getting please try again until the number is correct.
while guess != ans:
    guess = input("Please type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
     guess = int(guess)
    if guess < ans:
     print("Guess is to low")
    if guess > ans:
     print("Guess is to high")
    elif guess == ans:
     print("Congratulations!", name, "you got it!")
    else:
        # Now that the user has guessed the correct answer they have the option to
        # Play again if the user types yes/Yes they will run therought the beginning.
        # If the user types no/No they will exit the code and receive a message
        # "Ok thank you for playing *users name* have a nice day!"
        # Then the program will break.
        
     print("Please try again!")
    restart = input("Do you want to play again?") .lower()
    if restart == ("yes"):
     continue
    else:
     print("Ok thank you for playing", name, "have a nice day!")
    break
# ***End of program***
