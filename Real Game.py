#Author-Leo Barcenas
#Date-4/25/25
#Title-Boss Battle
#Random is imported to make the attacks have a range istead of a difinite value
import random

def game():
    print("Welcome To My Game")
    name = input("What is your name?")
    print("Hello " + name + )
#Health for both Entity
    boss_health = 1000
    hero_health = 100

    hero_attacks = ["Sword Attack", "Holy Boost", "Heal"]

    def boss_turn():
        nonlocal hero_health
        boss_attack = random.choice(["Bite", "Fire"])
        if boss_attack == "Bite":
            damage = random.randint (5,10)
            print("Boss attacks with Bite, dealing", damage, "damage.")
        elif boss_attack == "Fire":
            damage = random.randint (10,20)
            print("Boss attacks with Fire, dealing", damage, "damage.")
        hero_health -= damage
        print("Hero Health:", hero_health)

    def hero_turn():
        nonlocal boss_health, hero_health
        print("\nYour turn. Choose your attack:")
        for i, attack in enumerate(hero_attacks):
            print(f"{i + 1}. {attack}")

        while True:
            try:
                choice = int(input("Enter the number of your attack: "))
                if 1 <= choice <= len(hero_attacks):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(hero_attacks))
            except ValueError:
                print("Invalid input. Please enter a number.")

        attack_choice = hero_attacks[choice - 1]

        if attack_choice == "Sword Attack":
            damage = 100
            print("Hero attacks with Sword, dealing", damage, "damage.")
            boss_health -= damage
        elif attack_choice == "Holy Boost":
            # Assuming Holy Boost is intended to boost the next attack, not deal damage
            print("Hero uses Holy Boost, increasing next attack damage.")
            # Implement boost logic for the next attack
            damage = 150
            print("Hero attacks with boosted Sword, dealing", damage, "damage.")
            boss_health -= damage
        elif attack_choice == "Heal":
            #Heal count= 3
            #Only able to use 3 heals
            heal_amount = 50
            hero_health += heal_amount
            print("Hero heals for", heal_amount, "health.")
            print("Hero Health:", hero_health)

        print("Boss Health:", boss_health)

    while boss_health > 0 and hero_health > 0:
        hero_turn()
        if boss_health <= 0:
            print("Hero wins! You defeated the Dragon.")
            break
        boss_turn()
        if hero_health <= 0:
            print("Boss wins! You were defeated by the Dragon.")
            break
        print("-" * 20)  # Separator for turns


# Start the game
game()