from credentials import *
from selenium import webdriver
import time

class Instabot:
    def __init__(self,user,pwd):
        self.username = user
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pwd)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        
        time.sleep(4)
        
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        time.sleep(1)
        following = self.get_names()

        # Prints the number of accounts you follow
        # print(len(following))

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        time.sleep(1)
        followers = self.get_names()
        
        # Prints the number of followers you have
        # print(len(followers))

        fake_peeps = [user for user in following if user not in followers]
        for i in fake_peeps:
            print(i)

    def get_names(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        scroll_box.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        return names

my_bot = Instabot(getUsername(),getPassword())
my_bot.get_unfollowers()
