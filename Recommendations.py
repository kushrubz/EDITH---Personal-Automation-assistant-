from selenium import webdriver

class recom():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\kush\\Drivers\\geckodriver.exe")

    def recom_info(self):
        self.driver.get('https://www.imdb.com/list/ls091520106/')


#bot = recom()
#bot.recom_info()