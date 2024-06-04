from selenium.webdriver.common.by import By
class LoginPage:
    
    username_textbox ="user-name"
    password_textbox = "password"
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = "user-name"
        self.password_textbox= "password"
        self.login_button = "login-button"

    def setUserName(self, username):
        self.driver.find_element(By.ID,self.username_textbox).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.password_textbox).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.login_button).click()