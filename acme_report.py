import random
from acme import Product

team_names_1 = ['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']

team_names_2 = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_rand_names(n=30):
  name1 = random.sample(team_names_1, k=1)
  name2 = random.sample(team_names_2, k=1)
  name = name1 + name2
  return name


def generate_rand_price_weight(price, weight):
  price = random.sample(5, 100, k=1 )
  weight = random.sample(5, 100, k=1 )
  return price, weight 
  
def flammability(number):
  number = random.sample(0.0, 2.5, k=1)
  return number

