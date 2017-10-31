# Corey Miller
# Victor Pallares
# Matt Gonzalez
import time
import sys
from pygame import *
mixer.init()


def main():   
    mixer.music.load('sound.ogg')
    mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
    time.sleep(1)
    print("""Our tale begins in Eichenwalde where the lord of the castle has called for""")
    time.sleep(4)
    print("""heroes to come to his aid and defend him against the mad doctor Junkenstein.""")
    time.sleep(5)
    print("""Our tale is about to begin...""")
    time.sleep(3)
    print("""Dr. Junkenstein laughed as his minions arose for tonight was the night of""")
    time.sleep(5)
    print("""Junkenstein's Revenge!""")
    time.sleep(3)
    selectHero()
def selectHero():
    hero = input("""
    Select your hero

        Soldier 76
        Mccree
        Ana
        Hanzo

    (Enter exact name): """)
    if hero == ("Mccree"):
        heroName=("Mccree")
        heroString=("You have selected Mccree, the Gunslinger of the wild west.")
    elif hero == ("Ana"):
        heroName=("Ana")
        heroString=("You have selected Ana, the Alchemist who heals her fellow teammates.")
    elif hero == ("Soldier 76"):
        heroName=("Soldier: 76")
        heroString=("You have selected Soldier: 76, the Soldier who fights for what he believes in: Justice.")
    elif hero == ("Hanzo"):
        heroName=("Hanzo")
        heroString=("You have selected Hanzo, the Archer of the East who was born a dragon.")
    else:
        print("Invalid selection.")
        selectHero()
    print(heroString)
    time.sleep(3)
    roundOne(heroName)

def roundOne(heroName):
    zomnicOne = int(input("""
    Zomnics approach.
    Will you:
                      
            1. Attack
            2. Let teammates attack

    (Enter choice number): """))
    print("The first of the zomnics have been destroyed.")
    time.sleep(2)
    roundTwo(heroName)

def roundTwo(heroName):
    if heroName == ("Ana"):
        zomnicTwo = int(input("""
    More zomnics approach, and a zombardier attacks your Mccree.
    Will you:
    
    1. Heal your teammate: Mccree
    2. Kill the zombardier
    3. Kill the zomnics

    (Enter choice number): """))
        if zomnicTwo == 1:
            print("Mccree is healed, then proceeds to slay the zombardier and zomnics, alongside the two others")
            time.sleep(3)
            bossBattle(heroName)
        elif zomnicTwo == 2:
            print("The zombardier falls, but the zomnics crash against the door, breaking it down. You have failed.")
            time.sleep(2)
            main()
        elif zomnicTwo == 3:
            print("The zomnics fall, but the zombardier targets you, and you fall. You have failed.")
            time.sleep(2)
            main()
        else:
            print("Invalid selection.")
            roundTwo(heroName)
    else:
        zomnicTwo = int(input("""
    More zomnics approach, and a zombardier attacks you.
    Will you:
    
    1. Kill the zombardier
    2. Kill the zomnics

    (Enter choice number): """))
        if zomnicTwo == 1:
            print("The zombardier falls, and your teammates take care of the rest of the zomnics.")
            time.sleep(3)
            bossBattle(heroName)
        elif zomnicTwo == 2:
            print("The zomnics fall, but the zombardier targets you, and you fall. You have failed.")
            time.sleep(2)
            main()
        else:
            print("Invalid selection.")
            roundTwo(heroName)
    
main()


