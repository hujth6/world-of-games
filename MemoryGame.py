import random
from time import sleep


def generate_sequence(dif):
    sequence = []
    for i in range(dif):
        sequence.append(random.randrange(1, 101))
    return sequence


def get_list_from_user(dif):
    sequence = []
    for i in range(dif):
        sequence.append(int(input("write one number:\n")))
    return sequence


def is_list_equal(pre_list, user_list, x):
    same = False
    print(x)

    if x:
        if pre_list == user_list:
            return True
        else:
            return False
    else:
        for i in user_list:
            if i in pre_list:
                same = True
            else:
                return False
        return same


def play(dif):

    player = ""
    orderly = True
    difficulty = dif
    sequence = generate_sequence(difficulty)

    if orderly:
        print(f"hi {player}, you will be shown a sequence of numbers,\n each numbere for 0.7 seconds\nyou need to guess them in the same order")
    else:
        print(f"hi {player}, you will be shown a sequence of numbers,\n each numbere for 0.7 seconds\nyou dont need to guess them in the same order")

    input("press enter when you are ready")
    # show sequence
    sequence.append("")
    for i in sequence:
        print('\r' + str(i), end='')
        sleep(0.7)
    print("now its your turn to guess")
    del sequence[difficulty]
    # end show sequence

    return is_list_equal(sequence, get_list_from_user(difficulty), orderly)

