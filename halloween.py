# Corey Miller
# Victor Pallares
# Matt Gonzalez
import time
import sys
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
    elif hero == ("Ana"):
        heroName=("Mccree")
    elif hero == ("Soldier 76"):
        heroName=("Mccree")
    elif hero == ("Hanzo"):
        heroName=("Mccree")
    else:
        print("Invalid selection.")
        selectHero()
        
selectHero()
 
