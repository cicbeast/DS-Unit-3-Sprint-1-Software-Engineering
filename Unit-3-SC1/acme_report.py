from acme import Product
from random import randint, sample, uniform

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num=30):
    products = []
    n = 0
    while n < num:
        P = Product(name=str(sample(adj, 1)+sample(noun, 1)),
                    price=randint(5, 100),
                    weight=randint(5, 100),
                    flammability=uniform(0.0, 2.5),
                    identifier=randint(1000000, 9999999)
                    )
        P_info = [[P.name, P.price, P.weight, P.flammability, P.identifier]]
        products = products + P_info
        n += 1
    return products


def inventory_report(products):
    prod_names = [row[0] for row in products]
    prod_price = [row[1] for row in products]
    prod_weight = [row[2] for row in products]
    prod_flam = [row[3] for row in products]
    num_unique = len(set(prod_names))
    av_price = sum(prod_price)/len(prod_price)
    av_weight = sum(prod_weight)/len(prod_weight)
    av_flam = sum(prod_flam)/len(prod_flam)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Number of Unique Product Names:', num_unique)
    print('Average Price of Products:', av_price)
    print('Average Weight of Products:', av_weight)
    print('Average Flammability of Products:', av_flam)


if __name__ == '__main__':
    inventory_report(generate_products())
