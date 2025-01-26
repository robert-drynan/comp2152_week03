import random
#dice opt using the list and range
diceOptions = list(range(1, 7))
# weapons
weapons = ["fist", "Knife", "club", "Gun", "Bomb", "Nuke"]
print("Available weapons: ")
for w in weapons:
    print(w)
def get_combat_strength(prompt):
    while True:
        try:
            strength = int(input(prompt))
            if 1 <= strength <= 6:
                return strength
            else:
                print("Please enter a number between 1 and 6")
        except ValueError:
            print("Please enter a number between 1 and 6")
combatStrength = get_combat_strength("Please enter a number between 1 and 6: ")
monsterCS = get_combat_strength("Please enter a number between 1 and 6 for the monster: ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = monsterCS + monsterRoll

    print(f"\nHero roll: {heroRoll}")
    print(f"\nHero selected: {heroWeapon}")
    print(f"\nMonster roll: {monsterRoll}")
    print(f"\nMonster selected: {monsterWeapon}")
    print(f"\nHero Total: {heroTotal}")
    print(f"\nMonster Total: {monsterTotal}")
    if heroTotal > monsterTotal:
        print("\nYou won!")
    elif monsterTotal > heroTotal:
        print("\nYou lost!")
    else:
        print("\nTie")

if j != 11:
    print(f"\n Battle concluted after 20 rounds")