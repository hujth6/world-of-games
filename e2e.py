from selenium import webdriver
from time import sleep
import sys
from Utils import MainScores_url

def main_function():
    if test_score_service(MainScores_url):
        sys.exit(0)
    else:
        sys.exit(-1)


def test_score_service(url):
    chrome_driver = webdriver.Chrome(executable_path='/Users/yochaiglik/Downloads/chromedriver')
    chrome_driver.get(url)

    try:
        score = int(chrome_driver.find_element_by_id('score').text)
    except Exception as e:
        print(e)
        return False

    if 1 < score < 1000:
        return True
    else:
        return False


main_function()
