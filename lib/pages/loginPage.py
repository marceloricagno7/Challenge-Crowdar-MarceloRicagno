from lib.pages.basePage import BasePage
class LoginPage(BasePage):

    #Componentes -> Estructura vble: TypeComponent_NameComponent = 'Locator'  #TypeLocator
    input_user='user-name'  #id
    input_pass='password'   #id
    btn_login='login-button'   #id
    error_text='[data-test="error"]'  #css
    text_menu='[data-test="title"]'   #css


    def send_login(self, user, passwd):
        self.sendText(user, self.input_user, "ID")
        self.sendText(passwd, self.input_pass, "ID")
        self.clickElement(self.btn_login, "ID")

    def verify_error_message(self):
        result = self.getText(self.error_text, "CSS")
        return result

    def get_text_menu(self):
        result = self.getText(self.text_menu, "CSS")
        return result