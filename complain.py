PROMISED_DOWNLOAD = 20
PROMISED_UPLOAD = 20
chrome_driver_path = "C:/Users/LENOVO\Desktop/development/chromedriver.exe"

import time
import selenium
from selenium import webdriver


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        
        
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.up)
       
    def tweet_at_provider(self):
        import tweepy

# personal details
        consumer_key ="DggiEEVJeoaZ0A6lIslnm1oGR"
        consumer_secret ="QbC8VWZaHkOkdqGwwvqEYVfUxCIdfqZuK5bqfaTam3jG4Sl2Df"
        access_token ="797872401149206528-kI2KM5nR49yQV4MdwI6k4zHN7jOPpDC"
        access_token_secret ="rSaNybTiH0hZ1k8c9q0vhkHpUDT7zaEBaGphGThO5gYmM"

        # authentication of consumer key and secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # authentication of access token and secret
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        print("Debugging")

    # update the status
        if float(self.down) < PROMISED_DOWNLOAD or float(self.up) < PROMISED_UPLOAD :
            tweet = f"@RailWireIndia, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?"
    
            api.update_status(status = tweet)
            print("status updated")

    
    


from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    bot = InternetSpeedTwitterBot(chrome_driver_path)
    bot.get_internet_speed()
    print(bot.down)
    bot.tweet_at_provider()



scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=3)
scheduler.start()

