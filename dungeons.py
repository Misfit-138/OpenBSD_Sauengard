# Sauengard © Copyright 2022, 2023 by Jules Pitsker
# This source code is licensed under the license found in the
# LICENSE.txt file in the root directory of this source tree.

"""
Sauengard Copyright 2022, 2023, JULES PITSKER  (pitsker@proton.me)

O.R.C. NOTICE
This product is licensed under the Open RPG Creative License (ORC) located at the Library of
Congress and available online at various locations
including https://downloads.paizo.com/ORC_License_FINAL.pdf and others.
All WARRANTIES ARE DISCLAIMED AS SET FORTH THEREIN.

ATTRIBUTION
This product is original work except for the following sound/music released under the Creative Commons License:
https://creativecommons.org/licenses/by/4.0/

Main theme: "Soul's Departure" Royalty Free Music by Darren Curtis
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Blacksmith Theme: 'Viking Intro loop' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Dungeon Themes: 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Chemist Theme: 'Might and Magic' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Fieldenberg Theme: 'Tavern Loop 1' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Boss battle theme: 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Tavern Theme: 'The Medieval Banquet' by Silverman Sound is under a Creative Commons license (CC BY 3.0)
Music promoted by BreakingCopyright: http://bit.ly/Silvermansound_Medieval

Pit theme: 'Epic 39' by Jules Pitsker
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Undead king theme: Hall of the Mountain King by Kevin MacLeod http://incompetech.com
Creative Commons Attribution License 4.0 International (CC BY 4.0)
Free Download / Stream: https://bit.ly/hall-of-the-mountain-king
Music promoted by Audio Library https://youtu.be/2RDX5sVEfs4

PC Boot up sounds: Eirikr / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Floppy Disk Insert Sound: Joseph Sardin (BigSoundBank.com)
Creative Commons CC0 1.0 Universal (CC0 1.0)

Floppy Disk Drive R/W Sounds: Dennis Johansson (MrAuralization / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)

Gong: juskiddink / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Clacky Keyboard: Denis McDonald (denismcdonald / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)

Final Victory Theme: 'Epic Victory Music' Royalty Free Instrumental Music by MUSIC4VIDEO
https://www.youtube.com/watch?v=5JeU0pYk0dg

Queen Confrontation Theme: "Shadow"
Album: "The Net" 2020 Argsound
Author: Artem Grebenshchikov
Link: https://youtu.be/k-DJUohjcKo
Free for Any non-commercial use

If you use my EXPRESSLY DESIGNATED LICENSED MATERIAL in your own published works, please credit me as follows:
Sauengard, Copyright 2022,2023, by Jules Pitsker.

RESERVED MATERIAL
Reserved Material elements in this product include, but may not be limited to:
The ABOUT section, and
All elements designated as Reserved Material under the ORC License.

EXPRESSLY DESIGNATED LICENSED MATERIAL
The following elements are owned by the Licensor and would otherwise
constitute Reserved Material and are hereby designated as LICENSED MATERIAL:
Python code, ASCII Artwork, Tinbar, The Northern Kingdom and Northern Library, the Realm of Sauengard and associated
characters,locations, lore, and titles including, but not limited to Deaf One, Wicked Queen Jannbrielle, Vozzbozz,
Si'Kira, and Tor'bron."""


class Dungeon:

    def __init__(self):
        self.name = "A Dungeon"
        self.casual_name = "the dungeon"
        self.level = 0
        self.barrier_name = "a stone wall"
        self.barrier_name_plural = "stone walls"
        self.pit_barrier_name = "a wall of putrid moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.staircase = (0, 0)
        self.treasure_chest = (0, 0)
        self.quantum_treasure_chest = (0, 0)
        self.encounter_sikira = (0, 0)
        self.encounter_the_party = (0, 0)
        self.altar = (0, 0)
        self.throne = (0, 0)
        self.fountain = (0, 0)
        self.teleporter = (0, 0)
        self.teleporter_landing = (0, 0)
        self.elevator = (0, 0)
        self.elevator_landing = (0, 0)
        self.pit = (0, 0)
        self.pit_landing = (0, 0)
        self.elite_monster = (0, 0)  # 4, 10
        self.legendary_monster = (0, 0)
        self.encounter_deaf_one_1 = (0, 0)
        self.encounter_deaf_one_2 = (0, 0)
        self.deaf_one_portal_dungeon_level2 = (0, 0)
        self.deaf_one_portal_dungeon_level3 = (0, 0)
        self.deaf_one_portal_dungeon_level4 = (0, 0)
        self.wicked_queen = (0, 0)
        self.exit = (0, 0)
        self.grid = []
        self.player_grid = []

    def __repr__(self):
        return self.name


