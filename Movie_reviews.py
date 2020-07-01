from selenium import webdriver
import pyttsx3 as p

class Movie():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\kush\\Drivers\\geckodriver.exe")

    def movie_reviews(self,name):
        self.driver.get('https://www.google.com/')
        search = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + ' movie reviews')
        submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
        submit.click()

        engine = p.init()
        brief_review = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]')
        brief_review_text = brief_review.text
        detail_review1 = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/critic-reviews-container/div/div/div/span/div/div[1]/div/div/div[1]/i')
        detail_review1_text = detail_review1.text
        detail_review1by = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/critic-reviews-container/div/div/div/span/div/div[1]/div/div/div[2]/div')
        detail_review1by_text = detail_review1by.text
        detail_review2 = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/critic-reviews-container/div/div/div/span/div/div[2]/div/div/div[1]/i')
        detail_review2_text = detail_review2.text
        detail_review2by = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/critic-reviews-container/div/div/div/span/div/div[2]/div/div/div[2]/div')
        detail_review2by_text = detail_review2by.text

        engine.say(brief_review_text)
        engine.say(detail_review1_text)
        engine.say(detail_review1by_text)
        engine.say(detail_review2_text)
        engine.say(detail_review2by_text)
        engine.runAndWait()


#bot = Movie()
#bot.movie_reviews('life of pi')




