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

    #da implementare un po' di logica... domani - valutare rimozione del blocco else
    

#Spaceship        
class Spaceship:
    def __init__(self, name):
        self.name = name
        self.storage = 3
        self.fuel = 0
        self.equipment = 0
        self.has_storage = True
        self.has_fuel = True
    
    def __repr__(self):
        return f"Welcome on board! You are on the {self.name} spaceship."

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
test_spaceship = Spaceship("Test")
print(test_spaceship)

#defining planet
test_planet = Planet("test planet")
print(test_planet)