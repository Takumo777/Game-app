#Author-Leo Barcenas
#Date-4/25/25
#Title-Boss Battle
import random


print("Welcome To My Game")
name = input("What is your name?")
print("Hello " + name + " Your objective is to kill the Dragon")

Boss_Health = 1000
Bite_Attack = -10
Fire_Ball = random.randint(-20,-40)

Hero_Health = 100
Sword_Attack = -100
Holy_Boost = ("Sword_Boost")-50
Heal= Hero_Health+50
HeroAttacks = ["Sword Attack", "Holy Boost", "Heal"]

def hero_turn():
    print("\nYour turn. Choose your attack:")
