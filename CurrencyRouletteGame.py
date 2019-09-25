import requests
import random
def get_currency():
    # ils default
    ils = 3.5
    try:
        # Where USD is the base currency you want to use
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        # Making our request
        response = requests.get(url)
        data = dict(response.json())
        ils = data.get('rates').get('ILS')
        return ils
    except ConnectionError:
        print("no connection")
    finally:
        return ils


def get_money_interval(dif, amt):
    total = (amt * get_currency())
    return [total - (dif - 5), total + (dif - 5)]

def get_guess_from_user(amt):
    return int(input(f"how much {amt} would be in ILS\n"))

def play(dif):
    amount = random.randrange(1,101)
    difficulty = dif
    interval = get_money_interval(difficulty,amount)
    if interval[0] > get_guess_from_user(amount) > interval[1]:
        return True
    return False

