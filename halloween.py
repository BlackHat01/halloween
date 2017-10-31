# Corey Miller
# Victor Pallares
# Matt Gonzalez
import time
import sys
from pygame import *
mixer.init()

def main():
    
    mixer.music.load('intro.ogg')
    mixer.music.play()

while mixer.music.get_busy():
    
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
    time.Clock().tick(10)
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
        heroString=("The wandering Gunslinger, seeking adventure.")
    elif hero == ("Ana"):
        heroName=("Ana")
        heroString=("The reclusive Alchemist, skilled in the healing arts.")
    elif hero == ("Soldier 76"):
        heroName=("Soldier: 76")
        heroString=("The nameless soldier, veteran of countless battles.")
    elif hero == ("Hanzo"):
        heroName=("Hanzo")
        heroString=("An archer from the east, trying to escape his past.")
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
def bossBattle(heroName):
    print("As the battle raged, Dr. Junkenstein himself made a grand appearance!")
    time.sleep(3)
    print("You will all regret the day you laughed at Dr. Jamison Junkenstein!")
    time.sleep(3)
    finalBattle = int(input("""
    Dr. Junkenstein lobs his bombs from the ramparts, while zomnics zerg towards the gate.
    Will you:

    1. Attack the zomnics
    2. Focus your team on on Dr. Junkstein

    (Enter choice number): """))
    if finalBattle == 1:
        time.sleep(2)
        print("""

    You manage to avoid the flying bombs landing around you, and save the door.
    However, The bombs keep coming from the ramparts. You and your team focus your
    attack on Dr. Junkenstein and at last, he falls from the ramparts, cold and dead.
    """)
        time.sleep(8)
        print("The lord of the castle thanks you,",(heroName),", for your bravery in defending his castle.")
        time.sleep(5)
        reset = input("The end! Would you like to play again? [y/n]: ")
        if reset == ("y"):
            main()
        else:
            sys.exit("Thank you for playing!")
    
    elif finalBattle == 2:
        print("While you are distracted, zomnics sneak by, and break down the door! You have failed.")
        time.sleep(3)
        main()
main()


