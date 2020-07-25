spells = {
  'lvl_1': ['create_water', 'cure_minor_wounds', 'detect_magic', 'detect_poison', 'guidance', 'inflict_minor_wounds', 'light', 'mending', 'purify_food_drink', 'read_magic', 'resistance', 'virtue'],

  'lvl_2':['aid', 'align_weapon', 'augury', 'bears_endurance', 'bulls_strength', 'calm_emotions', 'consecrate', 'cure_moderate_wounds', 'darkness', 'death_knell', 'delay_poison', 'desecrate', 'eagles_splendor', 'enthrall', 'find_traps', 'gentle_repose', 'hold_person', 'inflict_moderate_wounds', 'make_whole', 'owls_wisdom', 'remove_paralysis', 'resist_energy', 'restoration_lesser', 'shatter', 'shield_other', 'silence', 'sound_burst', 'spiritual_weapon', 'status', 'summon_monster_2', 'undetectable_alignment', 'zone_of_truth']
  }

spell_slots = {
  'slot_lvl_0': 6,
  'slot_lvl_1': 6,
  'slot_lvl_2': 5,
  'slot_lvl_3': 5,
  'slot_lvl_4': 4,
  'slot_lvl_5': 3,
  'slot_lvl_6': 2
  }

#did classes as dict originally, probably just need list
#character_classes = {'bard': 'bard', 'cleric': 'cleric','druid': 'druid', 'paladin': 'paladin', 'ranger': 'ranger', 'sorcerer': 'sorcerer', 'wizard': 'wizard'}

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

name = input("what is your name?\n")

print("Choose from the following classes: " + str(character_classes) + "\n")

character_profession = input("what character_class are you?\n")

level_ask = input("what level are you?\n")

class Character:
  def __init__ (self, character_name, character_class, character_level, char_spells, spell_slots):
    self.character_name = None
    self.character_class = None
    self.character_level = 1
    self.char_spells = spells
    self.spell_slots = spell_slots
  
  def get_name():
    self.character_name = name
    return self.character_name
  
  def get_class():
    self.character_class = character_profession
    return self.character_class

  def calc_spell_slots():
    self.spell_slots = spell_slots
    return self.spell_slots
  
  def set_level():
    self.character_level = int(level_ask)
    return self.character_level

