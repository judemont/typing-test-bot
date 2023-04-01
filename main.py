from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json
import os
import sys

AVALAIBLES_WEBSITES = ["10fastfingers", "typing.com"]


def load_website_data(website):
    """Loads website data from a JSON file."""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    websites_dir = os.path.join(base_dir, "typing-test-websites")
    file_path = os.path.join(websites_dir, website + ".json")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data


def click_buttons(driver, buttons_to_click):
    """Clicks the buttons specified in the buttons_to_click list."""
    for button_info in buttons_to_click:
        
        locator = button_info["css-selector"]
        button = driver.find_element(By.CSS_SELECTOR, locator)
        button.click()
        print(f"{locator} button clicked")


def write_words(driver, word_input_info, word_to_write_info, next_key):
    """Writes words on the website."""
    
    locator = word_input_info["css-selector"]

    word_input = driver.find_element(By.CSS_SELECTOR, locator)

    locator = word_to_write_info["css-selector"]

    while True:
        try:
            word = driver.find_element(By.CSS_SELECTOR, locator).text
            word_input.send_keys(word)
            print(word)
            word_input.send_keys(next_key)
        
        except NoSuchElementException:
            break


def print_help():
    print("Usage: python main.py [website]")
    print("--help or -h : print this help")
    exit()
def verify_arguments(args):
    if len(args) <= 0:
        print_help()
    elif args[0].startswith('-'):
        if args[0] == "--help" or args[0] == "-h":
            print_help()
        else:
            raise ValueError("Invalid argument : %s \nuse --help to get help" % args[0])
    elif args[0] not in AVALAIBLES_WEBSITES:
        raise ValueError("The typing test %s is not available \nAvalaible typing tests: %s" %(args[0], AVALAIBLES_WEBSITES))
    

def main():
    argvs = sys.argv[1:]
    verify_arguments(argvs)


    website = argvs[0]
    website_data = load_website_data(website)

    url = website_data["url"]
    next_key = website_data["next-key"]
    buttons_to_click = website_data["buttons-to-click"]
    word_input_info = website_data["input"]
    word_to_write_info = website_data["to-write"]

    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)
    

    click_buttons(driver, buttons_to_click)
    time.sleep(5)
    write_words(driver, word_input_info, word_to_write_info, next_key)


if __name__ == "__main__":
    main()
