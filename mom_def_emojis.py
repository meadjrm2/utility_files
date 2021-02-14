# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:51:03 2020

@author: User
"""

"""
import mom_def_emojis
mom_def_emojis.emojis()
simple_smile = mom_def_emojis.simple_smile
emoji_money_mouth_face = mom_def_emojis.money_mouth_face
emoji_thumbs_up = mom_def_emojis.thumbs_up
emoji_robot = mom_def_emojis.robot
"""




def emojis():
    global money_mouth_face
    global thumbs_up
    global simple_smile
    global bottle_with_popping_cork
    global flying_saucer
    global trophy
    global money_bag
    global pound_banknote
    global credit_card
    global computer
    global winged_money
    global warning
    global no_entry
    global prohibited
    global eyes
    global bomb
    global pile_of_poo
    global disappointed_face
    global nerd_face
    global robot
    global alien_monster
    global technologist
    global chart_up
    global chart_down
    global halloween_pumpkin
    global ghost
    global christmas_tree
    global fireworks
    global abacus
    global egg_timer

    #Celebration
    money_mouth_face = '\N{money-mouth face}'
    thumbs_up = '\N{thumbs up sign}'
    trophy = '\N{trophy}'
    simple_smile = '\N{grinning face}'
    bottle_with_popping_cork = '\N{bottle with popping cork}'
    
    #Disappointment
    bomb = '\N{bomb}'
    pile_of_poo = '\N{pile of poo}'
    disappointed_face = '\N{disappointed face}'
    
    #Robots
    flying_saucer = '\N{flying saucer}'
    computer = '\U0001F4BB'
    robot = '\U0001F916'
    alien_monster = '\N{alien monster}'
    technologist = '\U0001F9D1'
    
    #Money
    money_bag = '\N{money bag}'
    pound_banknote = '\U0001F4B7'
    credit_card = '\N{credit card}'
    winged_money = '\U0001F4B8'	
    
    #Warnings
    warning = '\U000026A0'
    no_entry = '\N{no entry}'
    prohibited = '\U0001F6AB'
    
    #Buy / Sell
    chart_up = '\U0001F4C8'
    chart_down = '\U0001F4C9'
    egg_timer = '\U000023F3'
    
    #Other
    eyes = '\N{eyes}'
    nerd_face = '\N{nerd face}'
        
    #Seasonal
    halloween_pumpkin = '\U0001F383'
    ghost = '\U0001F47B'
    christmas_tree = '\U0001F384'
    fireworks = '\U0001F386'
    abacus = '\U0001F9EE'
    
    #print(technologist)
    

"""
Unicodes:
To use Unicodes , we need to replace “+” with “000” from the list of unicodes .
For example :
“U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it.
eg winking face = 'winking face' or U-1F609
print('\N{winking face}')
print('\U0001F609')
"""