'Name: Joel Murphy
'Date: May 16, 2013
'Program: Assignment 1
'Version: 1.00 May 23, 2013
'Description: Text based adventure.
'             Just finished the outline of choices, have a better
'             idea of what I want.
'             Wrote out a lot of choices, going to try to start piecing
'             them together.

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

def choice_0():
    ch = '0'
    while ch != '1' and ch != '2':
    	print ('What will you do?')
    	print ('1. Grab the gun and try to take the Metarchs out.')
    	print ('2. Just lay there and hope they don\'t kill you.')
    	ch = raw_input()
    return ch

def choice_a():
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
    time.sleep(2)
    print
    time.sleep(2)
    print
    time.sleep(2)
    print
    print ('You wake up in a hospital bed with your right hand cuffed to the bed.')
    print ('There\'s a doctor nearby with his back to you. There is a tray next')
    print ('to the bed with a few scalpels, some gauze, some thread, a needle for')
    print ('thread and a pair of scissors.')
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5' and ch != '6' and ch != '7':
    	print ('What will you do?')
    	print ('1. Do Nothing')
    	print ('2. Grab a scalpel')
    	print ('3. Grab some gauze')
    	print ('4. Grab some thread')
    	print ('5. Grab a needle')
    	print ('6. Grab the scissors')
    	print ('7. Try and convince the doctor to let you go')
    	ch = raw_input()
    return ch

def standard3():
    print ('What will you do?')
    print ('1. Don\'t say anything to him')
    print ('2. Tell him where the artifact is')
    print ('3. Tell him you don\'t know anything about an artifact')

def doc4():
    print ('What will you do?')
    print ('1. Don\'t say anything to him')
    print ('2. Give in and tell him where the artifact is')
    print ('3. State the consequences of it bing in his bosses hands')
    print ('4. Ask him to release you')

def doc3():
    print ('What will you do?')
    print ('1. Ask him if he can release you now')
    print ('2. Ask him what kind of doctor he is')
    print ('3. Don\'t say anything to him')

def leader5():
    print ('What will you do?')
    print ('1. Don\'t say anything to him')
    print ('2. Insult him')
    print ('3. Lie about where the artifact is')
    print ('4. Tell him where the artifact is')
    print ('5. Tell him you don\'t know anything about an artifact')

def choice_b():
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
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3':
    	standard3()
    	ch = raw_input()
    return ch

def doctor1(n):
    if n == 2:
        print ('You grab a scalpel from the tray without the doctor noticing.')
    elif n == 3:
        print ('You grab some gauze from the tray without the doctor noticing.')
    elif n == 4:
        print ('You grab some thread from the tray without the doctor noticing.')
    elif n == 5:
        print ('You grab the needle from the tray without the doctor noticing.')
    elif n == 6:
        print ('You grab the scissors from the tray without the doctor noticing.')
    
    print ('The doctor sees that you\'re awake now and smiles at you.')
    print ('"I\'m much kinder than my boss so if you wouldn\'t mind telling')
    print ('me where the artifact is I can see that he doesn\'t hurt you."')
    print
    time.sleep(2)

def doctor2():
    print ('"I\'m afraid I don\'t have that kind of athourity, but I\'m')
    print ('sure if you co-operate the boss will let you go. So, where\'s')
    print ('that artifact?"')
    print
    time.sleep(2)

def doctor3():
    print ('The doctor\'s face becomes sad "I\'m afraid of what the boss')
    print ('might do to you if you don\'t cooperate. If you can just tell')
    print ('us where the artifact is, so many lives can be saved!"')
    print
    time.sleep(2)

def doctor4():
    print ('The doctor\'s face becomes happy. "Oh thank you very much!')
    print ('That artifact will greatly enhance my work!"')
    print
    time.sleep(2)

def doctor5(n):
    print ('You pull the doctor in close')
    if n == 2:
        print ('and hold the scalpel against his neck.')
    elif n == 4:
        print ('and quickly wrap the thread around his neck pulling tight.')
    print ('"Wha-What do you want??" asks the scared doctor.')
    print
    time.sleep(2)

def doctor6(n):
    print ('The doctor glances at the tray and hesitates. In a less friendly')
    print ('tone he says, "How about you tell me where the artifact is."')
    print
    time.sleep(2)

def choice_c_e(n):
    doctor1(n)
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3':
    	standard3()
    	ch = raw_input()
    return ch

