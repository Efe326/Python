import random
from classes import Guard
from classes import Sniper
from classes import Caster
from classes import Defender
import Events
import os

print("Welcome to Darknights!")
username = input("please enter a username")


events_list = [Events.event1, Events.event2, Events.event3]

def continue_story():
    if events_list:
        event = random.choice(events_list)
        events_list.remove(event)
        event()


print("Hello there", username ,"please select a class to play as:")
print("1:Guard")
print("2:Sniper")
print("3:Caster")
print("4:Defender")

c1 = int(input("Please choose 1-4:"))

if c1 == 1:
    character = Guard(username, 2000, 400, 200, 5, "physical")
    print("Great,", username, "you chose the Guard class. This class is good in most situations")
    print("the stats are:")
    print("HP:",  character.hp)
    print("Attack", character.attack)
    print("physical defense and arts defense:", character.defense, ",", character.art_defense)
    print("damage type:", character.dmgtpye)
    print("let's start!")
elif c1 == 2:
    character = Sniper(username, 1500, 550, 120, 5, "physical")
    print("Great,", username, "you chose the Sniper class. This class is good in damage but a bit fragile.")
    print("the stats are:")
    print("HP:", character.hp)
    print("Attack", character.attack)
    print("physical defense and arts defense:", character.defense, ",", character.art_defense)
    print("damage type:", character.dmgtpye)
    print("let's start!")
elif c1 == 3:
    character = Caster(username, 1500, 450, 120, 15, "Arts")
    print("Great,", username, "you chose the Caster class. This class is useful if you want arts damage.")
    print("the stats are:")
    print("HP:", character.hp)
    print("Attack", character.attack)
    print("physical defense and arts defense:", character.defense, ",", character.art_defense)
    print("damage type:", character.dmgtpye)
    print("let's start!")
elif c1 == 4:
    character = Defender(username, 4000, 250, 350, 10, "physical")
    print("Great,", username, "you chose the Defender class. This class is very tanky and will come in handy.")
    print("the stats are:")
    print("HP:", character.hp)
    print("Attack", character.attack)
    print("physical defense and arts defense:", character.defense, ",", character.art_defense)
    print("damage type:", character.dmgtpye)
    print("let's start!")

devam = int(input("press '1' to continue."))
if devam == 1:
        print("You woke up on a grassy hill next to a road. You don't know where you are and why you are here")
        print("but you know that you were trying to reach somewhere and the reason was very important.")
        print("you start walking...")
        continue_story()













