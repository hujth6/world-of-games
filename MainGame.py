from live import welcome, load_game
# import requests
# import GuessGame


welcome(input("Hi, what is your name?\n"))


if load_game():
    print("you WON!!!")
else:
    print("you LOST!!!")


