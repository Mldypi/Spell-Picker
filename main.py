import numpy as np

#List of spells. Innermost brackets is a List of spells as a dict object. The inside dict objects are the spell levels, which are themselves dict ovjects to the outermost dict keys, which are DnD Character Classes.
spells = { 'Cleric': { 
  'lvl_1': ['Create Water', 'Cure Minor Wounds', 'Detect Magic', 'Detect Poison', 'Guidance', 'Inflict Minor Wounds', 'Light', 'Mending', 'Purify Food and Drink', 'Read Magic', 'Resistance', 'Virtue'],

  'lvl_2': ['Aid', 'Align Weapon', 'Augury', 'Bears Endurance', 'Bulls Strength', 'Calm Emotions', 'Consecrate', 'Cure Moderate Wounds', 'Darkness', 'Death Knell', 'Delay Poison', 'Desecrate', 'Eagles Splendor', 'Enthrall', 'Find Traps', 'Gentle Repose', 'Hold Person', 'Inflict Moderate Wounds', 'Make Whole', 'Owls Wisdom', 'Remove Paralysis', 'Resist Energy', 'Restoration, Lesser', 'Shatter', 'Shield Other', 'Silence', 'Sound Burst', 'Spiritual Weapon', 'Status', 'Summon Monster 2', 'Undetectable Alignment', 'Zone of Truth'],

  'lvl_3': ['Animate Dead', 'Bestow Curse', 'Blindness/Deafness', 'Contagion', 'Continual Flame', 'Create Food and Water', 'Cure Serious Wounds', 'Daylight', 'Deeper Darkness', 'Dispel Magic', 'Glyph of Warding', 'Helping Hand', 'Inflict Serious Wounds', 'Invisibility Purge', 'Locate Object', 'Magic Circle Against Alignment', 'Magic Vestment', 'Meld Into Stone', 'Obscure Object', 'Prayer', 'Protection from Energy', 'Remove Blindness/Deafness', 'Remove Curse', 'Remove Disease', 'Searing Light', 'Speak With Dead', 'Stone Shape', 'Summon Monster 3', 'Water Breating', 'Water Walk', 'Wind Wall']
  }
}

#Divine revers to Clerics and Druids, who share a spell slot progression. Clerics get a bonus slot for their domain spells. Innermost Dict is spell slots per level. Second Dict is Character Levels. Outermost Dict key is Character Class.
spell_slots_per_level = { 'Cleric': {
   'char_lvl_1': {'slot_lvl_0': 3, 'slot_lvl_1': 1},

   'char_lvl_2': {'slot_lvl_0': 4, 'slot_lvl_1': 2},

   'char_lvl_3': {'slot_lvl_0': 4, 'slot_lvl_1': 2, 'slot_lvl_2': 1},

   'char_lvl_4': {'slot_lvl_0': 5, 'slot_lvl_1': 3, 'slot_lvl_2': 2},

   'char_lvl_5': {'slot_lvl_0': 5, 'slot_lvl_1': 3, 'slot_lvl_2': 2, 'slot_lvl_3': 1},

   'char_lvl_6': {'slot_lvl_0': 5, 'slot_lvl_1': 3, 'slot_lvl_2': 3, 'slot_lvl_3': 2},

   'char_lvl_7': {'slot_lvl_0': 6, 'slot_lvl_1': 4, 'slot_lvl_2': 3, 'slot_lvl_3': 2, 'slot_lvl_4': 1},

   'char_lvl_8': {'slot_lvl_0': 6, 'slot_lvl_1': 4, 'slot_lvl_2': 3, 'slot_lvl_3': 3, 'slot_lvl_4': 2},

   'char_lvl_9': {'slot_lvl_0': 6, 'slot_lvl_1': 4, 'slot_lvl_2': 4, 'slot_lvl_3': 3, 'slot_lvl_4': 2, 'slot_lvl_5': 1},

   'char_lvl_10': {'slot_lvl_0': 6, 'slot_lvl_1': 4, 'slot_lvl_2': 4, 'slot_lvl_3': 3, 'slot_lvl_4': 3, 'slot_lvl_5': 2},

   'char_lvl_11': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 4, 'slot_lvl_3': 4, 'slot_lvl_4': 3, 'slot_lvl_5': 2, 'slot_lvl_6': 1},

   'char_lvl_12': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 4, 'slot_lvl_3': 4, 'slot_lvl_4': 3, 'slot_lvl_5': 3, 'slot_lvl_6': 2},

    'char_lvl_13': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 4, 'slot_lvl_4': 4, 'slot_lvl_5': 3, 'slot_lvl_6': 2, 'slot_lvl_7': 1},

    'char_lvl_14': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 4, 'slot_lvl_4': 4, 'slot_lvl_5': 3, 'slot_lvl_6': 3, 'slot_lvl_7': 2},

    'char_lvl_15': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 4, 'slot_lvl_5': 4, 'slot_lvl_6': 3, 'slot_lvl_7': 2, 'slot_lvl_8': 1},

    'char_lvl_16': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 4, 'slot_lvl_5': 4, 'slot_lvl_6': 3, 'slot_lvl_7': 3, 'slot_lvl_8': 2},

    'char_lvl_17': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 5, 'slot_lvl_5': 4, 'slot_lvl_6': 4, 'slot_lvl_7': 3, 'slot_lvl_8': 2, 'slot_lvl_9': 1},

    'char_lvl_18': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 5, 'slot_lvl_5': 4, 'slot_lvl_6': 4, 'slot_lvl_7': 3, 'slot_lvl_8': 3, 'slot_lvl_9': 2},

    'char_lvl_19': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 5, 'slot_lvl_5': 5, 'slot_lvl_6': 4, 'slot_lvl_7': 4, 'slot_lvl_8': 3, 'slot_lvl_9': 3},

   'char_lvl_20': {'slot_lvl_0': 6, 'slot_lvl_1': 5, 'slot_lvl_2': 5, 'slot_lvl_3': 5, 'slot_lvl_4': 5, 'slot_lvl_5': 5, 'slot_lvl_6': 4, 'slot_lvl_7': 4, 'slot_lvl_8': 4, 'slot_lvl_9': 4}
  }


}

