from selenium import webdriver

class youtube_music():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\kush\\Drivers\\geckodriver.exe")

    def play_music(self,name):
        self.driver.get('https://music.youtube.com/search?q=' + name)
        play = self.driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[1]/ytmusic-responsive-list-item-renderer/div[1]/ytmusic-item-thumbnail-overlay-renderer/div/ytmusic-play-button-renderer/div/yt-icon')
        play.click()



#bot=youtube_music()
#bot.play_music('Destiny')