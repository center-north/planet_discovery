#PLANET DISCOVERY TERMINAL GAME
import random

#Player
class Player:
    def __init__(self, name, r_sys):
        self.name = name
        self.r_sys = r_sys
        
    def __repr__(self):
        return f"Your name is {self.name} and your respiratory system is {self.r_sys} based."
    
    def define_breathing(self):
        while True:
          try:
            self.chose_r_sys = int(input("""Tell me about your respiratory system. 
            Type '1' if you breathe oxygen, type '2' if you breathe ammonia
            """))
            if self.chose_r_sys == 1:
              self.r_sys = "oxygen"
              break
            elif self.chose_r_sys == 2:
              self.r_sys = "ammonia"
              break
            else:
              print("Your input is not valid. Type 1 for oxygen, 2 for ammonia.")
          except ValueError:
            print("Invalid input. Please enter a number.")
    
#Spaceship        
class Spaceship:
    def __init__(self, name):
        self.name = name
        self.storage = 0
        self.fuel = 0
        self.equipment = 0
        self.has_storage = True
        self.has_fuel = True
    def __repr__(self):
        return f"Welcome on board! You are on the '{self.name}' spaceship."
    def add_fuel(self, amount):
        if self.storage + amount <= 3:
            self.fuel += amount
            self.storage += amount
            print(f"Added {amount} units of fuel. Total fuel: {self.fuel}/3")
        else:
            print("You're out of storage")
    def add_equipment(self, amount):
        if self.storage + amount <= 3:
            self.equipment += amount
            self.storage += amount
            print(f"Added {amount} units of equipment. Total equipment: {self.equipment}")
        else:
            print("You're out of storage")
            
#Spaceship random name generator
def spaceship_name_generator():
  first_part = ["Silly", "Fat", "Rusty", "Slow", "Dirty", "Bouncing", "Melted", "Spoiled", "Drunk", "Rotten"]
  second_part = ["Thunderstorm", "Dragon", "Lion", "Nova", "Galaxy", "Fireball", "Hero", "Discoverer", "Explorer", "Ninja"]
  spaceship_name = first_part[random.randint(0, len(first_part)-1)] + " " + second_part[random.randint(0, len(second_part)-1)]
  return spaceship_name

#Spaceship fuel /storage configuration
def spaceship_configuration(spaceship):
    while True:
        choice = input("Do you want to add fuel (f) or equipment (e) to the storage? (q to exit): ")
        if choice.lower() == 'f':
            try:
                amount = int(input("How many units of fuel do you want to add? "))
                spaceship.add_fuel(amount)
            except ValueError:
                print("Input is not valid. Please type a number.")
        elif choice.lower() == 'e':
            try:
                amount = int(input("How many unit of equipment do you want to add? "))
                spaceship.add_equipment(amount)
            except ValueError:
                print("Input is not valid. Please type a number.")
        elif choice.lower() == 'q':
            break
        else:
            print("Scelta non valida.")

#Planet
class Planet:
    def __init__(self, name):
        self.name = name
        self.atmosphere = ""
        self.hospitable = True
        self.gravity = 0 
    def __repr__(self):
        return f"Planet '{self.name}' spotted."
   #random planet constructor
    def planet_atmosphere_builder(self):
        self.atm_composition = random.randint(1, 2)
        if self.atm_composition == 1:
            self.atmosphere = "oxygen"
        else:
            self.atmosphere = "ammonia"
        return self.atmosphere     
    def planet_is_hospitable(self):
        self.hospitality = random.randint(1, 2)
        if self.hospitality == 1:
            self.hospitable = True
        else:
            self.hospitable = False
        return self.hospitable
    def planet_gravity_builder(self):
        self.set_gravity = random.randint(1, 2)
        if self.set_gravity == 1:
            self.gravity = 1
        else:
            self.gravity = 2
        return self.gravity

#planet random name generator
def planet_name_generator():
  first_part = ["XY", "Random", "Asteroid", "Massive", "Rock", "Star", "Giant", "Outer", "Small", "Flashing"]
  second_part = ["99", "67-67", "199", "5", "974", "12345", "0001", "737", "0-7-2", "Alpha"]
  planet_name = first_part[random.randint(0, len(first_part)-1)] + "-" + second_part[random.randint(0, len(second_part)-1)]
  return planet_name

