'Name: Joel Murphy
'Date: May 16, 2013
'Program: Assignment 1
'Version: 0.01
'Description: Text based adventure.

import random
import time

def displayIntro():
    print ('Your airship has just crashed into the rolling plains')
    print ('of the Metarch province.')
    print
    time.sleep(2)
    print ('The impact was felt through your entire body and has')
    print ('caused your vision to blur.')
    print
    time.sleep(2)
    print ('After a second you begin to see clearer and look over')
    print ('at your co-pilot, suddenly grateful of the aching muscles')
    print ('you see he didn\'t survive the impact.')
    print
    time.sleep(2)
    print ('Coughing helps you to notice the black smoke getting denser')
    print ('in the cabin. You pull on the emergency release and cause')
    print ('the roof to eject giving way to blue sky and more importantly,')
    print ('fresh air.')
    print
    time.sleep(2)
    print ('As you crawl out of the burning ship you look to your right')
    print ('and see some Metarch soldiers approaching. As you hit the')
    print ('ground you realize your body took more of a beating than')
    print ('previously thought.')
    print
    time.sleep(2)
    print ('You see your pistol laying next to you within arms reach.')
    print ('You are one of the best shots in your squadron, there\'s a')
    print ('chance you can take them out, or you could not show any')
    print ('aggression and hope they don\'t kill you.')

def choice1():
    ch1 = '0'
    while ch1 != '1' and ch1 != '2':
    	print ('What will you do?')
    	print ('1. Grab the gun and try to take the Metarchs out.')
    	print ('2. Just lay there and hope they don\'t kill you.')
    	ch1 = raw_input()
    return ch1

def choice1a():
    print ('You reach for your pistol, grip it tight, and swing your')
    print ('arm towards your targets.')
    time.sleep(2)
    print ('BANG!')
    time.sleep(2)
    print ('As soon as the bullet hit your shoulder the pain made you drop')
    print ('your gun.')
    time.sleep(2)
    print ('You look up to see a Metarch soldier standing over you with the')
    print ('butt of his rifle pointed at you.')
    time.sleep(2)
    print ('The last thing you remember is hearing the sound of your nose crunch.')

def choice1b():
    print ('You lay on the ground not making any sudden movements with your')
    print ('body, but you keep your head facing the Metarch soldiers, hoping')
    print ('they show "mercy" by taking you prisoner.')
    print
    time.sleep(2)
    print ('An older man with a short gray beard barks orders at the others')
    print ('as he walks towards you. He draws his gun and in a rough accent')
    print ('in the common tongue says,')
    time.sleep(2)
    print ('"You will tell me where the artifact is or I will shoot you!"')
    print
    time.sleep(2)

def choice2b():
    ch2 = '0'
    while ch2 != '1' and ch2 != '2' and ch2 != '3':
    	print ('What will you do?')
    	print ('1. Don\'t say anything to him.')
    	print ('2. Tell him where the artifact is.')
    	print ('3. Tell him you don\'t know anything about an artifact.')
    	ch2 = raw_input()
    return ch2

def choice

def main():
    displayIntro()
    ch1 = choice1()
    print (ch1)
    if ch1 == '1':
        choice1a()
    elif ch1 == '2':
        choice1b()
        ch2 = choice2b()
        

if __name__ == "__main__": main()
