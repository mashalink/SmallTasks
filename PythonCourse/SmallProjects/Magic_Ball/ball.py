from random import randint

answers = ["'It is certain'", "'As I see it, yes'", "'Reply hazy, try again'", "'Don't count on it'", \
           "'It is decidedly so'", "'Most likely'", "'Ask again late'", "'My reply is no'", "'Without a doubt'", \
            "'Outlook good'", "'Better not tell you now'", "'My sources say no'", "'Yes definitely'", \
            "'Yes'", "'Cannot predict now'", "'Outlook not so good'", "'You may rely on it'", "'Signs point to yes'",
            "'Concentrate and ask again'", "'Very doubtful'"]

def choise()->str:
    random_number = randint(0, 19)
    return answers[random_number]

def replay_choise()->bool:
    print("Would you like to know something else?\n")
    answer = input()
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Please print 'yes' or 'no'\n")
        return replay_choise()
    
def ball()->None:
    print("Hello World, I am a magic ball and I know the answer to any question you have.\n")

    name = input("What is your name?\n\n")
    print("Hello ", name, "!\n", sep='')
    
    replay = True
    while replay:
        question = input("\nWhat would you like to know?\n\n")
        print("\n", choise(), end="\n\n", sep='')
        replay = replay_choise()

    print("\nCome back if you have any questions!\n")

ball()
