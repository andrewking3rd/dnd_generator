#
#DND 5e Language List
#

standard_language_list =    ["Common","Dwarvish","Elvish","Giant","Gnomish","Goblin","Halfling","Orc"]
uncommon_language_list =    ["Draconic","Undercommon","Aarakocra","Bullywog","Gith","Gnoll","Sahuagin","Sphinx","Thri-kreen","Troglodyte","Yeti"]
exotic_language_list =      ["Celestial","Abyssal","Infernal","Deep Speech","Grell",
                            "Primordial","Auran","Terran","Ignan","Aquan","Sylvan","Hook Horror",
                            "Modron","Otyugh","Slaad","Umber Hulk","Grung","Tlincalli","Vegepygmie"]

class Language:

    def __init__(self):
        self.languages = []
    def description(self):
        print(" Language(s): ")
        for language in self.languages:
           print("\t" + language)
