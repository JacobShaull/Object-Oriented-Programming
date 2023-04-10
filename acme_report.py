import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    '''Generates a list of 30 acme products with randomly
    generated values for class attributes'''
    products = []

    for i in range(num_products):
        random_adjectives = random.sample(ADJECTIVES, 1)
        random_nouns = random.sample(NOUNS, 1)
        name = random_adjectives[0] + ' ' + random_nouns[0]

        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    '''returns unique names, avg price, weight and flammability'''

    unique_names = set()
    for i in products:
        unique_names.add(i.name)
    print(unique_names)
    unique_names = len(unique_names)

    avg_price_sum = sum([item.price for item in products])/len(products)
    avg_weight_sum = sum([item.weight for item in products])/len(products)
    avg_flamm_sum = sum([item.flammability for item in products])/len(products)

    return unique_names, avg_price_sum, avg_weight_sum, avg_flamm_sum


if __name__ == '__main__':
    inventory_report(generate_products())