class Dungeon1(Dungeon):

    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Catacombs"
        self.casual_name = "the catacombs"
        self.level = 1
        self.barrier_name = "a stone wall of tombs"
        self.barrier_name_plural = "walls of tombs"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.staircase = (6, 18)
        self.treasure_chest = (3, 16)
        self.quantum_treasure_chest = (99, 99)
        self.altar = (6, 7)
        self.throne = (99, 99)
        self.fountain = (10, 5)
        self.teleporter = (99, 99)
        self.teleporter_landing = (99, 99)
        self.elevator = (4, 18)
        self.elevator_landing = (8, 5)
        self.pit = (10, 7)
        self.pit_landing = (1, 14)  # always 1, 14
        self.elite_monster = (99, 99)  # 4, 10
        self.legendary_monster = (99, 99)
        self.encounter_deaf_one_1 = (7, 14)
        # self.encounter_sikira = (99, 99)
        self.wicked_queen = (99, 99)
        self.exit = (10, 0)
        # following are just for human-readable purposes. program ignores all values except "*", which represent walls
        # S = STAIRCASE C = CORRIDOR, P = PIT-opening, L = PIT LANDING ^ = ELEVATOR V = ELEVATOR LANDING . = OPEN AREA
        # F = FOUNTAIN
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "E", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "C", "C", "C", "V", "C", "F", "C", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "C", ".", ".", "*", "*", "P", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "*", ".", ".", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", "L", "C", ".", ".", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", "C", "*", ".", ".", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", "C", "*", "*", ".", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", "C", "C", "C", "^", "*", "S", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is called first and is more active
        self.intro = "Pressing onward, you soon come to a domed, circular chamber, with a large, spiral " \
                     "staircase at the center.\n" \
                     "You descend the steep, crumbling steps, finding yourself in a dense, " \
                     "dark atmosphere more oppressive\nthan any you have ever known. Taking a moment to adjust to " \
                     "the thick gloom, you hear a disturbance\nfrom above, as the great doors are slammed and " \
                     "barred shut! As the echoes throughout the emptiness linger,\nyou hear the muffled scraping of " \
                     "a mighty chain being quickly wrestled into place, and finally,\nlocked and released with a" \
                     " thud. Blackness and the stench of filth surround you.\n\nBEWARE . . .\n\n"