def choice_d(n):
    doctor1(n)
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	standard3()
    	print ('4. Lure him close and threaten him with the scalpel')
    	ch = raw_input()
    return ch

def choice_f(n):
    doctor1(n)
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	standard3()
    	print ('4. Lure him close and threaten him with the thread')
    	ch = raw_input()
    return ch

def choice_g(n):
    doctor1(n)
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	standard3()
    	print ('4. Lure him close and threaten him with the needle')
    	print ('5. Get him to look away')
    	ch = raw_input()
    return ch

def choice_h(n):
    doctor1(n)
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	standard3()
    	print ('4. Lure him close and threaten him with the scissors')
    	ch = raw_input()
    return ch

def choice_i():
    doctor2()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	standard3()
    	print ('4. Tell him he can come with you')
    	ch = raw_input()
    return ch

def choice_j_ar():
    print ('"I have ways of helping you talk." He calls over a couple')
    print ('of soldiers who come over and cover your head in a black hood.')
    print
    time.sleep(2)
    print ('When the hood is removed you find yourself sitting on a wooden')
    print ('chair in a dingy cell. There\'s a table and another chair infront')
    print ('of you. The leader walks in and sits down across from you.')
    print ('"Have you found your tongue yet? Where\'s the artifact?"')
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
        leader5()
        ch = raw_input()
    return ch

def choice_k_aq():
    print ('"Good! You\'ve made the right choice. You two! Come over here!"')
    print ('The leader motions for two soldiers to come over. "You will be')
    print ('showing us exactly where it is."')
    print
    time.sleep(2)
    print ('You get up to your feet fully aware that what you will guide the')
    print ('Metarchs to will be the cause of your country\'s destruction.')
    print ('An artifact that can destroy hundreds of men in a single use, or')
    print ('animate the dead into midless soldiers should have been destroyed')
    print ('long ago.')
    print
    time.sleep(2)
    print ('Oh well, at least you\'re not the one dying... yet.')

def choice_l():
    print ('BANG!')
    print
    time.sleep(2)
    print ('The bullet flew into the dirt between your legs, clearly on')
    print ('purpose. "Did that jog your memory a bit? I\'ll ask once more,')
    print ('"Where is the artifact??"')
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3':
        print ('What will you do?')
        print ('1. Insist you don\'t know what he\'s talking about')
        print ('2. Tell him where it is')
        print ('3. Don\'t say anything to him')
        ch = raw_input()
    return ch

def choice_m_ag():
    doctor3()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc4()
    	ch = raw_input()
    return ch

def choice_n_ah():
    doctor4()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3':
    	doc3()
    	ch = raw_input()
    return ch

def choice_o_r_v_z_ae_ai():
    print ('The doctor looks a little concerned, "Is your memory alright?"')
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3':
        print ('What will you do?')
        print ('1. Tell him you can\'t remember anything before the crash')
        print ('2. Tell him it\'s fine')
        print ('3. Tell him your head is hurting')
        ch = raw_input()
    return ch

def choice_p():
    doctor3()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	doc4()
    	print ('5. Lure him close and threaten him with the scalpel')
    	ch = raw_input()
    return ch

def choice_q():
    doctor4()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc3()
    	print ('4. Lure him close and threaten him with the scalpel')
    	ch = raw_input()
    return ch

def choice_s():
    doctor5()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	print ('What will you do?')
        print ('1. Tell him you want to be released')
        print ('2. Slice his throat')
        print ('3. Tell him you want a gun')
    	ch = raw_input()
    return ch

def choice_t():
    doctor3()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	doc4()
    	print ('5. Lure him close and threaten him with the thread')
    	ch = raw_input()
    return ch

def choice_u():
    doctor4()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc3()
    	print ('4. Lure him close and threaten him with the thread')
    	ch = raw_input()
    return ch

def choice_w():
    doctor5()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	print ('What will you do?')
        print ('1. Tell him you want to be released')
        print ('2. Pull the thread so tight it cuts through his throat')
        print ('3. Tell him you want a gun')
    	ch = raw_input()
    return ch

def choice_x():
    doctor3()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	doc4()
    	print ('5. Lure him close and threaten him with the needle')
    	ch = raw_input()
    return ch

def choice_y():
    doctor4()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc3()
    	print ('4. Lure him close and threaten him with the needle')
    	ch = raw_input()
    return ch

def choice_aa_af():
    doctor6()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc4()
    	ch = raw_input()
    return ch

