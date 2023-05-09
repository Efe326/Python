import classes
def event1():
    print("You found a small chest. It contains some coins.")

def event2():
    print("You see a wounded traveler. He asks for your help.")
    help = input("help him?(y/n)")
    if help != "y":
        print("The traveler slowly closes his eyes and dies from his wounds...")
    elif help == "y":
        print("you reach out to help him...")
        print("he suddenly strikes against you!")
        print(" a fight starts.")
        bandit_attack = 100
        bandit_defense = 50



def event3():
    print("You stumble upon a hidden room. It's full of treasures!")