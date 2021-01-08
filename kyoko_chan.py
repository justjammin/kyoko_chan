# Define your functions

def site_navigation():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a' or 'A':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return site_navigation()

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def music_selection():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'c':
    return social_ctas()
  else:
    print_message()
    return music_selection()
  
def social_ctas():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else:
    print_message()
    return social_ctas()  

def kyoko_chan():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []

  while order_drink == 'y':
    size = site_navigation()  
    drink_type = music_selection()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n> ')

      if order_drink in ['y', 'n']:
        break

  print('Okay, so I have:')

  for drink in drinks:
    print('-', drink)
  
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

# Call kyoko_chan()!

kyoko_chan()

#run this in the terminal under python3 coffee_chan.py