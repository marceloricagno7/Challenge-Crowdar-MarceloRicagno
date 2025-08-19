from behave import given, when, then
from lib.pages.shoppingCartPage import ShoppingCartPage

@when('Seleccionamos el producto "{product}" y lo agregamos al carrito')
def step_impl(context, product):
    driver = context.driver
    shoppingCartPage = ShoppingCartPage(driver)

    # Ingresamos a un producto y lo agregamos desde alli
    context.selected_product = product
    shoppingCartPage.select_product(context.selected_product)
    shoppingCartPage.add_product_shopping_cart()

@then('Verificamos que el producto se encuentra en el carrito')
def step_impl(context):
    driver = context.driver
    shoppingCartPage = ShoppingCartPage(driver)

    shoppingCartPage.go_to_shopping_cart()
    tupla_texts = shoppingCartPage.verify_product_cart()
    assert '1' in tupla_texts, f"La Cantidad no es la correcta"
    assert context.selected_product in tupla_texts, f"'{context.selected_product}' no está en el carrito"