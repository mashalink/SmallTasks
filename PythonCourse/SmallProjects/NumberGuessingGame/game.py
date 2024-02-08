from random import randint

def replay_game()->bool:
    print("Want to play again?\n")
    answer = input()
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Please enter 'yes' or 'no'\n")
        return replay_game()
    
def is_valid(user_number: int, max_number: int)->bool:
    if user_number.isnumeric():
        if 1 <= int(user_number) <= max_number:
            return True
    return False

def get_max_number()->int:
    max_number = input("Please enter the maximum number!\n")
    while max_number.isnumeric() == False or int(max_number) <= 1:
        max_number = input("Could you enter a number and make it greater than 1?\n")
    return int(max_number)

def start()->list:
    max_number = get_max_number()
    random_number = randint(1, max_number)

    question = "Try to guess a number from 1 to " + str(max_number) + "! What do you think this number is?\n\n"
    user_number = input(question)
    attempts = 1
    return [random_number, user_number, attempts, max_number]

def get_number(user_number: int, max_number: int)->int:
    while is_valid(user_number, max_number) == False:
        question = "Or maybe we’ll still enter an integer from 1 to " + str(max_number) + "?\n"
        user_number = input(question)
    return int(user_number)
    
def game_turn(user_number: int, random_number: int, attempts: int)->bool:
    if random_number == user_number:
        print("You guessed it, congratulations!\n")
        print("You guessed after", attempts, "tries!\n\n")
        return False
    else:
        if user_number < random_number:
            print("Your number is LESS than the hidden number, try again!")
        else:
            print("Your number is GREATER than the hidden number, try again!")
    return True

def game()->None:
    print("Welcom to Number guessing game!\n")
    
    start_game = True

    while start_game == True:
        random_number, user_number, attempts, max_number = start()

        user_number = get_number(user_number, max_number)

        while game_turn(user_number, random_number, attempts):
            attempts += 1
            user_number = input()
            user_number = get_number(user_number, max_number)
        start_game = replay_game()
    
    print("Thanks for playing the number guessing game. See you...")


game()