class Dungeon2(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Abandoned Dwarf Tunnels"
        self.casual_name = "the abandoned tunnels"
        self.level = 2
        self.barrier_name = "a wall of volcanic rock"
        self.barrier_name_plural = "walls of cut volcanic rock"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of foul, moist earth"
        self.corridor_phrase = f"This is a corridor of Dwarven masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium built by the Dwarves long ago."
        self.one_walled_atrium_phrase = "You are standing in an atrium built by the Dwarves long ago."
        self.pit_large_atrium_phrase = "You are standing in a large cavity opening."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity opening."
        self.staircase = (7, 12)
        self.treasure_chest = (18, 6)
        self.quantum_treasure_chest = (18, 11)
        self.altar = (12, 10)
        self.throne = (3, 9)
        self.fountain = (3, 10)
        self.teleporter = (99, 99)
        self.teleporter_landing = (99, 99)
        self.elevator = (4, 14)
        self.elevator_landing = (8, 6)
        self.pit = (10, 7)
        self.pit_landing = (1, 14)
        self.elite_monster = (14, 11)  # 4, 10
        self.legendary_monster = (99, 99)
        self.encounter_sikira = (99, 99)
        self.deaf_one_portal_dungeon_level2 = (17, 8)
        self.wicked_queen = (99, 99)
        self.exit = (19, 8)
        # following are just for human-readable purposes. program ignores all values except "*", which represent walls
        # S = STAIRCASE C = CORRIDOR, P = PIT-opening, L = PIT LANDING ^ = ELEVATOR V = ELEVATOR LANDING . = OPEN AREA
        # F = FOUNTAIN
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "C", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "C", "C", "C", "C", "C", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "C", "*"],  # 6
            ["*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "C", "*"],  # 7
            ["*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "C", "C", "C", "C", "E"],  # 8
            ["*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "C", "*"],  # 9
            ["*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", "C", "*"],  # 10
            ["*", "*", "*", "C", "*", "*", ".", ".", ".", "*", "*", ".", ".", ".", "C", "C", "*", "*", "C", "*"],  # 11
            ["*", "*", "*", "C", "C", "C", ".", "S", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", "L", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", "C", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", "C", "C", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = f"The door above closes solidly. You find yourself in a deeper level of the dungeons.\n" \
                     f"This is a series of tunnels dug by the Dark Dwarves many ages ago for King Justin III.\n" \
                     f"Thick, oppressive gloom and disturbing sounds fill the air.\n"


class Dungeon3(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Deep Realms"
        self.level = 3
        self.barrier_name = "a wall of limestone"
        self.barrier_name_plural = "walls of eroded limestone"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a naturally formed passage."  # of {self.casual_name}
        self.corridor_name = f"a tunnel formed by the dissolution of limestone"
        self.pit_description_phrase = f"The ground is covered in running water and streamed with colorful minerals."
        self.pit_corridor_phrase = "You are in a round, jagged tunnel with shallow water at your feet."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a vast, naturally-formed cavity."
        self.one_walled_atrium_phrase = "You are standing in a cramped, naturally-formed cavity."
        self.pit_large_atrium_phrase = "You are standing in a large, open cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity formed of clay and rock."
        self.staircase = (18, 1)  # testing (1, 3)
        self.treasure_chest = (4, 15)
        self.quantum_treasure_chest = (1, 18)
        self.altar = (11, 18)
        self.throne = (13, 12)
        self.fountain = (16, 3)
        self.teleporter = (3, 10)
        self.teleporter_landing = (9, 18)
        self.elevator = (1, 17)
        self.elevator_landing = (5, 3)
        self.pit = (7, 1)
        self.pit_landing = (1, 14)  # always 1, 14
        self.elite_monster = (4, 10)  # 4, 10
        self.legendary_monster = (11, 1)
        self.encounter_sikira = (11, 5)
        self.deaf_one_portal_dungeon_level3 = (18, 2)  # force a portal back to tavern if not done so already
        self.wicked_queen = (99, 99)
        self.exit = (19, 3)
        # following are just for human-readable purposes. program ignores all values except "*", which represent walls
        # S = STAIRCASE C = CORRIDOR, P = PIT-opening, L = PIT LANDING ^ = ELEVATOR V = ELEVATOR LANDING . = OPEN AREA
        # F = FOUNTAIN T = TELEPORTER
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "C", "C", "P", "*", "*", "*", "C", "C", "C", "C", "C", "C", "C", "C", "*"],  # 1
            ["*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "*"],  # 2
            ["*", "S", "C", "C", "C", "V", "C", ".", ".", ".", "*", "C", "*", "*", ".", ".", ".", "C", "C", "E"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", ".", ".", ".", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "C", "*", "*", ".", ".", ".", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "C", "*", "*", ".", ".", ".", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", "*", ".", ".", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "C", "C", "*", ".", ".", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "T", "C", "C", "*", ".", ".", ".", "*", "C", "C", "C", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "C", "C", "*", "C", "C", "*", "C", "C", ".", ".", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*"],  # 13
            ["*", "L", "*", "*", "*", "*", "C", "*", "*", "C", "*", "C", "C", ".", ".", "*", "*", "*", "*", "*"],  # 14
            ["*", "C", "C", "C", "C", "*", "C", "*", ".", ".", "*", "C", "*", "*", "C", "*", "*", "*", "*", "*"],  # 15
            ["*", "*", "*", "*", "C", "*", "C", "*", ".", ".", "*", "C", "*", "*", "C", "*", "*", "*", "*", "*"],  # 16
            ["*", "^", "*", "*", "C", "*", "C", "*", "*", "C", "*", "C", "*", "*", "C", "*", "*", "*", "*", "*"],  # 17
            ["*", "C", "C", "C", "C", "*", "C", "C", "C", "C", "C", "C", "C", "C", "C", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = "You find yourself at the bottom of a deep, spiral staircase..\n" \
                     "The echo from the door above being locked behind you still echoes throughout the emptiness.\n" \
                     "This is the entrance of the deep realms. Murk and disturbing shadows surround you.\n"


class Dungeon4(Dungeon):

    def __init__(self):
        super().__init__()
        self.name = "The Long Hallway"
        self.casual_name = "the long hallway"
        self.level = 4
        self.barrier_name = "a wall of gleaming granite"
        self.barrier_name_plural = "walls of granite"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a long corridor."  # of {self.casual_name}
        self.corridor_name = f"a long, tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.staircase = (1, 4)
        self.treasure_chest = (4, 4)
        self.quantum_treasure_chest = (9, 4)
        self.altar = (99, 99)
        self.throne = (99, 99)
        self.fountain = (99, 99)
        self.teleporter = (99, 99)
        self.teleporter_landing = (99, 99)
        self.elevator = (99, 99)
        self.elevator_landing = (99, 99)
        self.pit = (99, 99)
        self.pit_landing = (99, 99)  # always 1, 14
        self.elite_monster = (11, 4)  # 4, 10
        self.legendary_monster = (14, 4)
        self.encounter_deaf_one_2 = (15, 4)
        self.encounter_the_party = (7, 4)
        self.deaf_one_portal_dungeon_level4 = (2, 4)
        self.encounter_sikira = (99, 99)
        self.wicked_queen = (17, 4)
        self.exit = (99, 99)  # create event to take player back to level 1 for re-playability
        # following are just for human-readable purposes. program ignores all values except "*", which represent walls
        # S = STAIRCASE C = CORRIDOR, P = PIT-opening, L = PIT LANDING ^ = ELEVATOR V = ELEVATOR LANDING . = OPEN AREA
        # F = FOUNTAIN
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "S", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = "You enter a torchlit, long hallway of solid granite which stretches far into the distance.\n" \
                     "The stone walls and echoes create strange acoustic effects from even the most innocuous sounds-" \
                     " footsteps, the clank of armor,\neven your breathing. At the extreme end of the tunnel, to the " \
                     "east, you see a dimly glowing circle, which appears\nto be an entrance to a chamber or room of " \
                     "some sort.\n"


dungeon_dict = {1: Dungeon1(),
                2: Dungeon2(),
                3: Dungeon3(),
                4: Dungeon4()
                }

# blank grid with pit in lower left at 1, 14.
"""self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
            """
