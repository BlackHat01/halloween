# Corey Miller
# Victor Pallares
# Matt Gonzalez
# Period 4

# Halloween Project - Junkenstein's Revenge

# Start of game.
# Import these two for the exit at the end and the sleeps.
import time
import sys
# to use the pygame module for the sound bits
from pygame import mixer

# Introductory main function
def main():
    print("This game conatins sound bits. Please ensure volume is on. Enjoy Junkenstein's Revenge, which is heavily based off Overwatch's story.")
    time.sleep(6)
    mixer.init()
    mixer.music.load('intro.wav')
    mixer.music.play()
    time.sleep(1)
    print("""Our tale begins in Adlersbrunn, where the lord of the castle has called for""")
    time.sleep(4.8)
    print("""heroes to come to his aide, and defend him against the mad doctor Junkenstein.""")
    time.sleep(6.8)
    print("""Our tale is about to begin...""")
    time.sleep(6.8)
    print("""Dr. Junkenstein laughed as his minions arose for tonight was the night of""")
    time.sleep(6.2)
    print("""Junkenstein's Revenge!""")
    time.sleep(5)
    selectHero()

# This is where the user can select their hero of choice. Has little effect on outcome of the game.
def selectHero():
    mixer.music.load('intro2.ogg')
    mixer.music.play()
    time.sleep(1)
    hero = input("""
    Select your hero

        Soldier 76
        Mccree
        Ana
        Hanzo

    (Enter exact name): """)
    if hero == ("Mccree"):
        heroName=("Mccree")
        soundString=("mccree.ogg")
        heroString=("The wandering Gunslinger, seeking adventure.")
    elif hero == ("Ana"):
        heroName=("Ana")
        soundString=("ana.ogg")
        heroString=("The reclusive Alchemist, skilled in the healing arts.")
    elif hero == ("Soldier 76"):
        heroName=("Soldier: 76")
        soundString=("soldier.ogg")
        heroString=("The nameless soldier, veteran of countless battles.")
    elif hero == ("Hanzo"):
        heroName=("Hanzo")
        soundString=("hanzo.ogg")
        heroString=("An archer from the east, trying to escape his past.")
    # These elses appear throughout to prevent invalid input from breaking the game
    else:
        print("Invalid selection.")
        selectHero()
    mixer.music.load(soundString)
    mixer.music.play()
    print(heroString)
    time.sleep(5)
    roundOne(heroName)

# This is the first round. The correct answer is either.
def roundOne(heroName):
    zomnicOne = int(input("""
    Zomnics approach the gate you must protect.
    Will you:
                      
        1. Attack
        2. Let teammates attack

    (Enter choice number): """))
    print("The first of the zomnics have been destroyed.")
    time.sleep(2)
    roundTwo(heroName)

# This is the second round. The correct answer is 1
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
            mixer.music.load('zomnics.ogg')
            mixer.music.play()
            print("Dr. Junkenstein's zomnics hurled themselves at the doors of the castle. You have failed.")
            time.sleep(6)
            end()
        elif zomnicTwo == 3:
            mixer.music.load('failed.ogg')
            mixer.music.play()
            print("The zomnics fall, but the zombardier targets you, and you fall. You have failed.")
            time.sleep(8)
            end()
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
            mixer.music.load('failed.ogg')
            mixer.music.play()
            print("The zomnics fall, but the zombardier targets you, and you fall. You have failed.")
            time.sleep(8)
            end()
        else:
            print("Invalid selection.")
            roundTwo(heroName)

# This is the final round. The correct answer is 2
def bossBattle(heroName):
    mixer.music.load('junk.wav')
    mixer.music.play()
    print("As the battle raged, Dr. Junkenstein himself made a grand appearance!")
    time.sleep(7.5)
    print("You will all regret the day you laughed at Dr. Jamison Junkenstein!")
    time.sleep(6)
    mixer.music.load('hoarde.ogg')
    mixer.music.play()
    finalBattle = int(input("""
    Dr. Junkenstein lobs his bombs from the balcony, while the zomnics swarm towards the castle.
    Will you:
 
    1. Focus your team on on Dr. Junkstein
    2. Attack the zomnics

    (Enter choice number): """))
    if finalBattle == 2:
        time.sleep(1)
        mixer.music.load('junkdeath.ogg')
        mixer.music.play()
        print("With one last laugh, Dr. Junkenstein fell from the balcony to the flagstones below.")
        time.sleep(8)
        print("And as the last of his laughter echoed from the walls of the castle,")
        time.sleep(6)
        print("the battle was over, and the castle had been saved.")
        time.sleep(5.8)
        mixer.music.load('win.ogg')
        mixer.music.play()
        print("The defenders were victorious and Dr. Junkenstein's reign of terror . . .")
        time.sleep(8)
        print("was at an end.")
        time.sleep(3)
        print("The lord of the castle thanks you,",(heroName),", for your bravery in defending his castle.")
        time.sleep(4)
        end()
        
    elif finalBattle == 1:
        mixer.music.load('failed.ogg')
        mixer.music.play()
        print("While you are distracted, zomnics sneak by, and break down the door! You have failed.")
        time.sleep(8)
        end()
        
    else:
            print("Invalid selection.")
            bossBattle(heroName)
# Allows seamless transition to the start of the game again.
def end():
        mixer.music.load('end.ogg')
        mixer.music.play()
        reset = input("The end! Would you like to play again? [y/n]: ")
        if reset == ("y"):
            print("""

Restarting...


""")
            main()
        else:
            sys.exit("Thank you for playing!")
# Call main!
main()


