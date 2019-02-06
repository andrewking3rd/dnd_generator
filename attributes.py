#
#DND 5e Attributes List
#

import math
from random import *
import classes

class Attributes:
    char_class = ""
    char_race = ""
    hit_points = 0
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    
    str_ability_mod = math.floor((strength-10)/2)
    dex_ability_mod = math.floor((dexterity-10)/2)
    con_ability_mod = math.floor((constitution-10)/2)
    int_ability_mod = math.floor((intelligence-10)/2)
    wis_ability_mod = math.floor((wisdom-10)/2)
    chr_ability_mod = math.floor((charisma-10)/2)
    
    
    def description(self):
        desc_str = " HP: \t%d \n STR: \t%d \n DEX: \t%d \n CON: \t%d \n INT: \t%d \n WIS: \t%d \n CHR: \t%d" % (self.hit_points,self.strength, self.dexterity,self.constitution,
           self.intelligence, self.wisdom,self.charisma)
        return desc_str

    def ability_mod(self):
        #str_ability_mod = math.floor((self.strength-10)/2)
        #dex_ability_mod = math.floor((self.dexterity-10)/2)
        #con_ability_mod = math.floor((self.constitution-10)/2)
        #int_ability_mod = math.floor((self.intelligence-10)/2)
        #wis_ability_mod = math.floor((self.wisdom-10)/2)
        #chr_ability_mod = math.floor((self.charisma-10)/2)

        #desc_str = " STR MOD: \t%d \n DEX MOD: \t%d \n CON MOD: \t%d \n INT MOD: \t%d \n WIS MOD: \t%d \n CHR MOD: \t%d" % (self.str_ability_mod, self.dex_ability_mod,self.con_ability_mod,self.int_ability_mod,
        #   self.wis_ability_mod,self.chr_ability_mod)
        desc_str = " STR MOD: \t%d \n DEX MOD: \t%d \n CON MOD: \t%d \n INT MOD: \t%d \n WIS MOD: \t%d \n CHR MOD: \t%d" % (self.str_ability_mod,self.dex_ability_mod,
                                                                                                                 self.con_ability_mod,self.int_ability_mod,
                                                                                                                 self.wis_ability_mod,self.chr_ability_mod)
        return desc_str
        


    #simulates d6 dice roll 4 times, then drops lowest value before totaling 
    def roll_4d6(self):
        roll_1 = randint(1,6)
        roll_2 = randint(1,6)
        roll_3 = randint(1,6)
        roll_4 = randint(1,6)
        total = 0
        rolls = [roll_1,roll_2,roll_3,roll_4]
        rolls.remove(min(rolls))

        for roll in rolls:
            total = total + roll

        return total

    #def point_buy(self):

    #calculate player HP; rolls d10 4 times, dropping lowest roll,
    #and adding constitution modifier
    def determine_hp(self):       
        roll_1 = randint(1,10)
        roll_2 = randint(1,10)
        roll_3 = randint(1,10)
        roll_4 = randint(1,10)
        total = self.con_ability_mod
        
        rolls = [roll_1,roll_2,roll_3,roll_4]
        rolls.remove(min(rolls))

        for roll in rolls:
            total = total + roll

        return total

    #
    #adjust ability score based on class
    #
    #def class_bonus(self):
        


    #def race_bonus(self):
        



