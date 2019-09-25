import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 1
MainScores_url = 'http://127.0.0.1:5000/'

def Screen_clear():
    try:
        print("this will clear the screen")
        os.system('cls' if os.name == 'nt' else 'clear')
    finally:
        print("could not clear the screen")
        print("\n" * 20)


