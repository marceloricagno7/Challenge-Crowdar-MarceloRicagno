from lib.pages.basePage import BasePage

class ShoppingCartPage(BasePage):

    #Componentes -> Estructura vble: TypeComponent_NameComponent = 'Locator'  #TypeLocator
    text_selected_product= "//div[@data-test='inventory-item-name' and text()='{selectedProduct}']"  #xpath
    btn_add_to_cart='add-to-cart'   #id
    btn_go_to_cart='[data-test="shopping-cart-link"]'  #css
    text_quantity='[data-test="item-quantity"]'  #css
    text_product_in_cart='[data-test="inventory-item-name"]'

    def select_product(self, selectedProduct):
        self.clickElement(self.text_selected_product.format(selectedProduct=selectedProduct), "XPATH")

    def add_product_shopping_cart(self):
        self.clickElement(self.btn_add_to_cart, "ID")

    def go_to_shopping_cart(self):
        self.clickElement(self.btn_go_to_cart, "CSS")

    def verify_product_cart(self):
        text_quantity= self.getText(self.text_quantity, "CSS")
        text_product= self.getText(self.text_product_in_cart, "CSS")
        return text_quantity, text_product

