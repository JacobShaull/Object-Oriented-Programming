from acme import Product


def test_default_product_price():

    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():

    '''Test default product weight being 20.'''
    prod = Product('Test Product')
    assert prod.weight == 20


def test_stealability():

    '''Test products stealability returnes the
    correct values'''
    prod = Product('Test Product')
    if prod.price/prod.weight < 0.5:
        assert prod.stealability == "Not so stealable..."


def test_number_of_products():

    '''Assert 30 products in products'''
    products = Product('generate_products')
    assert len(products) == 30
