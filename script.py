#PLANET DISCOVERY TERMINAL GAME
import random

#Player
class Player:
    def __init__(self, name, r_sys):
        self.name = name
        self.r_sys = r_sys
    def __repr__(self):
        return f"Your name is {self.name} and your respiratory system is {self.r_sys} based."
    

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
        self.atmosphere = atmosphere
        self.temperature = temperature
        self.gravity = gravity
        


#defining player: definire la variabile input per name respiratorio e le due variabili per sist. resp. poi inserirle nell'oggetto player
test_player = Player("a", "b")  
print(test_player)

#defining spaceship
test_spaceship = Spaceship("Test")
print(test_spaceship)