############################################################################
#   DnD 5e Character Generator
#
#   Copyright: Andrew King III 2018
############################################################################

from random import *

from classes import *
#from races import *
#from skills import *
#from feats import *
#from spells import *
from attributes import *
from languages import *

#class_list = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
#adv_class_list = []
#sub_class_list = []
#homebrew_class_list = []

race_list = ['Half-Orc','Halfling','Half-Elf','Human','Tiefling','Gnome','Elf','Dwarf','Dragonborn']
adv_race_list = ['Hobgoblin','Kenku','Orc','Lizardfolk','Kobold','Tabaxi','Tortle','Triton','Yuan-Ti Pureblood','Goliath','Goblin','Genasi','Firbolg','Feral Tiefling','Bugbear','Aasimar','Aarakocra']
#sub_race_list = []
#homebrew_race_list = []

order_list = ['Lawful','Neutral','Chaotic']
moral_list = ['Good','Neutral','Evil']

#skill_list = []
#spell_list = []
#feat_list = []

class Character:
    first_name = ""
    last_name = ""
    clss = ""
    race = ""
    level = 0
    def description(self):
        desc_str = "\n %s %s is a level %d %s %s." % (self.first_name, self.last_name, self.level, self.race, self.clss)
        return desc_str

class Alignment:
    order = ""
    moral = ""
    def description(self):
        desc_str = " Alignment: %s %s" % (alignment_new_char.order,alignment_new_char.moral)
        return desc_str

#
#Instantiate character with name, race, class, alignment, and attributes
#

new_char = Character()
new_char.first_name= input("Please enter your (character's) first name: ")  #"Jack"
new_char.last_name= input("Please enter your (character's) last name: ")    #"LaLanne"
new_char.level = int(input("Please enter level: "))
new_char.race = choice(race_list)
new_char.clss = choice(class_list)

#
#Randomize character alignment
#

alignment_new_char = Alignment()
alignment_new_char.order = choice(order_list) #order_list[randint(0,2)]
alignment_new_char.moral = choice(moral_list) #moral_list[randint(0,2)]

#
#Set character attribute parameters
#

stats_new_char = Attributes()

stats_new_char.char_class = new_char.clss
stats_new_char.char_race = new_char.race

#stats_new_char.hit_points = randint(3,30)
#stats_new_char.strength = randint(1,20)
#stats_new_char.dexterity = randint(1,20)
#stats_new_char.constitution = randint(1,20)
#stats_new_char.intelligence = randint(1,20)
#stats_new_char.wisdom = randint(1,20)
#stats_new_char.charisma = randint(1,20)

stats_new_char.strength = stats_new_char.roll_4d6()
stats_new_char.dexterity = stats_new_char.roll_4d6()
stats_new_char.constitution = stats_new_char.roll_4d6()
stats_new_char.intelligence = stats_new_char.roll_4d6()
stats_new_char.wisdom = stats_new_char.roll_4d6()
stats_new_char.charisma = stats_new_char.roll_4d6()
stats_new_char.hit_points = stats_new_char.determine_hp()
    
#
#Set character language(s)
#

languages_new_char = Language()
languages_new_char.languages.append(standard_language_list[0])
languages_new_char.languages.append(choice(standard_language_list))

#
#Print newly created character details
#

print(new_char.description())
print(alignment_new_char.description())
print(stats_new_char.description())
print(stats_new_char.ability_mod())
print(languages_new_char.description())

print(stats_new_char.char_race)
print(stats_new_char.char_class)

#print random.randint(1,100)
#print(randint(1,100))

#print(new_char.description())
#print(alignment_new_char.description())
#print(stats_new_char.description())


