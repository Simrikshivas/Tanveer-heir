print("Welcome to HackWakers Plant Watering Reminder App")
name = input("What is your name? ")

print("Welcome", name)

plants = int(
    input(
        "Do you own any plants?\nIf yes, type the number of plants you own. If you don't own any plants, type 0: \n"
    ))

while plants != 0:
  inn = int(input("How many indoor plants do you own? \n"))
  if inn == 0:
    print("You should get some indoor plants")
  elif inn >= 1:
    print("You should water your indoor plant once a week")
  else:
    print("Invalid input. Please try again...")

  print("You can water your indoor plants every 3 days")
  if plants == 0:
    print("You should get a plant...It's good for the environment...")
  elif plants >= 1:
    q = int(
        input(
            "Have you already watered your plants today?\n If yes, type 1. If no, type 2 \n"
        ))
  if q == 1:
    print(
        "You should water them again in a bit! Watering plants twice a day in the summer is good for the plants..."
    )
  elif q == 2:
    print(
        "You should water them now! You should try to water your plants twice a day..."
    )
  else:
    print("Invalid input. Please try again...")
  break

if plants == 0:
  print("You should get a plant...It's good for the environment...")
