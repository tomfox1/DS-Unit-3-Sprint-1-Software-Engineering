from possible_values import *
from acme import Product
from random import randint, uniform, sample, choice


nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']


def generate_products(n=30):
    
     list_prod = []

    for _ in list(range(n)):

        product = Product(name='{n} {a}'.format(n=choice(nouns),a=choice(adjectives)), 
        price=randint(5, 100), 
        weight=randint(5,100),
        flammability=uniform(0,2.5))

        list_prod.append(product)

    return list_prod




def inventory_report(list_prod):

    total_price = 0
    total_weight= 0 
    total_flammability = 0

    for product in list_prod:
        total_price +=  product.price
        total_weight += product.weight
        total_flammability += product.flammability 

    exclusive_prod = len(set(list_prod))
    mean_price = total_price / len(list_prod)
    mean_weight = total_weight / len(list_prod)
    mean_flammability = total_flammability / len(list_prod)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
   
    print('Unique Prod: ', unique_prod)
    print('Average Price of items: ', mean_price)
    print('Average Weight of items: ', mean_weight)
    print('Average Flammability of items: ', mean_flammability)
    