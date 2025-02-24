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
        return f"Welcome on board! You are on the {self.name} spaceship."
      
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

#Spaceship configuration
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
        self.distance = 0
        self.atmosphere = "oxygen"
        self.hospitable = True
        self.gravity = 0
    
    def __repr__(self):
        return f"Planet '{self.name}' spotted."
        
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

#defining spaceship
test_spaceship = Spaceship("Zero Gravity")
spaceship_configuration(test_spaceship)
print(test_spaceship)

#defining planet
test_planet = Planet("test planet")
print(test_planet)