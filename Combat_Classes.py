from random import choice

names = ("Bob", "Frank", "Dick", "Dave", "Rick", "Vito", "Chester", "Chad")

# CREATING A CLASS

class Enemy:
    def __init__(self, species, level):    # Initializes a new instance of a class
        self.species = species    # self relates to the new instance itself
        self.level = level
        self.name = choice(names)
        self.hp = 10 * self.level

    def __str__(self):    # Returns a string representation of an object
        return "A " + self.species + " " + self.name + " approaches! It has " + str(self.hp) + " HP!"

    def get_hp(self):
        return self.hp
        
skeleton1 = Enemy("skeleton", 1)
minotaur1 = Enemy("minotaur", 5)

print(skeleton1)
print(minotaur1)



# CREATING A SUBCLASS

class Boss(Enemy):    # Subclass inherits all functions from superclass which can be overwritten
    def fireball(self, target):
        target.hp -= 10
        print(self.species + " " + self.name + " casts Fireball! " + target.name + " loses 10 HP!")
        
    def __str__(self):
        return "A " + self.species + " " + self.name + " approaches! It has " + str(self.hp) + " HP! It's humongous!"

skele_king = Boss("Skeleton King", 20)

print(skele_king)



# EXAMPLE OF USING CLASSES: CASTING FIREBALL:

print("----- WELCOME TO THE ARENA! -----")
print(minotaur1)
print(skele_king)

skele_king.fireball(minotaur1)    # Skeleton King casts Fireball on Minotaur

print("Current health of " + minotaur1.species + " " + minotaur1.name + ": " + str(minotaur1.get_hp()))
