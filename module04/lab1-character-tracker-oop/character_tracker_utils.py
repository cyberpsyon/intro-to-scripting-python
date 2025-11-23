# Author: Ben Mickens
# Due Date: 11-16-2025
# Function: The program contains the character class

class GameCharacter:

    # Initialize GameCharacter
    def __init__(self, name, character_class, health, xp):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.xp = xp

    def __str__(self):
        return f"Name: {self.name} | Class: {self.character_class} | Health: {self.health} | XP: {self.xp}"

    # Displays the character's information and attributes
    def display_info(self):
        print(self)

    # Adds xp to the character
    def gain_xp(self, amount):
        self.xp += amount

    # Increase character's health by 10 and resets xp
    def level_up(self):
        self.health += 10
        self.xp = 0