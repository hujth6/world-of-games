import GuessGame, MemoryGame, CurrencyRouletteGame, Score



def welcome(name):
    print('Hello, %s and wellcome to the World of Games (WoG).\nHere you can find many cool games to play.' %name)




def load_game():

    print("Please choose a game to play:")
    game = int(input("    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\
    2. Guess Game - guess a number and see if you chose like the computer\n\
    3. Currency Roulette - tryand guess the value of a random amount of USD in ILS\n\
    choose 1/2/3\n"))
    difficulty = int(input("choose difficulty level (1-5):\n"))

    if game == 1:
        win = MemoryGame.play(difficulty)
    elif game == 2:
        win = GuessGame.play(difficulty)
    elif game == 3:
        win = CurrencyRouletteGame.play(difficulty)

    Score.add_score(difficulty)
    return win

