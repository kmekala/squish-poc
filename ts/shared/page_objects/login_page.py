from squish import *

# Page Object for Login Page
class LoginPage:
    UI_USERNAME_FIELD = ":LoginDialog.usernameEdit"
    UI_PASSWORD_FIELD = ":LoginDialog.passwordEdit"
    UI_LOGIN_BUTTON = ":LoginDialog.loginButton"

    def enter_username(self, username):
        waitForObject(self.UI_USERNAME_FIELD)
        type(self.UI_USERNAME_FIELD, username)

    def enter_password(self, password):
        waitForObject(self.UI_PASSWORD_FIELD)
        type(self.UI_PASSWORD_FIELD, password)

    def click_login(self):
        waitForObject(self.UI_LOGIN_BUTTON)
        clickButton(self.UI_LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()