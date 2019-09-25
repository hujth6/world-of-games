import random

def generate_number(dif):
    return random.randrange(1, dif)

def get_guess_from_user(dif):
    return input(f"please choose a number between 1 and {dif}\n")

def compare_results(guess, secret):
    if guess == secret:
        return True
    else:
        return False

def play(dif):
    difficulty = dif * 20
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    # print(secret_number)
    if compare_results(guess,secret_number):
        return True
    else:
        return False