#did classes as a dict originally, probably just need list.
#character_classes = {'bard': 'bard', 'cleric': 'cleric','druid': 'druid', 'paladin': 'paladin', 'ranger': 'ranger', 'sorcerer': 'sorcerer', 'wizard': 'wizard'}

#Have to leave these as strings. Can I pull these without the '' in the console?
character_classes = ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Wizard',]

#format to print the list in the dict
#print(spells['lvl_1'])

#format to print items from the list in the dict on their own lines, in order
#print("Level One:\n")
#for item in spells['lvl_1']:
#  print (item)

#find a better way to do the new line
#print("\n")
#print("Level Two:\n")
#for item in spells['lvl_2']:
#  print(item)

name = input("What is your name?\n")

print("\n" + "Choose from the following classes: " + str(character_classes) + "\n")

#Character_profession is DnD Character Class - used Profession here to avoid confusion.
character_profession = input("What class are you?\n")

#Input is read as a Str, will need to convert for operations which need to add to the number.
level_ask = input("\n" + "what level are you?\n")

#Finds caster level, which is the number used to determine which spells a character can cast. Numpy module is used to force it to round up. Inner int() is used to force input to be an int, outer is used to force the float generated by np.ceil() to be in again.
caster_level = int(np.ceil(int(level_ask)/2))

#Class for the Character. char_spells and spell_slots. I don't know why I didn't need to use character_profession or level_ask in the class parameters. Will try updating that and see what happens, then when I call the class I'll try just using the parameter names.
#How do I make char_spells call spells for levels lower than current AND current level?
class Character:
  def __init__ (self, character_name, character_class, character_level, caster_level, char_spells, spell_slots,):
    self.character_name = character_name
    self.character_class = character_class
    self.character_level = character_level
    self.caster_level = caster_level
    self.char_spells = spells[character_class]['lvl_'+str(caster_level)]
    self.spell_slots = spell_slots_per_level[character_class]['char_lvl_'+str(character_level)]
  
#instantiate the Character class. Doesn't have to be a healer, that's a placeholder name for now
healer = Character(name, character_profession, level_ask, caster_level, spells, spell_slots_per_level,)

print("\n" + healer.character_name)
print("\n" + "Spells:" + "\n" + str(healer.char_spells))
print("\n" + "Slots:" + "\n" + str(healer.spell_slots))
print("caster level: " + str(healer.caster_level))