#function lander 
def spaceship_lander(planet_name, spaceship): #aggiungere il controllo per fuel <0!
    if spaceship.fuel <= 0:
        print("You're out of fuel! Game over.")
        return False #game over
    spaceship.fuel -= 1
    print(f"Planet {planet_name} spotted!")
    while True:
        landing_button = input("Press 'a' key to land!")
        if landing_button.lower() == "a":
            print(f"Landed! Your amount of fuel is now {spaceship.fuel} units!")
            break #insert check planet function here? to decide
        else:
            print("Invalid key! Press 'a' key to land")
    return landing_button


#liveability checker
def check_planet_liveability(hosp, grav):
    estimated_liveability = ""
    if hosp == True and grav == 1:
        estimated_liveability = "high"
    elif hosp == True and grav == 2:
        estimated_liveability = "medium"
    elif hosp == False and grav == 1:
        estimated_liveability = "medium"
    elif hosp == False and grav == 2:
        estimated_liveability = "low"
    else:
        print("Something went wrong")
    return estimated_liveability
    
    #planet switcher
def planet_switcher(liveability_score, test_spaceship):
    print(f"At the first sight, the liveability of this planet seems {liveability_score}")
    while True:
        final_decision = input("""Do you want to land or move to another planet?
                               NOTE: by continuing to another planet you will consume 1 unit of fuel.
                               Press 'c' to continue or 's' to land.""")
        if final_decision.lower() == "s":
            winner_checker = winner_or_loser(main_player, test_spaceship, test_planet)
            if winner_checker:
                print("Congratulations! You colonised the planet!")
            else:
                print("Sorry, you're dead!")
            return False #end the game
        elif final_decision.lower() == "c":
            return True #continue to next planet
        else: 
            print("Invalid input. Please try again.")
            
#winner or loser check
def winner_or_loser(player, spaceship, planet):
    planet_score = 0
    player_score = 0
    result = True
    if player.r_sys == planet.atmosphere:
        player_score += 1
    else:
        planet_score += 1
    if planet.hospitable == True:
        player_score += 1
    else:
        planet_score += 1
    if planet.gravity == 1:
        player_score += 1
    else:
        planet_score += 1
    player_score += spaceship.equipment 
    if player_score > planet_score:
        result = True
    else: 
        result = False
    return result
    
#Introduction
introduction = """Welcome astronaut.
You are now on your way to discover a new planet.
Are you ready for this journey?
"""
print(introduction)

#PLAYER 
#defining player: defining respiratory system and name of the player
player_name = input("""First of all, introduce yourself.
what is your name?
""")
main_player = Player(player_name, "")
main_player.define_breathing()
print(main_player)

#SPACESHIP
#defining spaceship
spaceship_random_name = spaceship_name_generator()
test_spaceship = Spaceship(spaceship_random_name)
spaceship_configuration(test_spaceship)
print(test_spaceship)

#getting ready to the voyage... starting the engine
print(f"{main_player.name}, you are now ready to go. {spaceship_random_name} has {test_spaceship.fuel}/3 units of fuel and {test_spaceship.equipment}/3 units of equipment")
while True:
    user_input = input("Are you ready? Press 'y' to start the engine: ")
    if user_input.lower() == "y":
        break
    else:
        print("Invalid input! press 'y' to continue")

#PLANET 
#defining planet
test_planet = Planet(planet_name_generator())
planet_name = test_planet.name
liveability_checker = check_planet_liveability(test_planet.planet_is_hospitable(), test_planet.planet_gravity_builder())

#planet lander
if spaceship_lander(planet_name, test_spaceship) == False:
    exit()

# checking if the planet is good or not. if it is good land, if not go away
while True:
    if planet_switcher(liveability_checker, test_spaceship) == False:
        exit()

# generating a new planet for the next iteration
    test_planet = Planet(planet_name_generator())
    planet_name = test_planet.name
    liveability_checker = check_planet_liveability(test_planet.planet_is_hospitable(), test_planet.planet_gravity_builder())

    #planet lander
    if spaceship_lander(planet_name, test_spaceship) == False:
        exit()

#determine winner / loser  
winner_checker = winner_or_loser(main_player, test_spaceship, test_planet)
print(winner_checker)