# instabot_selenium
A simple bot that logs into your Instagram account (using chrome) and then prints the list of fake people in your life (People you follow who don't follow you back).

This bot uses the **Selenium Webdriver** along with the **chromedriver** to access your Instagram account via the website using Google Chrome.

Points to note before executing the code -
1. Please make changes to the credentials.py file at the specified places to match **your** username and password.
2. This code can only be run on an instagram account with **atleast** a decent number of follower and following accounts. (Minor changes have to be made for other accounts)
3. Accounts with an unusually large number of followers/following accounts may take a while to execute. In this case, your patience is expected here.
4. Issues may arise due to incompatibility with the chromedriver. In this case, please click this link and then download the required  version. https://chromedriver.chromium.org/downloads
5. This program can also be run on other browsers, although chrome is recommended. For this, please download the required driver and include it in the \_\_init\_\_ function of the Instabot class (self.driver).

