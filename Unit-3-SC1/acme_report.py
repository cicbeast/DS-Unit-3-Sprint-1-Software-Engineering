from acme import Product
from random import randint, sample, uniform

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num = 30):
    products = []
    n = 0
    while n < num:
        P = Product(name=[sample(adj,1)+sample(noun,1)],
                                      price=randint(5, 100),
                                      weight=randint(5, 100),
                                      flammability=uniform(0.0, 2.5),
                                      identifier=randint(1000000,9999999)
                                      )
        P_info = [P.name, P.price, P.weight, P.flammability, P.identifier]
        products = products + P_info
        n += 1
    # print(products)
    return products

def inventory_report(products):
    # num_unique = 0
    pass

if __name__ == '__main__':
    inventory_report(generate_products())