def choice_ab():
    print ('You ask the doctor if he has something to help with stomach aches.')
    print ('"I think I do. Give me a second." The doctor says as he walks')
    print ('behind the curtain.')
    print
    time.sleep(2)
    ch = '0'
    while ch != '1' and ch != '2':
    	print ('Now\'s your chance!')
    	print ('1. Do nothing')
    	print ('2. Pick the handcuffs with the needle')
    	ch = raw_input()
    return ch

def choice_ac():
    doctor3()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	doc4()
    	print ('5. Lure him close and threaten him with the scissors')
    	ch = raw_input()
    return ch

def choice_ad():
    doctor4()
    ch = '0'
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc3()
    	print ('4. Lure him close and threaten him with the scissors')
    	ch = raw_input()
    return ch

def choice_aj():
    print ('The doctor thinks about it for a second, "Hmm... I\'m afraid')
    print ('I\'ll have to decline the offer, I have too much work to do here.')
    print ('So, about that artifact."')
    print
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4':
    	doc4()
    	ch = raw_input()
    return ch

def choice_ak():
    print ('He signals two soldiers over and you are beaten for a good five')
    print ('minutes. "Now, where is the artifact?"')
    print
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	leader5()
    	ch = raw_input()
    return ch

def choice_al():
    print ('He laughs at you and signals two soldiers over and you are')
    print ('beaten for a good five minutes. "Now, where is the artifact?"')
    print
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	leader5()
    	ch = raw_input()
    return ch

def choice_am():
    print ('You tell him it\'s in a specific part of your ship. "I know it is')
    print ('nowhere on that ship." He signals two soldiers over and you are')
    print ('beaten for a good five minutes. "Now, where is the artifact?"')
    print
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	leader5()
    	ch = raw_input()
    return ch

def choice_ao():
    print ('You tell him you don\'t know. "I think you do know where it is."')
    print ('He signals two soldiers over and you are beaten for a good five')
    print ('minutes. "Now, where is the artifact?"')
    print
    time.sleep(2)
    while ch != '1' and ch != '2' and ch != '3' and ch != '4' and ch != '5':
    	leader5()
    	ch = raw_input()
    return ch

def choice_an():
    print ('"See, was that so hard? Now you will be showing us exactly where')
    print ('it is." Motioning for you to follow him and his men out of the room.')
    print
    time.sleep(2)
    print ('You get up off the chair fully aware that what you will guide the')
    print ('Metarchs to will be the cause of your country\'s destruction.')
    print ('An artifact that can destroy hundreds of men in a single use, or')
    print ('animate the dead into midless soldiers should have been destroyed')
    print ('long ago.')
    print
    time.sleep(2)
    print ('Oh well, at least you\'re not the one dying... yet.')

def choice_ap():
    print ('You tell him you don\'t know about the artifact. The leader sighs,')
    print ('"Well I guess I don\'t have much use for you then."')
    print ('BANG! BANG!')
    time.sleep(2)
    print ("You are dead!")


'There are sooo many choices to list them all.
def main():
    displayIntro()
    ch = choice_0()
    if ch == '1':
        item = choice_a()
        if item == '1' or item == '3':
            ch = choice_c_e(item)
            if ch == '1':
                ch = choice_m_ag()
            elif ch == '2':
                ch = choice_n_ah()
            elif ch == '3':
                ch = choice_o_r_v_z_ae_ai()
        elif item == '2':
            ch = choice_d(item)
            if ch == '1':
                ch = choice_p()
            elif ch == '2':
                ch = choice_q()
            elif ch == '3':
                ch = choice_o_r_v_z_ae_ai()
            elif ch == '4':
                ch = choice_s()
        elif item == '4':
            ch = choice_f(item)
        elif item == '5':
            ch = choice_g(item)
        elif item == '6':
            ch = choice_h(item)
        elif item == '7':
            ch = choice_i()
    elif ch == '2':
        ch = choice_b()
        if ch == '1':
            ch = choice_j_ar()
            if ch == '1':
                ch = choice_ak()
            elif ch == '2':
                ch = choice_al()
            elif ch == '3':
                ch = choice_am()
            elif ch == '4':
                ch = choice_an()
            elif ch == '5':
                ch = choice_ao()
        elif ch == '2':
            choice_k_aq()
            print ('Congratulations! You just killed hundreds of your countrymen.')
            print ('This is a very bad ending.')
        elif ch == '3':
            ch = choice_l()
            if ch == '1':
                choice_ap()
                print ('You Lose!')

if __name__ == "__main__": main()
