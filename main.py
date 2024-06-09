print("Welcome to HackWakers Plant Watering Reminder App")
name=input("What is your name? ")
print("Welcome",name)
plants=input("Do you own any plants?\n" "If yes, type the number of plants you own." " If you don't own any plants, type 0: \n")
inn=0
if inn=="0":
  inn=input("How many indoor plants do you own? \n")
  if inn=="0":
    print("You should get some indoor plants")
  elif inn>="1":
    print("You should water your indoor plant once a week")
  else:
    print("Invalid input. Please try again...")

  print("You can water your indoor plants every 3 days")
  if plants=="0":
    print("You should get a plant...It's good for the environment...")
  elif plants>="1":
    q=int(input("Have you already watered your plants today?\n If yes, type 1. If no, type 2 \n"))
    if q==1:
      print("You should water them again in a bit! Watering plants twice a day in the summer is good for the plants...")
    elif q==2:
      print("You should water them now! You should try to water your plants twice a day...")
    else:
      print("Invalid input. Please try again...")
  else:
    print("Invalid input. Please try again...")



# Define your functions
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def greeting():
  name = input("Welcome to our Plant Watering Reminder app, let's start by getting your name?" )
  if name == "":
    print("Please enter your name.")
  else:
    print("Welcome", name)
    
def get_size():
  res = input('Do you own a plant? \n[a] Yes I own 1 plant \n[b] Yes I own more than one plant \n[c] No, I do not own any plants \n ')
  if res == 'a' or 'b':
    return "That is good... are your plant's indoor or outdoor plants?"
  elif res == 'c':
    return 'You should plan on getting a plant... It is good for the environment!'
  else:
    print_message()
    return get_size()

def get_drink_type(): 
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n> ")

  if res == 'a':
    return 'brewed coffee'
  elif res =='b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte(): 
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n> ")

  if res == 'a':
    return 'latte'
  elif res =='b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()  

def coffee_bot():
  print('Welcome to the cafe!')

  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

# Call coffee_bot()!
coffee_bot()
