from selenium import webdriver
import pyttsx3 as p

#class to get informataion from wikipedia
class info():
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path="C:\\Users\\kush\\Drivers\\geckodriver.exe")

    def get_info(self,query):
        self.query= query
        self.driver.get(url='https://www.wikipedia.org/')
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]') #finding search box by xpath
        search.click() #selecting the search field box
        search.send_keys(query) #entering search keyword into the field

        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

        #the definition that the bot can read
        info = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div/p[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()


#bot=info()
#bot.get_info('liberty bell')
