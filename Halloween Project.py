#====================
# Developed by Corey Miller
# Period 3
# 11/4/15
# Halloween Project
#====================
import time
import sys
def start():
    #Starting function
    print ('The Haunted House v3.2 final-release, Developed by Corey Miller. Copyright 2015. All rights reserved.')
    time.sleep(2)
    print ("You're going to be going through the house and the goal is to make it out.")
    print ('*1987*')
    time.sleep(1)
    print ('You have to input "1" to use the first option or "2" for the second option.')
    ready = input ('Ready? Press ENTER to begin!')
    time.sleep(1)
    print ('Loading spooky, scary skeletons...')
    time.sleep(3)
    print ('Adding soundtrack "2spooky5me.mp3"...')
    time.sleep(3)
    front_door()
def front_door():
    #Person enters through front door
    print ('You walk in through the creaky, front door, and sneak in after the haunted house hours are closed...')
    time.sleep(2)
    print ('You creep down the main hall way with the creaky floorboards under your feet squealing. You found a flashlight on a desk in the hall.')
    time.sleep(2)
    #First scenario
    s_1 = input ('You see a figure approaching from the darkness ahead... Hide or Shine your light on it? ')
    if s_1 == '1':
        print ('You hide under the desk in the hall.')
        time.sleep(2)
        hall()
    elif s_1 == '2':
        print ('The shadow disperses quickly...')
        time.sleep(2)
        print ('You feel a tap on your shoulder...')
        time.sleep(2)
        print (':(')
        time.sleep(2)
        return front_door()
    else:
        print ('The shadow disperses quickly...')
        time.sleep(2)
        print ('You feel a tap on your shoulder...')
        time.sleep(2)
        print (':(')
        time.sleep(2)
        return front_door()
            
def hall():
    print ('The footsteps slow, then fade away.')
    time.sleep(2)
    s_2 = input ('Stay hidden or emerge from hiding spot? ')
    if s_2 == '1':
        time.sleep(2)
        print ('A dark head shape slowly looks under the desk...')
        time.sleep(2)
        print(':(')
        time.sleep(2)
       
        return front_door()
    else:
        #Person is going down the hall
        print ('You continue down the hall and approach two doors with a candle on the wall...')
        time.sleep(2)
        doors_1()
def doors_1():
    #Person has option to take candle/go through right or left door
    time.sleep(1)
    s_3 = input ('Take candle for flash light or keep flashlight? ')
    if s_3 == '1':
        print('You take the candle')
        time.sleep(2)
        doors_2_1()
    elif s_3 == '2':
        print('You kept your flashlight.')
        time.sleep(2)
        doors_2()
    else:
        print('You keep the flashlight')
        time.sleep(2)
        doors_2()
def doors_2_1():
        s_4 = input('Which door do you go through, right or left? ')
        if s_4 == '1':
            print("It's locked...")
            time.sleep(1)
            return doors_2_1()
        else:
            print('The door creaks open...')
            time.sleep(2)
            print('A sudden gust of wind blows your candle out...')
            time.sleep(2)
            hall2_1()
def hall2_1():
    #This is when person takes candle
    s_5 = input('You continue into the hall with a blown out candle. You follow up a flight of stairs. Footsteps are heard at the bottom of the stairs. Investigate or Continue? ')
    if s_5 == '1':
        time.sleep(2)
        print('You go back down the shaky stairs.')
        time.sleep(1)
        print('A figure is seen creeping up the stairs.')
        s_6 = input('You find some purple fluid on the ground, splash some at it or keep walking at it?')
        if s_6 == '2':
            print ('The figure turns around and vanishes down the hallway again.')
            time.sleep(1)
            print ('You turn around and see the creature staring at you...')
            time.sleep(1)
            print (':(')
            time.sleep(1)
            return front_door()
        else:
            print ('The ghost screams and vanishes.')
            time.sleep(2)
            print ('You aproach a code locked door, but it has already been unlocked. You walk through it. ')
            time.sleep(2)
            s_7 = input ('There is portal on the ground.  Jump in or put the fluid into  it?')
            if s_7 =='1':
                time.sleep(2)
                print ('You fall into a pit of death. Great idea idiot.')
                return front_door()
            else:
                print ('The image on the portal morphs into an image of your bedroom. You jump in.')
                time.sleep(2)
                print ('You appear in you room, but the portal is still in your room.')
                time.sleep(2)
                s_8 = input ('Pour the rest of the fluid on it or let it be? ')
                if s_8 =='1':
                    print ('You pour the fluid on it, and go to bed.')
                    time.sleep(5)
                    print ('You wake up and the portal is gone, but...there are bloody footprint from where the portal was, leading to your closet...')
                    time.sleep(3)
                    end_1()
                else:
                    print ('You let it be and go to bed.')
                    time.sleep(5)
                    print ('You wake up, and all seems good. What a night!.')
                    time.sleep(3)
                    end_2()
    else:
        print('You continue up the stairs. The figure appears again. It is holding a bloody knife.')
        time.sleep(2)
        print (':(')
        return front_door()
def doors_2():
    #This is if the person keeps flashlight
    s_4 = input('Which door do you go through, right or left?')
    time.sleep(2)
    if s_4 == '1':
        print("It's locked...")
        time.sleep(2)
        doors_2()
    elif s_4 == '2':
        print('The door creaks open...')
        time.sleep(1)
        print('A sudden gust of wind blows by...')
        time.sleep(2)
        hall2()
def hall2():
    s_5 = input('You continue into the hall with the flashlight. You follow up a flight of stairs. Footsteps are heard at the bottom of the stairs. Investigate or Continue? ')
    if s_5 == '1':
        time.sleep(2)
        print('You go back down the shaky stairs.')
        time.sleep(1)
        print('A figure is seen creeping up the stairs.')
        time.sleep(2)
        s_6 = input('Shine your light at it or keep walking at it?')
        if s_6 == '1':
            time.sleep(2)
            print ('The figure turns around and vanishes down the hallway again.')
            time.sleep(1)
            print ('You turn around and see the creature staring at you...')
            time.sleep(1)
            print (':(')
            time.sleep(1)
            return front_door()
        else:
            print('You walk up to the creature. It leads you to a code locked door.')
            time.sleep(2)
            code = input('Enter the 4 - digit code, I swear I have seen a 4 digit number somewhere...: ')
            if code == '1987':
                time.sleep(2)
                print ('The lock clicks. Good job, detective.')
                time.sleep(2)
                doors_3()
            else:
                print ('The screen on the lock prints:":("')
                time.sleep(2)
                print ('The creature pulls out a blade...')
                time.sleep(1)
                return front_door()
def doors_3():
    #Portal room with flashlight
    print ('There is portal on the ground. It seems to lead to a pit.')
    time.sleep(2)
    print ('The creature behind you closes in on you. You jump with no other option.')
    time.sleep(2)
    print ('You fall into a pit of death.')
    time.sleep(2)
    print (':(')
    time.sleep(2)
    return front_door()
def end_1():
    end = input('Congrats, you reached the end, but not the good one...restart by entering "1" or exit by entering "2"')
    if end =='1':
        time.sleep(2)
        return front_door()
    else:
        print ('Unloading spooky stuffs...')
        time.sleep(2)
        sys.exit('Thanks for playing!')
def end_2():
    end = input('Congrats, you reached the end, and it was the good ending!...restart by entering "1" or exit by entering "2"')
    if end =='1':
        return front_door()
    else:
        print ('Unloading spooky stuffs...')
        time.sleep(2)
        sys.exit('Thanks for playing!')
                     
def main():
    start()

main()
            
        
            
