from random import randint

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_."

AMBIGUOUS_CHARACTERS = "il1Lo0O"

def add_or_not(question: str)->bool:
    answer = input(question)
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Please enter 'yes' or 'no'\n")
        return add_or_not(question)

def add_characters()->str:
    chars = ""
    if add_or_not("Should I include the numbers 0123456789?\n"):
        chars = DIGITS
    if add_or_not("Should I include lowercase letters abcdefghijklmnopqrstuvwxyz?\n"):
        chars += LOWERCASE_LETTERS
    if add_or_not("Should I include capital letters ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n"):
        chars += UPPERCASE_LETTERS
    if add_or_not("Should I include the characters !#$%&*+-=?@^_?\n"):
        chars += PUNCTUATION
    return chars

def is_valid_number(question: str)->int:
    number = input(question)
    if number.isnumeric():
        return int(number)
    else:
        print("Please use numbers only.\n")
        return is_valid_number(question)

def password_without_ambiguous(chars:str, number_of_passwords: int, password_length: int)->None:
    for _ in range(number_of_passwords):
        password = ""
        for _ in range(password_length):
            char = chars[randint(0, len(chars) - 1)]
            while char in AMBIGUOUS_CHARACTERS:
                char = chars[randint(0, len(chars) - 1)]
            password += char
        print(password)

def password_with_ambiguous(chars:str, number_of_passwords: int, password_length: int)->None:
    for _ in range(number_of_passwords):
        password = ""
        for _ in range(password_length):
            password += chars[randint(0, len(chars) - 1)]
        print(password)

def generator()->None:
    number_of_passwords = is_valid_number("What is the number of passwords to generate?\n")
    password_length = is_valid_number("How long should passwords be?\n")
    chars = add_characters()
    if add_or_not("Should ambiguous characters il1Lo0O be excluded?\n"):
        password_without_ambiguous(chars, number_of_passwords, password_length)
    else:
        password_with_ambiguous(chars, number_of_passwords, password_length)

generator()