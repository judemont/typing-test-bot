from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import os
import sys

AVALAIBLES_WEBSITES = ["10fastfingers"]

def get_locator(by_string):
    """Returns the By object based on the string representation."""
    if by_string == "id":
        return By.ID
    elif by_string == "class":
        return By.CLASS_NAME
    else:
        raise ValueError("Unknown locator type: %s" % by_string)


def load_website_data(website):
    """Loads website data from a JSON file."""
    base_dir = os.path.dirname(os.path.realpath(__file__))
    websites_dir = os.path.join(base_dir, "websites")
    file_path = os.path.join(websites_dir, website + ".json")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data


def click_buttons(driver, buttons_to_click):
    """Clicks the buttons specified in the buttons_to_click list."""
    for button_info in buttons_to_click:
        locator_type = button_info["get-with"]
        locator_value = button_info["value"]

        locator = get_locator(locator_type)
        button = driver.find_element(locator, locator_value)
        button.click()
        print(f"{locator_value} button clicked")


def write_words(driver, word_input_info, word_to_write_info):
    """Writes words on the website."""
    locator_type = word_input_info["get-with"]
    locator_value = word_input_info["value"]
    word_input = driver.find_element(get_locator(locator_type), locator_value)

    locator_type = word_to_write_info["get-with"]
    locator_value = word_to_write_info["value"]

    while True:
        try:
            word = driver.find_element(get_locator(locator_type), locator_value).text
            word_input.send_keys(word)
            print(word)
            word_input.send_keys(" ")
        except:
            break

def print_help():
    print("Usage: typing-bot [website]")
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
    buttons_to_click = website_data["buttons-to-click"]
    word_input_info = website_data["word-input"]
    word_to_write_info = website_data["word-to-write"]

    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)

    click_buttons(driver, buttons_to_click)
    time.sleep(5)
    write_words(driver, word_input_info, word_to_write_info)


if __name__ == "__main__":
    main()
