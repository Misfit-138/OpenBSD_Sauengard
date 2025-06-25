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
The ABOUT section,
All elements designated as Reserved Material under the ORC License.

EXPRESSLY DESIGNATED LICENSED MATERIAL
The following elements are owned by the Licensor and would otherwise
constitute Reserved Material and are hereby designated as LICENSED MATERIAL:
Python code, ASCII Artwork, Tinbar, The Northern Kingdom and Northern Library, the Realm of Sauengard and associated
characters,locations, lore, and titles including, but not limited to Deaf One, Wicked Queen Jannbrielle, Vozzbozz,
Si'Kira, and Tor'bron.
"""

import math
import pickle
import random
import time
import os
import sys
from collections import Counter
from dungeons import dungeon_dict
from monster_module import monster_dict, king_boss_list, undead_prophet_list, WickedQueenJannbrielle
from pathlib import Path
import itertools

if os.name == 'nt':
    import winsound
    import keyboard
if os.name == 'posix':
    from termios import tcflush, TCIFLUSH

# if you call a function and expect to use a return value, like, by printing it, you must first assign a variable in
# the call itself!!!
# when passing a list as an argument, remember to use the * unpacking operator
# seq = [1, 2, 3]
# foo(*seq)

'''DIFFICULTY CLASSES (Misfit’S REMIX)
Task Difficulty	 DC
Very Easy	     5
Easy	         8
Medium	         10
Tricky	         12
Hard	         15
Very hard	     20
Incredibly hard	 25
Why bother?	     30
'''


def ibm_startup_meta_function():
    pc_powerup()
    sleep(5)
    floppy_insert_and_load()
    ibm_dos_screen()


def os_check():
    cls()
    print("Welcome!\nPlease ensure terminal is in full screen mode.")
    print()
    if os.name == 'nt':
        random_startup_list = [ibm_startup_meta_function, commodore_pet_screen]
        random_startup = random.choice(random_startup_list)
        random_startup()
        initial_loading_screen()

    else:
        teletype(f"Operating System identifies as: {os.name.title()}")
        teletype(f"Sauengard should be stable, with the following 2 limitations:\n"
                 f"1. Sound support is not currently available.\n"
                 f"2. The 'keyboard' module requires root permissions on GNU/Linux, and I could not get it to work\n"
                 f"reliably. Therefore, users will be unable to skip through teletype-style messages.\n\n")
        pause()
        unix_screen()


def commodore_pet_screen():
    sleep(3)
    cls()
    sleep(2)
    stop_sound()
    print(f"\n*** COMMODORE PET BASIC 4.0 ***\n 31743 BYTES FREE\nREADY.")
    sleep(1.5)
    clacky_keyboard_short2()
    same_line_teletype(F"LOAD\"$\",8")
    sleep(.25)
    same_line_print("\n")
    random_floppy_rw_sound()
    sleep(2)
    # stop_sound()
    print(f"0 \"GAME DISK 1\"            1       ")
    print(f"38   \"HANGMAN\"             PRG")
    print(f"92   \"HAMMURABI\"           PRG")
    print(f"64   \"BASEBALL\"            PRG")
    print(f"54   \"CAVE\"                PRG")
    print(f"33   \"WUMPUS\"              PRG")
    print(f"126  \"CANYON\"              PRG")
    print(f"121  \"DUNGEON\"             PRG")
    print(f"442  \"SAUENGARD\"           PRG")
    print(f"12 BLOCKS FREE.")
    print(f"READY.")
    sleep(4)
    clacky_keyboard_short()
    sleep(.4)
    same_line_teletype("LOAD\"SAUENGARD\",8")
    stop_sound()
    sleep(.5)
    print("\n")
    sleep(.5)
    random_floppy_rw_sound()
    sleep(3)
    print(f"READY.")
    sleep(2)
    clacky_keyboard_short()
    sleep(.25)
    same_line_teletype("RUN\n")
    stop_sound()
    sleep(1)
    random_floppy_rw_sound()
    sleep(2)


def ibm_dos_screen():
    cls()
    sleep(2)
    stop_sound()
    print("Current date is Tue 1-01-1980")
    same_line_print("Enter new date (mm-dd-yy): ")
    sleep(.5)
    clacky_keyboard_short2()
    same_line_teletype("5-27-1983\n")
    sleep(.25)
    stop_sound()
    print("Current time is 0:00:25:36")
    same_line_print("Enter new time: ")
    sleep(1)
    clacky_keyboard_short()
    sleep(.4)
    same_line_teletype("8:02\n")
    stop_sound()
    sleep(1)
    print("\n\n")
    print("The IBM Personal Computer DOS\n"
          "Version 3.00 (C)opyright IBM Corp 1984")
    sleep(1)
    same_line_print("A> ")
    sleep(1)
    clacky_keyboard_short2()
    sleep(.25)
    same_line_teletype("SAUENGARD.BAT")
    print("\n")
    sleep(.5)
    random_floppy_rw_sound()
    sleep(1)


def unix_screen():
    # original devs of
    # UNIX, 'chess', 'space_travel',
    # the C programming language,
    # 'dnd',
    # 'DND' and
    # 'Dungeon',
    # respectively, and, respectfully :)
    # Note that 'dnd' (lowercase) (Whisenhunt, Wood, Dirk Pellett, Flint Pellett, developed on the PLATO network)
    # and 'DND' (UPPERCASE) (Daniel Lawrence) are different games with an interesting, and contentious history.
    # Lawrence later wrote 'Telengard', a game based on 'DND'. 'Telengard' was a commercial success.
    # Lawrence denied having ever played 'dnd' on PLATO.
    # dnd maintainer and author, Dirk Pellett, claims that Daniel Lawrence outright plagiarized it.
    # For more: http://www.armory.com/~dlp/dnd1.html)
    user_list = ["ken_thompson", "dennis_ritchie",
                 "gary_whisenhunt", "ray_wood", "dirk_pellett", "flint_pellett",
                 "daniel_lawrence",
                 "don_daglow"]
    user = random.choice(user_list)
    cls()
    print("digital PDP 11/23 PLUS")
    sleep(.5)
    cls()
    same_line_print("BOOT> ")
    sleep(1.5)
    same_line_teletype("DU 0\n")
    sleep(.5)
    print("73Boot from ra(0,0,0) at 0172150")
    sleep(.5)
    print(":\n: ra(0,0,0)unix")
    sleep(.5)
    print("Boot: bootdev=02400 bootcsr=0172150")  # I'm curious about what 'bootcsr' means.
    sleep(.5)
    print("total real memory       = 1024000")
    sleep(.25)
    print("total available memory  = 901068\n")
    sleep(.25)
    print("AT&T UNIX System V Release 1.0 version 1.1")
    print("(Bell Labs internal USG UNIX 5.0 codebase. *Not for re-distribution*)")
    print("Copyright (c) 1983 AT&T")
    print("All Rights Reserved")
    sleep(1.5)
    same_line_print("The system is coming up.  ")
    sleep(1)
    same_line_print("Please wait. ")
    spinner(500)  # this is anachronistic, but I thought it looked cool, like openBSD or something. consider removing.
    # sleep(2)
    cls()
    same_line_print("Console Login: ")
    sleep(1)
    same_line_teletype(user)
    print()
    sleep(.5)
    print()
    sleep(.5)
    same_line_print("Password: ")
    sleep(1.5)
    print("\n")
    print("AT&T UNIX System V Release 1.0 version 1.1")
    print("Copyright (c) 1983 AT&T")
    print("All Rights Reserved")
    print("Last login: Thu Sep 10 01:50:13 on console")
    sleep(.5)
    print("/        :    Disk space 5.14 MB of 10 MB available (51.4%) ")
    sleep(1)
    same_line_print("$ ")
    sleep(1.5)
    same_line_teletype("cd /usr/games\n")
    sleep(.5)
    same_line_print("$ ")
    sleep(1.5)
    same_line_teletype("ls\n")
    sleep(.25)
    print(f"adventure\ncanyon\ndnd\nDND\ndungeon\nchess\nspace_travel\nsauengard\n")
    same_line_print("$ ")
    sleep(1.5)
    same_line_teletype("./sauengard\n")
    print("\n")
    sleep(2)


def clacky_keyboard_short():
    sound_player('clacky_keyboard_short.wav')


def clacky_keyboard_short2():
    sound_player('clacky_keyboard_short2.wav')


def initial_loading_screen():
    cls()
    same_line_print(f"\nLOADING.")
    dot_dot_dot(20)


def random_floppy_rw_sound():
    floppy_sound = [floppy_rw, floppy_rw2]
    loading_sound = random.choice(floppy_sound)
    loading_sound()


def loading_screen():
    cls()
    random_floppy_rw_sound()
    same_line_print(f"\nLOADING.")
    dot_dot_dot(20)


def quit_game():
    cls()
    teletype("Quit game..")
    teletype("Any unsaved progress will be lost....\n")

    if are_you_sure():
        print(f"Farewell. . .")
        sleep(1)
        cls()
        sys.exit()

    else:
        return


def are_you_sure():
    while True:
        confirm = input("Are you sure (y/n)? ").lower()

        if confirm == 'y':
            return True
        else:
            return False


def spinner(number_of_spins):
    # silly little function for a progress spinner.
    spin_cycle = itertools.cycle(['-', '/', '|', '\\'])

    for i in range(number_of_spins):
        sys.stdout.write(next(spin_cycle))   #
        sys.stdout.flush()
        sys.stdout.write('\b')  # erase the last written char
        sleep(.005)


def escape_key_interrupt_teletype(message):
    # I am proud of this little snippet I figured out,
    # but unfortunately, it does not work reliably on *nix due to permissions problems with the 'keyboard' module.
    if os.name == 'nt':

        if keyboard.is_pressed('Esc'):  # Skip through teletype message straight to printing, if escape is pressed:
            cls()
            print()  # skip a line, just like teletype(), so printed text will line up perfectly with teletyped text
            print(message)
            return True

        else:
            return False

    else:
        return False


def same_line_print(string):
    # simple function that does not add a carriage return, allowing next item to be printed on same line
    sys.stdout.write(string)
    sys.stdout.flush()


def same_line_teletype(string):
    for each_character in string:
        sys.stdout.write(each_character)
        sys.stdout.flush()
        sleep(0.07)


def dot_dot_dot(number_of_dots):
    # print a series of specified periods '.' after same_line_print(string)
    for i in range(number_of_dots):
        sleep(.2)
        same_line_print(".")


def teletype(message):
    # based this snippet on a snippet from 101computing.net:
    print()  # skip a line
    for each_character in message:
        sys.stdout.write(each_character)
        sys.stdout.flush()
        sleep(0.0050)  # 0.0065, 0.01 all seem good
        if escape_key_interrupt_teletype(message):
            return

    sleep(0.1)
    return


def print_txt_file(txt_file_name):
    cls()
    p = ""
    try:
        text_folder = Path(__file__).with_name("text")
        p = text_folder / txt_file_name
        # p = Path(__file__).with_name(txt_file_name)
        with p.open('r') as txt:
            if txt.readable():
                print(txt.read())

    except FileNotFoundError:
        print(f"Missing {p} or bad file path.")


def teletype_txt_file(txt_file_name):
    cls()
    p = ""
    try:
        text_folder = Path(__file__).with_name("text")
        p = text_folder / txt_file_name
        # p = Path(__file__).with_name(txt_file_name)
        with p.open('r') as message:
            if message.readable():
                teletype(message.read())

    except FileNotFoundError:
        print(f"Missing {p} or bad file path.")


def game_splash():
    while True:
        cls()
        print_txt_file('splash_art.txt')
        print("                                   "
              "W  E  L  C  O  M  E    T  O    S  A  U  E  N  G  A  R  D.\n")
        print(f"                                         "
              f"   © Copyright 2022, 2023, by Jules Pitsker")
        choice = input(f"                               "
                       f"(Quit) to Desktop  (A)bout  (T)ips  (C)redits  "
                       f"(L)icense  (B)egin ").lower()

        if choice == 'a':
            teletype_txt_file('about.txt')
            pause()

        elif choice == 't':
            teletype_txt_file('tips.txt')
            pause()

        elif choice == 'c':
            print_txt_file('credits.txt')
            pause()
            print_txt_file('credits2.txt')
            pause()
            print_txt_file('credits3.txt')
            pause()

        elif choice == 'l':
            print_txt_file('LICENSE.txt')
            pause()

        elif choice == 'quit':
            quit_game()

        elif choice == 'b':
            return


def convert_list_to_string(list1):
    # no brackets, no quotes, no commas
    return str(list1).replace('[', '').replace(']', '').replace("'", "").replace(",", "")


def convert_list_to_string_with_commas_only(list1):
    # no brackets, no quotes. WITH commas
    return str(list1).replace('[', '').replace(']', '').replace("'", "")


def convert_list_to_string_with_and(list1):
    # no brackets, no quotes. WITH commas. add "and" before last element to be more naturally readable
    list1.insert(-1, 'and')
    readable_list = str(', '.join(list1[:-2]) + ' ' + ' '.join(list1[-2:]))
    return readable_list


# def compare():  # unused function?
#    lambda x, y: collections.Counter(x) == collections.Counter(y)


def pause():
    # for cross-platform compatibility, I have tried to make this as best I can.
    # MS Windows users will have a slight convenience in the ability to hit any key,
    # whereas Posix/GNU/Linux users must hit ENTER
    if os.name == 'nt':
        os.system('pause')

    else:
        tcflush(sys.stdin, TCIFLUSH)  # flush input stream to prevent game disruption by player mashing ENTER key!
        input("Press [ENTER] to continue . . . ")

    return


def cls():
    # for cross-platform compatibility
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

    return


def sleep(seconds):
    time.sleep(seconds)
    return


def dice_roll(no_of_dice, no_of_sides):
    dice_rolls = []  # create list for multiple die rolls

    for dice in range(no_of_dice):
        dice_rolls.append(random.randint(1, no_of_sides))

    your_roll_sum = sum(dice_rolls)
    return your_roll_sum


def dungeon_command_choices():
    command = input("(QUIT) to desktop, (R)estart game, (L)ook at surroundings, (STAY) where you are,\n"
                    "use (MAP), (C)larifying elixir, Town (P)ortal, (H)ealing potion, (M)anage inventory,\n"
                    "(G)iant strength potion, (V)ial of Antidote, (I)nventory, (Q)uantum effects,\n"
                    "or W-A-S-D to navigate. --> ").lower()
    return command


def character_generator():
    cls()
    explanation_dict = {"Strength": "Strength is a measure of one's physical force. A character high\n"
                                    "in Strength can do more damage with melee weapons.\nAlso essential for "
                                    "lifting heavy objects when interacting with certain dungeon features.",
                        "Dexterity": "Dexterity is a measure of a character’s speed, swiftness, and "
                                     "coordination.\nIt is also an essential component of stealth attempts and "
                                     "your Armor Class.",
                        "Constitution": "Constitution defines one's general stoutness and resistence to evil "
                                        "effects, like poison and Quantum necrosis.\n"
                                        "Constitution is also proportional to one's hit points.",
                        "Intelligence": "Intelligence determines how well your character learns and discerns. It is\n"
                                        "important for certain quantum effects, your ability to recall \n"
                                        "languages and read runes, as well as your ability to investigate your \n"
                                        "surroundings.",
                        "Wisdom": "Wisdom represents action based on intelligence and understanding; "
                                  "the ability\n"
                                  "to practically apply one's knowledge successfully, solve problems, avoid or "
                                  "avert\n"
                                  "dangers, and attain goals. Wisdom is absolutely critical for "
                                  "harnessing\n"
                                  "many Quantum effects, as well as avoiding many Quantum attacks.",
                        "Charisma": "Charisma measures one's personal attraction and social skills. A character with "
                                    "high charisma will have a\n"
                                    "better chance of favorable outcomes when encountering certain monsters.\n"
                                    "Charisma can mean the difference between great fortune and death."}

    default_stats = f"Attribute Value    	Attribute Modifier\n" \
                    f"15	                            +3\n14	                            " \
                    f"+2\n13	                            +1\n12	                            +1\n10" \
                    f"	                            +0\n9	                            -1\n"

    stats = {
        "strength": 15,
        "dexterity": 14,
        "constitution": 13,
        "intelligence": 10,
        "wisdom": 12,
        "charisma": 9,
    }

    while True:
        cls()
        player_name = input(f"Please enter character name: ")

        if len(player_name) < 3:
            print(f"Minimum 3 characters!")
            sleep(.25)
            continue

        confirm_player_name = input(f"Player name is {player_name}. Is this ok (y/n)? ").lower()

        if confirm_player_name == 'y':
            break

        else:
            continue

    cls()
    # print(f"{player_name}:")
    print(f"Default Stats (Recommended if unsure)")

    for key, value in stats.items():
        print(key.capitalize(), ":", value)
    default_choice = input(f"[ENTER] to use the above default stats or (C)ustomize? ([ENTER]/C): ").lower()

    if default_choice != 'c':
        player_1 = Player(name=player_name, **stats)
        # pause()
        return player_1

    cls()
    print(f"Customization involves assigning your own attribute values.\n"
          f"The stats are picked from a set pool of six values: 15, 14, 13, 12, 10, 9\n"
          f"Each number will be matched with one of the six character attributes.\n"
          f"Note that each attribute value has a corresponding modifier, which\n"
          f"acts as a bonus, (or, as a penalty, in the case of a negative modifier),\n"
          f"and will become more important as you progress.\n"
          f"Attributes and modifiers increase as you level up.\n")
    print(default_stats)
    pause()
    score_list = [15, 14, 13, 12, 10, 9]

    while len(score_list):

        for key in stats:
            cls()
            print(default_stats)
            human_key = key.capitalize()
            print(f"{human_key}:")
            print(explanation_dict[human_key])
            scores = convert_list_to_string_with_commas_only(score_list)
            print(f"Available scores: {scores}")

            try:
                score = int(input(f"Enter score to assign to {human_key} (or hit [ENTER] to start over): "))

                if score in score_list:
                    print(f"{key} = {score}")
                    sleep(.5)
                    stats[key] = score
                    score_list.remove(score)

                else:
                    score_list = [15, 14, 13, 12, 10, 9]  # re-set list
                    print(f"Valid scores are listed above.")
                    sleep(0.5)
                    print(f"Starting over.")
                    sleep(0.5)
                    break

            except ValueError:
                print(f"Invalid entry..")
                score_list = [15, 14, 13, 12, 10, 9]  # re-set list
                sleep(0.5)
                print(f"Starting over.")
                sleep(0.5)
                break
    # for key, value in stats.items():
    # print(key, ":", value)
    player_1 = Player(name=player_name, **stats)  # **stats sends the 'stats' dictionary as parameters
    # pause()
    return player_1


def game_start():
    # called from main loop
    while True:
        sad_cello_theme()
        game_splash()
        cls()
        player_1 = ""  # to get rid of undefined warning

        intro_or_not = input("View Introduction? (y/n) ").lower()
        if intro_or_not == 'y':
            teletype_txt_file('introduction.txt')
            pause()

        while True:
            cls()
            new_game_or_load = input("(S)tart a new character, (L)oad a saved one, or go (B)ack to main menu: ").lower()

            if new_game_or_load == 'b':
                break

            if new_game_or_load not in ('s', 'l'):
                continue

            elif new_game_or_load == 'l':
                player_name = input("Enter name of saved character: ")
                load_a_character = player_name + ".sav"
                p = Path(__file__).with_name(load_a_character)
                random_floppy_rw_sound()
                sleep(2)
                if p.is_file():
                    with p.open('rb') as saved_player:  # 'rb'
                        same_line_print(f"{player_name} found")
                        player_1 = pickle.load(saved_player)
                        dot_dot_dot(5)
                        same_line_print(f"{player_name} read.\n")
                        sleep(2)
                        # dungeon = dungeon_dict[player_1.dungeon_key]  # diagnostic - remove after testing
                        # print(dungeon.name)  # diagnostic - remove after testing
                        # print(player_1.coordinates)  # diagnostic - remove after testing
                        player_1.loaded_game = True
                        sleep(1)
                        return player_1

                else:
                    print(f"Could not find {player_name} ")
                    sleep(1.5)
                    continue

            elif new_game_or_load == 's':
                accept_stats = ""

                while accept_stats != 'y':
                    player_1 = character_generator()
                    player_1.hud()
                    # print(f"Dungeon Key {player_1.dungeon_key}")
                    accept_stats = input(f"Accept character and continue? (y/n)? ").lower()

                if accept_stats == "y":
                    # player_1.dungeon_key = 1  # unneeded
                    # player_1.dungeon = dungeon_dict[player_1.dungeon_key]  # should be unneeded
                    (player_1.x, player_1.y) = player_1.dungeon.staircase
                    player_1.position = 0
                    player_1.hud()
                    return player_1


def unknown_command():
    print("Unknown command..")
    sleep(.25)


def npc_ally_hud_sub_function(npc):
    # called from self.hud()
    npc_ally_hud_hit_points = npc.hit_points
    npc_readiness = "(OK)"
    if npc.hit_points < 1:
        npc_ally_hud_hit_points = 1
        npc_readiness = "(RETREATING)"
    print(f"{npc.name}  HP: {npc_ally_hud_hit_points} {npc_readiness}")


def augmentation_intro():
    cls()
    print(f"                                  *Attribute Augmentation*")
    print()
    print(
        f"You may choose to improve a single attribute, such as strength, and increase it by 2 points.\n"
        f"\n"
        f"                           *OR*\n"
        f"\n"
        f"You may choose to improve two attributes, such as charisma and constitution, by 1 point each.\n"
        f"\n"
        f"NOTES: \n"
        f"* Attribute *modifiers* improve with each ascending even-numbered score, therefore, if unsure,\n"
        f"  it is generally recommended to apply 1 point to odd-numbered attribute values and apply \n"
        f"2 points to even-numbered values.\n"
        f"* When your Constitution modifier increases by 1, your hit point maximum increases by 1 for each\n"
        f"  level you have attained.\n"
        f"                         *The maximum score for any attribute is 20*"
        f"\n")
    pause()


def stop_sound():
    winsound.PlaySound(None, 0)


def sound_player(sound_file):
    # a sound player function which simply plays sound_file asynchronously
    if os.name == 'nt':
        p = ""
        try:
            sound_folder = Path(__file__).with_name("sound")
            p = sound_folder / sound_file
            # p = Path(__file__).with_name(sound_file)
            with p.open('rb') as sound:
                if sound.readable():
                    winsound.PlaySound(str(p), winsound.SND_FILENAME | winsound.SND_ASYNC)
        except FileNotFoundError:
            # pass  # restore after testing
            print(f"{p} not found.")  # remove after testing
            pause()  # remove after testing


def sound_player_loop(sound_file):
    # a sound player function which plays sound_file asynchronously on a continuous loop
    if os.name == 'nt':
        p = ""
        try:
            sound_folder = Path(__file__).with_name("sound")
            p = sound_folder / sound_file
            # print(p)
            # p = Path(__file__).with_name(sound_file)
            with p.open('rb') as sound_loop:
                if sound_loop.readable():
                    winsound.PlaySound(str(p), winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        except FileNotFoundError:
            # pass  # restore after testing
            print(f"{p} not found.")  # remove after testing
            pause()  # remove after testing


def gong():
    # notice the gong is not looped!
    sound_player('gong.wav')


def pc_powerup():
    sound_player('pc_powerup.wav')


def floppy_rw():
    sound_player('floppy_rw.wav')


def floppy_rw2():
    sound_player('floppy_rw2.wav')


def floppy_insert_and_load():
    sound_player('floppy_insert.wav')
    sleep(1)
    sound_player_loop('floppy_rw.wav')
    # floppy_rw()
    # sound_player('floppy_insert_and_load.wav')


def sad_cello_theme():
    sound_player_loop('sad_cello_darren_curtis.wav')


def blacksmith_theme():
    sound_player_loop('blacksmith_theme_2.wav')


def chemist_theme():
    sound_player_loop('chemist_theme.wav')


def mountain_king_theme():
    sound_player_loop('mountain_king.wav')


def pit_theme():
    sound_player_loop('creepy_dungeon_theme_loop.wav')


def boss_battle_theme():
    sound_player_loop('boss_battle_2.wav')


def town_theme():
    sound_player_loop('town_(tavern)_loop_by_alexander_nakarada.wav')


def tavern_theme():
    sound_player_loop('silvermansound_the medieval_banquet.wav')


def queen_confrontation_theme():
    sound_player_loop('queen_confrontation.wav')


def final_victory_theme():
    sound_player_loop('final_victory.wav')


class Weapon:

    def __init__(self):
        self.name = ""
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f"{self.name} - Damage Bonus: {self.damage_bonus}  To-hit bonus: {self.to_hit_bonus}  " \
               f"Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP"


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 10
        self.minimum_level = 1
        self.a_an = "a"


class BroadSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Broad Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = 1
        self.sell_price = 5
        self.buy_price = 25
        self.minimum_level = 2
        self.a_an = "a"


class GreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Great Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 3
        self.to_hit_bonus = 2
        self.sell_price = 150
        self.buy_price = 500
        self.minimum_level = 4
        self.a_an = "a"


class ElvishGreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Elvish Great Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 10
        self.to_hit_bonus = 4
        self.sell_price = 2500
        self.buy_price = 5000
        self.minimum_level = 10
        self.a_an = "an"


class WeirdSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Weird Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 15  # 5
        self.to_hit_bonus = 7
        self.sell_price = 6000
        self.buy_price = 55000
        self.minimum_level = 1
        self.a_an = "a"


class QuantumSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 12  # 5
        self.to_hit_bonus = 5
        self.sell_price = 5000
        self.buy_price = 8000
        self.minimum_level = 12
        self.a_an = "a"


class QuantumAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 15  # 5
        self.to_hit_bonus = 5
        self.sell_price = 5000
        self.buy_price = 8000
        self.minimum_level = 12  # 3
        self.a_an = "a"


class ShortAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = -1
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1
        self.a_an = "a"


class BattleAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Battle Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 3
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 50
        self.minimum_level = 3
        self.a_an = "a"


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Great Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 4
        self.to_hit_bonus = 0
        self.sell_price = 15
        self.buy_price = 500
        self.minimum_level = 4
        self.a_an = "a"


class ElvishGreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Elvish Great Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 12
        self.to_hit_bonus = 4
        self.sell_price = 2750
        self.buy_price = 6000
        self.minimum_level = 12
        self.a_an = "an"


class Armor:

    def __init__(self):
        self.name = ""
        self.item_type = "Armor"
        self.armor_bonus = 0
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a set of"

    def __repr__(self):
        return f'{self.name} - AC: {self.ac}  Armor bonus: {self.armor_bonus}  ' \
               f'Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class PaddedArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Padded Armor"
        self.item_type = "Armor"
        self.ac = 10
        self.armor_bonus = 0
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1
        self.a_an = "a set of"


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Leather Armor"
        self.item_type = "Armor"
        self.ac = 11
        self.armor_bonus = 0
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 1
        self.a_an = "a set of"


class StuddedLeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Studded Leather Armor"
        self.item_type = "Armor"
        self.ac = 12
        self.armor_bonus = 0
        self.sell_price = 30
        self.buy_price = 45
        self.minimum_level = 2
        self.a_an = "a set of"


class ScaleMail(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Scale Mail"
        self.item_type = "Armor"
        self.ac = 14
        self.armor_bonus = 0
        self.sell_price = 300
        self.buy_price = 500
        self.minimum_level = 7
        self.a_an = "a set of"


class HalfPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Half Plate Armor"
        self.item_type = "Armor"
        self.ac = 16
        self.armor_bonus = 0
        self.sell_price = 550
        self.buy_price = 750
        self.minimum_level = 12
        self.a_an = "a set of"


class FullPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Full Plate Armor"
        self.item_type = "Armor"
        self.ac = 18
        self.armor_bonus = 0
        self.sell_price = 1000
        self.buy_price = 1500
        self.minimum_level = 15
        self.a_an = "a set of"


class Shield:

    def __init__(self):
        self.name = "Shield"
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class NoShield(Shield):  # default
    def __init__(self):
        super().__init__()
        self.name = "No Shield"
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = ""


class Buckler(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Buckler"
        self.item_type = "Shields"
        self.ac = 1
        self.sell_price = 5
        self.buy_price = 50
        self.minimum_level = 1  # 2
        self.a_an = "a"


class KiteShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Kite Shield"
        self.item_type = "Shields"
        self.ac = 2
        self.sell_price = 50
        self.buy_price = 100
        self.minimum_level = 7
        self.a_an = "a"


class QuantumTowerShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Tower Shield"
        self.item_type = "Shields"
        self.ac = 3
        self.sell_price = 375
        self.buy_price = 700
        self.minimum_level = 12
        self.a_an = "a"


class Boots:

    def __init__(self):
        self.name = ""
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a pair of"

    def __repr__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class LeatherBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Leather Boots"
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 1
        self.buy_price = 1
        self.minimum_level = 1
        self.a_an = "a pair of"


class ElvenBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Elven Boots"
        self.item_type = "Boots"
        self.ac = 1
        self.sell_price = 30
        self.buy_price = 50
        self.minimum_level = 1
        self.a_an = "a pair of"


class AncestralFootsteps(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Ancestral Footsteps"
        self.item_type = "Boots"
        self.ac = 2
        self.sell_price = 300
        self.buy_price = 500
        self.minimum_level = 10
        self.a_an = "a pair of"


class Cloak:

    def __init__(self):
        self.name = ""
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Stealth: {self.stealth}  Minimum level: {self.minimum_level}  ' \
               f'Purchase Price: {self.buy_price} GP'


class CanvasCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Canvas Cloak"
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 1
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"


class ElvenCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Elven Cloak"
        self.item_type = "Cloaks"
        self.stealth = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1
        self.a_an = "an"


# belt items
class Healing:
    def __init__(self):
        self.name = ""
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 0
        self.sell_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class Elixir:
    def __init__(self):
        self.name = "Clarifying Elixir"
        self.item_type = "Elixirs"
        self.uses = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class Antidote:
    def __init__(self):
        self.name = "Vial of Antidote"
        self.item_type = "Antidotes"
        self.uses = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class HealingPotion(Healing):
    def __init__(self):
        super().__init__()
        self.name = "Potion of Healing"
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class StrengthPotion:
    def __init__(self):
        self.name = "Potion of Strength"
        self.item_type = "Potions of Strength"
        self.duration = 5
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class TownPortalImplements:

    def __init__(self):
        self.name = "Scroll of Town Portal"
        self.item_type = "Town Portal Implements"
        self.protect = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1
        self.uses = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


# rings
class Regeneration:

    def __init__(self):
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return self.name


class DefaultRingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "No Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


class RingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


class Protection:

    def __init__(self):
        self.name = ""
        self.item_type = "Rings"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return self.name


class DefaultRingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "No Ring of Protection"
        self.item_type = "Rings of Protection"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


class RingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "Ring of Protection"
        self.item_type = "Rings of Protection"
        self.protect = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


top_level_loot_dict = {
    'Armor': [LeatherArmor, StuddedLeatherArmor, ScaleMail, HalfPlate, FullPlate],
    'Shields': [Buckler, KiteShield, QuantumTowerShield],
    'Boots': [ElvenBoots, AncestralFootsteps],
    'Cloaks': [ElvenCloak],
    'Weapons': [ShortAxe, BroadSword, GreatSword, ElvishGreatSword, QuantumSword,
                BattleAxe, GreatAxe, QuantumAxe],
    'Elixirs': [Elixir],
    'Healing': [HealingPotion],
    'Rings of Regeneration': [RingOfRegeneration],
    'Rings of Protection': [RingOfProtection],
    'Town Portal Implements': [TownPortalImplements],
    'Potions of Strength': [StrengthPotion],
    'Antidotes': [Antidote]}


def undead_prophet_returns():
    return "Undead Prophet"


def king_returns():
    return "King Boss"


def nothing_happens():
    print(f"Nothing happens....")
    pause()
    return


def npc_retreat_counter_logic(npc):
    # called from self.monster_attacks_npc_meta(), for each npc, if retreating
    npc.retreat_counter += 1
    if npc.retreat_counter >= npc.retreat_counter_threshold:
        return npc_end_of_turn_calculation(npc)


def npc_end_of_turn_calculation(npc):
    # called from npc_calculation()
    # when monster defeated, turned, or no longer in proximity, npc allies no longer in retreat
    # they also fully heal
    # also called from npc_retreat_counter_logic() when npc.retreat_counter >= npc.retreat_counter_threshold
    if npc.retreating:
        npc.retreating = False
        npc.retreat_counter = 0
        print(f"{npc.name} is no longer retreating")
        sleep(1)
    if npc.hit_points < npc.maximum_hit_points:
        print(f"{npc.name} heals to full strength.")
        npc.hit_points = npc.maximum_hit_points
        sleep(1)


# NPC allies


class VozzBozz:

    def __init__(self):
        self.name = "Vozzbozz"
        self.level = 13
        self.quantum_level = 6
        self.maximum_quantum_units = 6000
        self.quantum_units = 6000
        self.experience = 0
        self.base_dc = 10
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = QuantumSword()
        self.armor = HalfPlate()
        self.shield = NoShield()
        self.boots = ElvenBoots()
        # self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 13
        self.strength_bonus = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 16
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 14
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 20
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 20
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 18
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 8
        self.acumen = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 199 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus + self.shield.ac +
                            self.boots.ac + self.dexterity_modifier)
        self.protect = 6
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


class SiKira:

    def __init__(self):
        self.name = "Si'Kira"
        self.level = 10
        self.quantum_level = 2
        self.maximum_quantum_units = 2
        self.quantum_units = 6
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = ElvishGreatSword()
        self.armor = ScaleMail()
        self.shield = KiteShield()
        self.boots = ElvenBoots()
        # self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 13
        self.strength_bonus = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 17
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 14
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 16
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 16
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 18
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 8
        self.acumen = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 70 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac
                            + self.dexterity_modifier)
        self.protect = 3
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 2  # 2 full rounds of retreat, not including initial round


class TorBron:

    def __init__(self):
        self.name = "Tor'Bron"
        self.level = 10
        self.quantum_level = 2
        self.maximum_quantum_units = 2
        self.quantum_units = 6
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = QuantumSword()
        self.armor = HalfPlate()
        self.shield = KiteShield()
        self.boots = AncestralFootsteps()
        # self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 17
        self.strength_bonus = 1.5
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 15
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 18
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 14
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 10
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 10
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 12
        self.acumen = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 100 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.protect = 4
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


class Magnus:

    def __init__(self):
        self.name = "Magnus"
        self.level = 10
        self.quantum_level = 5
        self.maximum_quantum_units = 15
        self.quantum_units = 15
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = QuantumAxe()
        self.armor = HalfPlate()
        self.shield = KiteShield()
        self.boots = AncestralFootsteps()
        # self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 16
        self.strength_bonus = 1.33
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 15
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 16
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 14
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 10
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 10
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 10
        self.acumen = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 100 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.protect = 4
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


# Human Player:


class Player:

    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.level = 1
        self.quantum_level = 1
        self.maximum_quantum_units = 2
        self.quantum_units = self.maximum_quantum_units
        self.encounter = 0
        self.experience = 0
        self.base_dc = 8
        self.gold = 0
        self.monsters_on = True  # diagnostic
        self.wielded_weapon = ShortSword()
        self.wielded_weapon.damage_bonus = 0
        self.armor = PaddedArmor()
        self.shield = NoShield()
        self.boots = LeatherBoots()
        # self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = strength
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = dexterity
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = constitution
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = intelligence
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = wisdom
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = charisma
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 10
        self.acumen = 1
        self.maximum_hit_points = 12 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points  # Hit Points at 1st Level: 10 + your Constitution modifier
        self.in_proximity_to_monster = False
        self.is_paralyzed = False
        self.cloak = CanvasCloak()
        self.ring_of_prot = DefaultRingOfProtection()
        self.ring_of_reg = DefaultRingOfRegeneration()
        self.extra_attack = False
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.stealth = self.cloak.stealth
        self.town_portals = 1
        self.elixirs = 1
        self.potions_of_healing = 1
        self.antidotes = 1
        self.potions_of_strength = 1
        self.potion_of_strength_effect = False
        self.potion_of_strength_uses = 0
        self.max_quantum_strength_uses = self.quantum_level + self.strength_modifier
        self.quantum_strength_uses = 0
        self.quantum_strength_effect = False
        self.protection_effect = False
        self.protection_effect_uses = 0
        self.max_protection_effect_uses = self.quantum_level + self.constitution_modifier
        self.protection_effect_value = 0
        self.poisoned = False
        self.poisoned_turns = 0
        self.max_poisoned_turns = 0
        self.necrotic = False
        self.necrotic_turns = 0
        self.dot_multiplier = 1
        self.dot_turns = 1
        # self.current_dungeon_level = 1
        self.dungeon_key = 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        self.discovered_interactives = []
        self.discovered_monsters = []
        self.position = 0
        self.x = 0
        self.y = 0
        self.coordinates = (self.x, self.y)
        self.previous_x = 0
        self.previous_y = 0
        self.in_a_pit = False
        self.vanquished_foes = []
        self.sikira = SiKira()
        self.torbron = TorBron()
        self.magnus = Magnus()
        self.vozzbozz = VozzBozz()
        self.sikira_ally = False
        self.torbron_ally = False
        self.magnus_ally = False
        self.vozzbozz_ally = False
        self.boss_hint_1 = False
        self.boss_hint_1_event = False
        self.boss_hint_2 = False
        self.boss_hint_2_event = False
        self.boss_hint_3 = False
        self.boss_hint_3_event = False
        self.forced_portal = False
        # self.boss_hint_4 = False
        # self.boss_hint_4_event = False
        # self.boss_hint_5 = False
        # self.boss_hint_5_event = False
        # self.boss_hint_6 = False
        # self.boss_hint_6_event = False
        self.loaded_game = False
        self.forest_explored = False
        self.town_portal_exists = False
        self.in_town = False
        self.in_dungeon = False
        self.game_complete = False
        self.pack = {
            'Armor': [],
            'Shields': [],
            'Boots': [],
            'Weapons': [],
            'Cloaks': []

        }

    def dungeon_theme(self):
        if os.name == 'nt':
            if not self.in_a_pit:
                sound_player_loop('dungeon_theme_2.wav')
            else:
                pit_theme()

    def regenerate(self):
        if self.hit_points < self.maximum_hit_points and self.ring_of_reg.regenerate > 0:
            regeneration = self.ring_of_reg.regenerate
            self.hit_points = self.hit_points + regeneration
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points
            print(f"*YOU REGENERATE + {regeneration}*")  # remove after testing
            sleep(1)
        return

    def restart(self):
        # called from self.town_navigation()
        print("Restart..")
        sleep(.5)
        if are_you_sure():
            random_floppy_rw_sound()
            sleep(3)
            cls()
            self.in_town = False
            return "Restart"
        else:
            return False

    def end_game_check(self, monster):
        # called from main loop
        if monster.proper_name == "Queen Jannbrielle the Wicked":
            self.game_complete = True
            return True
        else:
            return False

    def end_game_character_condition_resets(self):  # player defeats final boss
        # called from main loop.
        # reset character conditions before saving character with end_game_routine()

        # give player weird sword as reward for game completion
        self.wielded_weapon = WeirdSword()

        # remove allies
        self.torbron_ally = False
        self.magnus_ally = False
        self.vozzbozz_ally = False
        self.sikira_ally = False

        # reset calculations
        self.poisoned = False
        self.poisoned_turns = 0
        self.necrotic = False
        self.necrotic_turns = 0
        self.potion_of_strength_effect = False
        self.potion_of_strength_uses = 0
        self.quantum_strength_effect = False
        self.quantum_strength_uses = 0
        self.protection_effect = False
        self.protection_effect_uses = 0
        self.protection_effect_value = 0

        # reset to full health:
        self.hit_points = self.maximum_hit_points
        # reset to full quantum units:
        self.quantum_units = self.maximum_quantum_units

        # put player back at level 1:
        self.monsters_on = True
        self.town_portal_exists = True  # transport player back to town. on replay, player will re-enter portal
        self.dungeon_key = 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        (self.x, self.y) = self.dungeon.staircase
        self.coordinates = (self.x, self.y)
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = 0  # self.dungeon.grid[self.y][self.x]
        self.hud()

    def end_game_routine(self):
        # called from self.choose_to_play_again()
        self.game_complete = False  # reset condition for replay
        final_victory_theme()
        cls()
        teletype_txt_file('end_game.txt')
        pause()
        cls()
        teletype_txt_file('end_game2.txt')
        pause()
        cls()
        teletype(f"Congratulations!\nYou have defeated Wicked Queen Jannbrielle and restored peace to the realm.\n")
        pause()

        save_a_character = self.name + ".sav"
        p = Path(__file__).with_name(save_a_character)
        # same_line_print(f"Saving {self.name}")
        # random_floppy_rw_sound()
        # dot_dot_dot(15)

        with p.open('wb') as character_filename:  # 'wb'
            pickle.dump(self, character_filename)
            print(f"Well done, {self.name}.\n")
            sleep(2)

        cls()
        teletype_txt_file('credits.txt')
        pause()
        cls()
        teletype_txt_file('credits2.txt')
        pause()
        cls()
        teletype_txt_file('credits3.txt')
        pause()
        cls()
        print(f"\nSauengard Copyright 2022, JULES PITSKER  (pitsker@proton.me)\nAll rights reserved\n")
        pause()

        '''while True:
            cls()
            try_again = input("Do you wish to play again (y/n)? ").lower()
            if try_again == "y":
                sleep(1.5)
                cls()
                self.in_proximity_to_monster = False
                self.in_dungeon = False
                self.in_town = False
                # player_is_dead = False
                return True  # return to self.choose_to_play_again() and main loop, which will break and reset game
            if try_again == "n":
                print(f"Farewell.")
                sleep(1.5)
                cls()
                sys.exit()'''

    def save_character(self):
        # called from self.town_navigation()
        save_a_character = self.name + ".sav"
        p = Path(__file__).with_name(save_a_character)

        if p.is_file():

            while True:
                self.hud()
                confirm_save = input(f"{self.name} already saved. Overwrite? (y/n)? ").lower()

                if confirm_save == 'n':
                    return

                elif confirm_save == 'y':
                    break

        same_line_print(f"Saving {self.name}")
        random_floppy_rw_sound()
        dot_dot_dot(15)
        with p.open('wb') as character_filename:  # 'wb'
            pickle.dump(self, character_filename)
            same_line_print(f"{self.name} saved.\n")
            sleep(2)
        tavern_theme()
        # town_theme()
        return

    def hud(self):
        cls()
        print(f"{self.name}")

        print(f"Level: {self.level} ({self.level}d{self.hit_dice})")
        print(f"Experience: {self.experience}")
        print(f"Gold: {self.gold}")
        print(f"Weapon: {self.wielded_weapon.name} (Damage Bonus: {self.wielded_weapon.damage_bonus}) "
              f"(To-hit bonus: {self.wielded_weapon.to_hit_bonus})")
        if self.armor.armor_bonus > 0:
            print(f"Armor: {self.armor.name} (AC: {self.armor.ac}) (ARMOR BONUS: {self.armor.armor_bonus}")
        else:
            print(f"Armor: {self.armor.name} (AC: {self.armor.ac})")
        print(f"Shield: {self.shield.name} (AC: {self.shield.ac})")
        print(f"Boots: {self.boots.name} (AC: {self.boots.ac})")
        print(f"Your Armor Class: {self.armor_class}")
        print(f"Strength: {self.strength} (Modifier: {self.strength_modifier})")
        print(f"Dexterity: {self.dexterity} (Modifier: {self.dexterity_modifier})")
        print(f"Constitution: {self.constitution} (Modifier: {self.constitution_modifier})")
        print(f"Intelligence: {self.intelligence} (Modifier: {self.intelligence_modifier})")
        print(f"Wisdom: {self.wisdom} (Modifier: {self.wisdom_modifier})")
        print(f"Charisma: {self.charisma} (Modifier: {self.charisma_modifier})")
        print(f"Hit points: {self.hit_points}/{self.maximum_hit_points}")
        print(f"Quantum units: {self.quantum_units}/{self.maximum_quantum_units}")
        print(f"Cloak: {self.cloak.name} (Stealth: {self.stealth})")

        if self.potions_of_strength > 0:
            print(f"Potions of Giant Strength: {self.potions_of_strength}")
        if self.potions_of_healing > 0:
            print(f"Potions of Healing: {self.potions_of_healing}")
        if self.town_portals > 0:
            print(f"Town Portal Scrolls: {self.town_portals}")
        if self.elixirs > 0:
            print(f"Elixirs: {self.elixirs}")
        if self.antidotes > 0:
            print(f"Vials of Antidote: {self.antidotes}")
        if self.ring_of_reg.name != "No Ring of Regeneration":
            print(f"Ring of Regeneration: +{self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != "No Ring of Protection":
            print(f"Ring of Protection: +{self.ring_of_prot.protect}")
        if self.potion_of_strength_effect and self.potion_of_strength_uses > -1:
            print(f"(STRENGTH POTION EFFECT)  ({self.potion_of_strength_uses}/{self.max_quantum_strength_uses})")
        if self.quantum_strength_effect and self.quantum_strength_uses > -1:
            print(f"QUANTUM STRENGTH EFFECT)  ({self.quantum_strength_uses}/{self.max_quantum_strength_uses})")
        if self.protection_effect and self.protection_effect_uses > -1:
            print(f"(PROT/EVIL: {self.protection_effect_value}) "
                  f"({self.protection_effect_uses}/{self.max_protection_effect_uses})")
        if self.poisoned:
            print(f"(POISONED)  Poison clarifying: ({self.poisoned_turns}/{self.dot_turns})")
        if self.necrotic:
            print(f"(NECROTIC)  Necrotic clarifying: ({self.necrotic_turns}/{self.dot_turns})")
        if self.sikira_ally:
            print(f"ALLIES:")
            npc_ally_hud_sub_function(self.sikira)
            if self.torbron_ally:
                npc_ally_hud_sub_function(self.torbron)
            if self.magnus_ally:
                npc_ally_hud_sub_function(self.magnus)
            if self.vozzbozz_ally:
                npc_ally_hud_sub_function(self.vozzbozz)
        print()
        return

    # CALCULATION
    def monster_attacks_npc_meta(self, monster):
        # called from main loop, after monster attacks human player. (also called after paralyze attacks.)
        # if monster has multi_attack ability, monster attacks all npc allies
        self.hud()
        # monster.multi_attack ability allows monster to attack ALL npc allies
        if monster.multi_attack:
            if self.sikira_ally:
                if not self.sikira.retreating:
                    monster.meta_monster_vs_npc_function(self.sikira)
                    self.npc_retreat_logic(self.sikira)
                    self.hud()
                else:
                    npc_retreat_counter_logic(self.sikira)
            if self.torbron_ally:
                if not self.torbron.retreating:
                    monster.meta_monster_vs_npc_function(self.torbron)
                    self.npc_retreat_logic(self.torbron)
                    self.hud()
                else:
                    npc_retreat_counter_logic(self.torbron)
            if self.magnus_ally:
                if not self.magnus.retreating:
                    monster.meta_monster_vs_npc_function(self.magnus)
                    self.npc_retreat_logic(self.magnus)
                    self.hud()
                else:
                    npc_retreat_counter_logic(self.magnus)
            if self.vozzbozz_ally:
                if not self.vozzbozz.retreating:
                    monster.meta_monster_vs_npc_function(self.vozzbozz)
                    self.npc_retreat_logic(self.vozzbozz)
                    self.hud()
                else:
                    npc_retreat_counter_logic(self.vozzbozz)
            return

        elif monster.lesser_multi_attack:

            # monster.lesser_multi_attack. create a list of non-retreating allies, if any:
            allies = []

            if self.sikira_ally:
                if not self.sikira.retreating:
                    allies.append(self.sikira)
                else:
                    npc_retreat_counter_logic(self.sikira)

            if self.torbron_ally:
                if not self.torbron.retreating:
                    allies.append(self.torbron)
                else:
                    npc_retreat_counter_logic(self.torbron)

            if self.magnus_ally:
                if not self.magnus.retreating:
                    allies.append(self.magnus)
                else:
                    npc_retreat_counter_logic(self.magnus)

            if self.vozzbozz_ally:
                if not self.vozzbozz.retreating:
                    allies.append(self.vozzbozz)
                else:
                    npc_retreat_counter_logic(self.vozzbozz)

            # one ally is then randomly chosen and attacked by monster:
            if len(allies):
                ally = random.choice(allies)
                monster.meta_monster_vs_npc_function(ally)
                self.npc_retreat_logic(ally)

    def npc_retreat_logic(self, npc):
        # called from self.monster_attacks_npc_meta(), after monster attack turn
        if npc.hit_points < 1:
            npc.retreating = True
            self.hud()
            print(f"{npc.name} is retreating!")
            pause()

    def npc_calculation(self):
        # called from main loop, after player end_of_turn_calculation()
        # when monster defeated, turned, or no longer in proximity, npc allies no longer in retreat
        # they also fully heal
        if self.sikira_ally:
            npc_end_of_turn_calculation(self.sikira)
        if self.torbron_ally:
            npc_end_of_turn_calculation(self.torbron)
        if self.magnus_ally:
            npc_end_of_turn_calculation(self.magnus)
        if self.vozzbozz_ally:
            npc_end_of_turn_calculation(self.vozzbozz)

    def end_of_turn_calculation(self):
        # called from main loop at end of player navigation, or battle turn
        self.regenerate()
        self.calculate_potion_of_strength()  # potions of strength have max uses = self.max_quantum_strength_uses
        self.calculate_quantum_strength()  # self.max_quantum_strength_uses= self.quantum_level + self.strength_modifier
        self.calculate_protection_effect()  # max_protection_effect_uses= self.quantum_level+ self.constitution_modifier
        self.calculate_poison()  # poison wears off after self.dot_turns which = monster.dot_turns during battle
        self.calculate_necrotic_dot()  # necrosis wears off after self.dot_turns which = monster.dot_turns during battle

    def calculate_stealth(self):
        # called from found_cloak_substitution() as well as item_management()
        self.stealth = self.cloak.stealth
        return

    def calculate_armor_class(self):
        # called from monster_likes_you(), item_management(), found_shield_substitution, found_armor_substitution()
        self.armor_class = self.armor.ac + self.armor.armor_bonus + \
                           self.shield.ac + self.boots.ac + self.dexterity_modifier
        return

    def calculate_poison(self):
        # called from end_of_turn_calculation() meta function
        if self.poisoned:

            if self.poisoned_turns >= self.dot_turns:
                self.poisoned = False
                self.poisoned_turns = 0
                print(f"The poison leaves your body..")
                sleep(1.5)

            else:
                self.poisoned = True
                self.poisoned_turns += 1
                poison_damage = (1 * self.dot_multiplier)
                self.hit_points -= poison_damage
                print(f"*POISON DAMAGE: {poison_damage}*")
                sleep(1.5)

        return self.poisoned

    def calculate_necrotic_dot(self):
        # called from end_of_turn_calculation() meta function
        if self.necrotic:

            if self.necrotic_turns >= self.dot_turns:
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The necrotic plague leaves your body..")
                sleep(1.5)

            else:
                self.necrotic = True
                self.necrotic_turns += 1
                necrotic_damage = (1 * self.dot_multiplier)
                self.hit_points -= necrotic_damage
                print(f"*NECROTIC DAMAGE -{necrotic_damage}*")
                sleep(1.5)

        return self.necrotic

    def calculate_quantum_strength(self):
        # called from end_of_turn_calculation() meta function
        if self.quantum_strength_effect:

            if self.quantum_strength_uses >= self.max_quantum_strength_uses:  # self.quantum_lvl+self.strength_modifier
                self.quantum_strength_effect = False
                self.quantum_strength_uses = 0
                print(f"The Quantum Effects wear off....the giant strength leaves your body..")
                pause()

            else:
                self.quantum_strength_effect = True
                self.quantum_strength_uses += 1

        return self.quantum_strength_effect

    def calculate_potion_of_strength(self):
        # called from end_of_turn_calculation() meta function
        if self.potion_of_strength_effect:

            if self.potion_of_strength_uses >= self.max_quantum_strength_uses:  # self.strength_modifier + 2:
                self.potion_of_strength_effect = False
                self.potion_of_strength_uses = 0
                print(f"The potion's effect wears off....the giant strength leaves your body..")
                pause()

            else:
                self.potion_of_strength_effect = True
                self.potion_of_strength_uses += 1

        return self.potion_of_strength_effect

    def calculate_protection_effect(self):
        # called from end_of_turn_calculation() meta function
        if self.protection_effect:

            if self.protection_effect_uses >= self.max_protection_effect_uses:
                self.protection_effect = False
                self.protection_effect_uses = 0
                self.protection_effect_value = 0
                print(f"The Quantum Protection effect wears off...")
                pause()

            else:
                self.protection_effect = True
                self.protection_effect_uses += 1
                # self.protection_effect_value = (2 + self.level)
                if self.protection_effect_value > 10:  # beta
                    self.protection_effect_value = 10

        return self.protection_effect

    def calculate_modifiers(self):
        # called from augmentation_system(), increase_random_ability(), decrease_random_ability(),
        # level_up(), increase_lowest_ability() and decrease_lowest_ability()
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        # When your Constitution modifier increases by 1,
        # your hit point maximum increases by 1 for each level you have attained.
        before_con_mod = self.constitution_modifier
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        after_con_mod = self.constitution_modifier
        if after_con_mod > before_con_mod:
            print(f"Weird powers are stirred up within you...")
            sleep(1)
            self.maximum_hit_points += self.level
            self.hit_points = self.maximum_hit_points
            print(f"Your Constitution Modifier has increased from {before_con_mod} to {after_con_mod}!")
            sleep(1)
            print(f"You gain {self.level} maximum hit points!")
            sleep(1)
            print(f"You feel your vitality surge.")
            sleep(1)
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.max_protection_effect_uses = self.quantum_level + self.constitution_modifier
        self.max_quantum_strength_uses = self.quantum_level + self.strength_modifier
        return

    def calculate_acumen(self):
        # called from level_up()
        if self.level == 1:
            self.acumen = 1

        if self.level > 1 < 4:
            self.acumen = 2

        if self.level > 3 < 7:
            self.acumen = 3

        if self.level > 6 < 13:
            self.acumen = 4

        if self.level > 12 < 17:
            self.acumen = 5

        if self.level > 16:
            self.acumen = 6

        return

    # Quantum LEVEL   EXPERIENCE LEVEL
    #                    NEEDED TO USE
    # 1                       1
    # 2                       3
    # 3                       6
    # 4                       9
    # 5                       12
    # 6                       15

    def calculate_current_level(self):
        # called from level_up()
        if self.experience < 300:
            self.level = 1
            self.quantum_level = 1
            self.maximum_quantum_units = 2

        if self.experience >= 300 < 900:
            self.level = 2
            self.quantum_level = 1
            self.maximum_quantum_units = 4

        if self.experience >= 900 < 2700:
            self.level = 3
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 2700 < 6500:
            self.level = 4
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 6500 < 14000:
            self.level = 5
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 14000 < 23000:
            self.level = 6
            self.quantum_level = 3
            self.maximum_quantum_units = 8

        if self.experience >= 23000 < 34000:
            self.level = 7
            self.quantum_level = 3
            self.maximum_quantum_units = 8

        if self.experience >= 34000 < 48000:
            self.level = 8
            self.quantum_level = 4
            self.maximum_quantum_units = 10

        if self.experience >= 48000 < 64000:
            self.level = 9
            self.quantum_level = 4
            self.maximum_quantum_units = 10

        if self.experience >= 64000 < 85000:
            self.level = 10
            self.quantum_level = 5
            self.maximum_quantum_units = 12

        if self.experience >= 85000 < 100000:
            self.level = 11
            self.quantum_level = 5
            self.maximum_quantum_units = 12

        if self.experience >= 100000 < 120000:
            self.level = 12
            self.quantum_level = 5
            self.maximum_quantum_units = 14

        if self.experience >= 120000 < 140000:
            self.level = 13
            self.quantum_level = 5
            self.maximum_quantum_units = 16

        if self.experience >= 140000 < 165000:
            self.level = 14
            self.quantum_level = 5
            self.maximum_quantum_units = 18

        if self.experience >= 165000 < 195000:
            self.level = 15
            self.quantum_level = 6
            self.maximum_quantum_units = 18

        if self.experience >= 195000 < 225000:
            self.level = 16
            self.quantum_level = 6
            self.maximum_quantum_units = 20

        if self.experience >= 225000 < 265000:
            self.level = 17
            self.quantum_level = 6
            self.maximum_quantum_units = 24

        if self.experience >= 265000 < 305000:
            self.level = 18
            self.quantum_level = 6
            self.maximum_quantum_units = 30

        if self.experience >= 305000 < 355000:
            self.level = 19
            self.quantum_level = 6
            self.maximum_quantum_units = 36

        if self.experience >= 355000:
            self.level = 20
            self.quantum_level = 6
            self.maximum_quantum_units = 1000

        return

    # LEVEL AND EXPERIENCE
    def augment_eligibility(self):
        if self.strength < 20 or self.dexterity < 20 or self.constitution < 20 or self.intelligence < 20 \
                or self.wisdom < 20 or self.charisma < 20:
            return True
        else:
            print(f"All attributes at maximum!")  # remove after testing
            return False

    def augmentation_system(self):
        # called from level_up()
        # Attribute augmentation at levels 4, 6, 8, 10, 12, 14, 16, 18
        # also, if player goes up more than one level, by gaining a large amount of experience,
        # augmentation is available

        while True:
            self.hud()
            tries = 0
            points = 2
            while True:
                self.hud()

                if tries > 1:
                    return

                attribute_dict = self.__dict__  # create variable as actual copy of player dict attribute
                attribute_lst = []  # list to be populated with all attributes < 20
                # the working dict and 'for' loop just takes the place of many 'if:' statements
                working_dict = {'strength': self.strength, 'dexterity': self.dexterity,
                                'constitution': self.constitution, 'intelligence': self.intelligence,
                                'wisdom': self.wisdom, 'charisma': self.charisma}

                # add all attributes < 20 in working dict to ability_lst to define attributes you are allowed to change:
                for key, value in working_dict.items():
                    if value < 20:
                        attribute_lst.append(key)

                # this code is reachable if stats are maxed out, and level_up() calls it:
                if not len(attribute_lst):  # if ability list is empty, all stats at 20; no more improvements allowed
                    print(f"All of your attributes are at the maximum level!")
                    sleep(1.25)
                    return

                print(f"Attribute Augmentation\n"
                      f"Player level: {self.level}")
                print(f"Points to distribute: {points}")
                # create a subset ability dictionary from the ability list by indexing, and then print out
                attribute_dict_subset_too = {}
                for attribute in attribute_lst:
                    if len(attribute_lst):
                        attribute_dict_subset_too[attribute_lst.index(attribute)] = attribute
                for key, value in attribute_dict_subset_too.items():
                    print(key + 1, ':', value.capitalize())  # add 1 to key since indexing begins at 0

                try:
                    attribute_index = int(input(f"Enter the attribute to improve.\n"
                                                f"(THIS IS PERMANENT!) : "))
                    attribute_index -= 1  # indexing begins at zero...
                    attribute_to_improve = (attribute_dict_subset_too[attribute_index])
                    old_score = attribute_dict[attribute_to_improve]
                    attribute_dict[attribute_to_improve] += 1
                    print(
                        f"Your {attribute_to_improve} has been increased from {old_score} "
                        f"to {attribute_dict[attribute_to_improve]}!")
                    self.calculate_modifiers()
                    tries += 1
                    points -= 1
                    pause()
                    continue

                except (ValueError, KeyError):
                    print("Invalid entry..")
                    sleep(1)
                    continue

    def level_up(self, exp_award, monster_gold):
        # called from main loop after victory
        self.gold += monster_gold

        before_level = self.level
        before_quantum_level = self.quantum_level
        before_acumen = self.acumen

        self.experience += exp_award
        self.calculate_current_level()
        self.calculate_acumen()

        after_acumen = self.acumen
        after_level = self.level
        level_multiplier = (after_level - before_level)  # in case player goes up more than 1 level
        after_quantum_level = self.quantum_level

        if after_level > before_level:
            self.quantum_units = self.maximum_quantum_units  # necessary code for advancing from level 1 to 2

            if monster_gold > 0:
                print(f"You snarf {monster_gold} gold pieces.")
                sleep(1)
            print(f"You gain {exp_award} experience points.")
            sleep(2)
            gong()
            if level_multiplier > 1:
                print(f"You have gained {level_multiplier} experience levels!")
            elif level_multiplier == 1:
                print(f"You went up a level!!")
            sleep(2)
            print(f"You are now level {self.level}.")
            sleep(2)
            self.dungeon_theme()
            self.calculate_acumen()
            gain_hit_points1 = (dice_roll(1, self.hit_dice) + self.constitution_modifier) * level_multiplier  # method 1
            gain_hit_points2 = (6 + self.constitution_modifier) * level_multiplier  # hp increase method 2
            hit_point_list = [gain_hit_points1, gain_hit_points2]
            gain_hit_points = max(hit_point_list)  # the highest of method 1 and 2
            self.hit_points += gain_hit_points  # you heal and gain max hp (previous HP + Hit Die roll + CON modifier)
            self.maximum_hit_points += gain_hit_points
            print(f"You gain {gain_hit_points} hit points")
            sleep(2.5)

            # Attribute augmentation at levels 4, 6, 8, 10, 12, 14, 16, 18
            # augmentation logic
            # This logic also works for players going up more than one level,
            # e.g. vanquishing a monster with very high experience reward
            # Logic works by creating 2 lists and comparing whether the player's current level, or any levels between
            # their last level and current level are augmentation eligible.
            # Ranges are initially counterintuitive in python;
            # they do not include the last number in range, so I added +1 to end_range
            # Also, for the current purposes, I added +1 to start_range as well, since we don't want to award augments
            # based on the previous experience level, only on current level and any eligible levels between.

            range_1 = range((before_level + 1), (after_level + 1), 1)  # enumerate levels between, inc. after_level by 1
            all_levels_between = list(range_1)  # create a list containing levels between, including after_level
            augment_levels = [4, 6, 8, 10, 12, 14, 16, 18]

            # check if any levels between are augmentation levels by comparing elements from both lists
            # number_of_augment_awards = sum of all_levels_between elements which exist in augment_levels:
            number_of_augment_awards = sum(el in all_levels_between for el in augment_levels)
            augment_level_check = False
            if number_of_augment_awards > 0:
                augment_level_check = True

            if augment_level_check:
                if self.augment_eligibility():  # ensure player has at least 1 ability value < 20
                    if number_of_augment_awards > 1:
                        print(f"You have earned {number_of_augment_awards} ability augments!")
                        pause()

                    augmentation_intro()
                    for i in range(number_of_augment_awards):
                        self.augmentation_system()
                    if not self.game_complete:
                        print(f"You savor the empowering augmentation you have gained..\n"
                              f"And yet, the dungeon horde grows more powerful with you!")
                        pause()
                    self.hud()

            self.calculate_modifiers()

            if 5 in all_levels_between:  # players gain extra attack skill at level 5 # if self.level == 5:
                self.extra_attack = True
                print("You gain the Extra Attack skill!!")
                pause()
                self.hud()

            if after_acumen > before_acumen:
                print(f"Your Acumen increases from {before_acumen} to {after_acumen}!")
                pause()
                self.hud()

            if after_quantum_level > before_quantum_level:
                print(f"Your Quantum knowledge level increases from {before_quantum_level} to {after_quantum_level}!")
                self.quantum_units = self.maximum_quantum_units
                pause()
                self.hud()

            self.hud()

        else:
            if monster_gold > 0:
                if monster_gold == 1:
                    print(f"You snarf {monster_gold} gold piece.")
                else:
                    print(f"You snarf {monster_gold} gold pieces.")
                sleep(1)
            print(f"You gain {exp_award} experience points.")
            sleep(2)
            self.hud()

    # BATTLE AND PROXIMITY TO MONSTER OCCURRENCES

    def try_again_sub_function(self):
        while True:
            cls()
            try_again = input("Do you wish to play again (y/n)? ").lower()
            if try_again == "y":
                sleep(1.5)
                cls()
                self.in_proximity_to_monster = False
                self.in_dungeon = False
                self.in_town = False
                # player_is_dead = False
                return True
            if try_again == "n":
                print(f"Farewell.")
                sleep(1.5)
                cls()
                sys.exit()

    def choose_to_play_again(self):
        # called from main loop if game_over variable is True
        cls()
        gong()
        if not self.game_complete:
            print_txt_file('grim_reaper.txt')
            teletype(f"\n                 "
                     f"Another adventurer has fallen prey to the Sauengard Dungeon!")
            sleep(4.5)
            random_floppy_rw_sound()
            sleep(1)
            if self.try_again_sub_function():
                return True
            '''self.in_proximity_to_monster = False
            self.in_dungeon = False
            self.in_town = False'''
        else:
            self.end_game_routine()  # game is completed
            if self.try_again_sub_function():  # if player chooses to play again
                return True
            '''self.game_complete = False  # reset condition for replay
            mountain_king_theme()
            teletype(f"Congratulations!\nYou have defeated Wicked Queen Jannbrielle and restored peace to the realm.\n")
            pause()

            save_a_character = self.name + ".sav"
            p = Path(__file__).with_name(save_a_character)
            same_line_print(f"Saving {self.name}")
            random_floppy_rw_sound()
            dot_dot_dot(15)

            with p.open('wb') as character_filename:
                pickle.dump(self, character_filename)
                same_line_print(f"{self.name} saved.\n")
                sleep(2)

            cls()
            teletype_txt_file('credits.txt')
            pause()
            cls()
            teletype_txt_file('credits2.txt')
            pause()
            cls()
            teletype_txt_file('credits3.txt')
            pause()
            cls()
            print(f"\n        Sauengard Copyright 2022, JULES PITSKER  (pitsker@proton.me)\nAll rights reserved\n")
            pause()
        while True:
            cls()
            try_again = input("Do you wish to play again (y/n)? ").lower()
            if try_again == "y":
                sleep(1.5)
                cls()
                self.in_proximity_to_monster = False
                self.in_dungeon = False
                self.in_town = False
                # player_is_dead = False
                return True
            if try_again == "n":
                print(f"Farewell.")
                sleep(1.5)
                cls()
                sys.exit()'''

    def encounter_logic(self):
        # called from main loop
        if self.monsters_on:
            self.encounter = dice_roll(1, 20)
        else:
            self.encounter = 15  # this will make it so there are no monsters at all except bosses (for testing, etc)

    def the_monster_is_not_amused(self, monster):
        # called from self.battle_menu_choices() for invalid inputs
        print(f"The {monster.name} is not amused.")
        sleep(.75)
        self.hud()
        return

    def monster_introduction(self, monster):
        # called from main loop
        if monster.name in self.discovered_monsters:
            self.hud()  # placing a hud() here erases the dungeon description; more appropriate
            # print(f"(TESTING) Discovered monsters: {self.discovered_monsters}")  # remove after testing
            print(f"You have encountered {monster.a_an} {monster.name}. Challenge level: {monster.level}")
            # remove lvl after testing
            pause()
        else:
            self.hud()  # placing a hud() here erases the dungeon description; more appropriate
            print(f"{monster.introduction}")

            if self.encounter < 21:  # if not a boss
                self.discovered_monsters.append(monster.name)
            pause()

    def monster_likes_you_or_steals_from_you(self, monster):
        # called from main loop
        if self.encounter < 21:  # if not a boss, monster may like you or steal from you

            if self.monster_likes_you(monster):
                self.in_proximity_to_monster = False
                # player_1.event_logic()  # this will trigger an event without using (L)ook
                self.dungeon_description()
                return True

            if self.quick_move(monster):
                self.in_proximity_to_monster = False
                # player_1.event_logic()  # this will trigger an event without using (L)ook
                self.dungeon_description()
                return True  # if monster steals something he gets away clean, if not, battle

            else:
                return False

        else:
            return False

    def battle_menu_choices(self, monster):
        # main loop battle menu. note that a party of adventurers cannot evade
        while True:
            self.hud()
            monster.monster_data()

            if not self.sikira_ally and not self.torbron_ally and not self.magnus_ally and not self.vozzbozz_ally:
                battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                      "(G)iant Strength potion, (V)ial of Antidote,\n(Q)uantum Effects or "
                                      "(E)vade\nF/H/C/G/V/Q/E --> ").lower()

                if battle_choice in ('f', 'h', 'c', 'g', 'v', 'q', 'e'):
                    return battle_choice

                else:  # invalid inputs
                    self.the_monster_is_not_amused(monster)
                    continue

            else:  # a party of adventurers cannot evade
                battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                      "(G)iant Strength potion, (V)ial of Antidote,\nor (Q)uantum Effects\n"
                                      "F/H/C/G/V/Q --> ").lower()

                if battle_choice in ('f', 'h', 'c', 'g', 'v', 'q'):
                    return battle_choice

                else:  # invalid inputs
                    self.the_monster_is_not_amused(monster)
                    continue

    def check_for_boss(self, event):

        if event == "Elite Monster":
            self.encounter = 95
        if event == "Legendary Monster":
            self.encounter = 96
        elif event == "Undead Prophet":
            self.encounter = 97
        elif event == "King Boss":
            self.encounter = 98
        elif event == "Exit Boss":
            self.encounter = 99
        elif event == "Wicked Queen":
            self.encounter = 100
        else:
            return False

    def victory_statements(self, monster):
        statements_list = [f"You are victorious!", f"You have defeated the {monster.name}.", f"You have vanquished"
                                                                                             f" the {monster.name}.",
                           "You have defeated your enemy.", "Your enemy is defeated."]
        if self.encounter > 20:  # if victory over boss
            gong()
            if monster.proper_name != "None":
                print(f"You have vanquished {monster.proper_name}! You are victorious!")
                self.vanquished_foes.append(monster.proper_name)
            else:
                print(f"You have vanquished the {monster.name}!")
            sleep(4)
            self.dungeon_theme()
        else:
            statement = random.choice(statements_list)
            print(statement)

    def victory_over_boss_logic(self):
        # called from main loop
        if self.encounter == 99:  # if dungeon level exit boss
            self.boss_hint_logic()

    def random_death_statement(self):
        # called from main loop
        random_statements = ["You have succumbed to your injuries!",
                             "Bravely you have fought. Bravely you have died. Rest in Peace."
                             ]
        print(f"{self.name} Level {self.level}")
        print(random.choice(random_statements))
        return

    def meta_monster_generator(self):
        # called from main loop
        monster = None

        if self.encounter < 11:  # regular monster
            monster = self.regular_monster_generator()
            # put testing monster here:
            # from monster_module import Doppelganger
            # monster = Doppelganger()
            return monster

        elif self.encounter == 100:  # final boss
            monster = self.wicked_queen_generator()

        elif self.encounter == 99:  # level exit boss fight
            monster = self.exit_boss_generator()

        elif self.encounter == 98:  # undead king
            monster = self.king_monster_generator()

        elif self.encounter == 97:  # undead prophet
            monster = self.undead_prophet_generator()

        elif self.encounter == 96:  # legendary monster
            monster = self.legendary_monster_generator()

        elif self.encounter == 95:  # elite
            monster = self.elite_monster_generator()

        gong()
        sleep(4)

        if self.encounter == 98:
            mountain_king_theme()

        else:
            boss_battle_theme()

        pause()
        self.hud()
        return monster

    def monster_booster(self, monster):
        # called from monster_generators to boost hit points and experience rewards
        # depending on the existence of NPC allies
        if self.sikira_ally:
            monster.hit_points += self.sikira.hit_points
            monster.experience_award = round(monster.experience_award * 1.25)
        if self.torbron_ally:
            monster.hit_points += self.torbron.hit_points
            monster.experience_award = round(monster.experience_award * 1.25)
        if self.magnus_ally:
            monster.hit_points += self.magnus.hit_points
            monster.experience_award = round(monster.experience_award * 1.25)
        if self.vozzbozz_ally:
            monster.hit_points += self.vozzbozz.hit_points
            monster.experience_award = round(monster.experience_award * 1.25)

        if self. sikira_ally or self.torbron_ally or self.magnus_ally or self.vozzbozz_ally:
            if monster.to_hit_bonus <= self.acumen:  # consider modifying for balance
                monster.to_hit_bonus = self.acumen + 1

            if monster.proper_name == "None":
                monster.name = f"{monster.name} Dreadnought"
            else:
                monster.name = f"{monster.name} Dreadnought"
                monster.proper_name = f"{monster.proper_name} Dreadnought"
        return monster

    def wicked_queen_generator(self):
        # called from meta_monster_generator() if encounter == 100
        wicked_queen = WickedQueenJannbrielle()  # monster_dict([4][0])()
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"The Queen rises from the grotesque throne, her eyes burning with murderous intent!")
        return wicked_queen

    def legendary_monster_generator(self):
        # called from meta_monster_generator() if encounter == 96
        rndm_boss_names = ['Sarlen', 'Sinedor', 'Birlendor', 'Lichtor', 'Renburr',
                           'Belorg', 'Sirlak', 'Gruldirren', 'Falldorren', 'Tilenbor', 'Durjinn',
                           'Morgenoth', 'Tergoam', 'Terdannor', 'Lorenqor', 'Worgoth',
                           'Hahrbinnor', 'Korrendor', 'Karbrath', 'Qintar', 'Wobard',
                           'Sorrikon', 'Dellbrion', 'Selanius', 'Qorron', 'Sorrendir',
                           'Mawleon', 'Sador', 'Qardormirr', 'Bendorn', 'Vallqedon',
                           'Merlkandon']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        boss_monster = monster_cls()
        first_name = random.choice(rndm_boss_names)
        boss_monster.proper_name = f"{first_name} the Legendary {boss_monster.name}"
        boss_monster.hit_points = math.ceil(boss_monster.hit_points * 2)
        boss_monster.experience_award = math.ceil(boss_monster.experience_award * 2)
        boss_monster.strength += 4
        boss_monster.dexterity += 4
        boss_monster.constitution += 4
        boss_monster.intelligence += 4
        boss_monster.wisdom += 4
        boss_monster.charisma += 4
        boss_monster.armor_class += 2
        boss_monster.resistances = ["All"]
        boss_monster.weapon_bonus = math.ceil(self.acumen * 2.5)
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        checked_monster = self.monster_booster(boss_monster)  # beta
        print(f"Before you stands {checked_monster.proper_name}!")
        return checked_monster  # beta
        # return boss_monster

    def elite_monster_generator(self):
        # called from meta_monster_generator() if encounter == 95
        rndm_boss_names = ['Sarlongrath', 'Sundor', 'Birrenol', 'Sontor', 'Marburr',
                           'Belok', 'Sorlak', 'Grildorren', 'Falaur', 'Tildor', 'Durj',
                           'Morgenor', 'Talgram', 'Teldanoth', 'Linmat', 'Worcon',
                           'Hahrmon', 'Kardon', 'Corbrath', 'Willentor', 'Weggard',
                           'Norrikon', 'Fellbrion', 'Sajanus', 'Qorrat', 'Sorenmir',
                           'Kraw', 'Kullador', 'Qardrommir', 'Wiltendorn', 'Valwark',
                           'Morluk']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        boss_monster = monster_cls()
        first_name = random.choice(rndm_boss_names)
        boss_monster.proper_name = f"{first_name} the Elite {boss_monster.name}"
        boss_monster.hit_points = math.ceil(boss_monster.hit_points * 2)
        boss_monster.experience_award = math.ceil(boss_monster.experience_award * 1.5)
        boss_monster.strength += 2
        boss_monster.dexterity += 2
        boss_monster.constitution += 2
        boss_monster.intelligence += 2
        boss_monster.wisdom += 2
        boss_monster.charisma += 2
        boss_monster.armor_class += 2
        boss_monster.dot_multiplier = self.acumen
        boss_monster.experience_award = 350 * self.level
        boss_monster.weapon_bonus = math.ceil(self.level * 1.5)
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        checked_monster = self.monster_booster(boss_monster)  # beta
        print(f"Before you stands {checked_monster.proper_name}!")
        return checked_monster  # beta
        #  return boss_monster

    def regular_monster_generator(self):
        # called from meta_monster_generator() if encounter < 11
        maximum_level = self.level  # (self.level + 1) makes it too hard
        minimum_level = 1

        if self.level > 2:
            minimum_level = (self.level - 2)  # this should keep it more challenging and fun

        regular_monster_key = random.randint(minimum_level, maximum_level)

        if self.encounter == 1:  # beta 5% chance of running into monsters that are +1 level to keep it challenging

            if self.level < 20:
                regular_monster_key = (self.level + 1)

            else:
                regular_monster_key = self.level

        regular_monster_cls = random.choice(monster_dict[regular_monster_key])
        regular_monster = regular_monster_cls()
        checked_monster = self.monster_booster(regular_monster)
        return checked_monster

    def undead_prophet_generator(self):
        # called from meta_monster_generator(), if encounter == 97
        rndm_prophet_names = ['Tacium', 'Amarrik', 'Arynd', 'Beldonnor', 'Forrg',
                              'Sambressorr', 'Jornav', 'Tyrnenn', 'Fenlor', 'Yagoddish', 'Borell',
                              'Ehrnador', 'Thaymorro', 'Gorrel', 'Aureor', 'Linus', 'Mattheus',
                              'Hahrus', 'Astorem', 'Chardast', 'Brendorin', 'Meradorn',
                              'Gorrikor', 'Nannukis', 'Torrolom', 'Ornelius', 'Geffenmor',
                              'Jorrbrialus', 'Koffengen', 'Jyrus', 'Jybrius', 'Tyrrendor',
                              'Forendilus']
        rndm_epithets = ['of the Evil Wisdom', 'the Lesser', 'the Elder', 'the Fierce', 'of the Eleven Elders',
                         'of the Twelve', 'of the Fell Elders', 'the Mad', 'the Blasphemous',
                         'of the Eleven Elders', 'the Fallen', 'the Insane', 'the Mad Magistrate',
                         'the Grand King-Priest', 'of the Seven Minds', 'the Bloodsoaked',
                         'the Accursed', 'the Abandoned', 'the Absolutionist', 'the Avenger', 'of the Seven Horns',
                         'the Blackhearted', 'the Blind', 'the Bloodthirsty', 'the Cruel',
                         'the Damned', 'the Foul', 'the Foulest', 'the Feared', 'the Fear-Inspiring'
                         ]

        undead_prophet = random.choice(undead_prophet_list)
        name = random.choice(rndm_prophet_names)
        epithet = random.choice(rndm_epithets)
        undead_prophet.proper_name = f"{name} {epithet}"
        undead_prophet.hit_points = math.ceil(self.maximum_hit_points * 1.5)
        undead_prophet.level = self.level
        undead_prophet.number_of_hd = self.level
        undead_prophet.weapon_bonus = self.wielded_weapon.damage_bonus
        undead_prophet.dot_multiplier = self.acumen
        undead_prophet.experience_award = 350 * self.level
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        checked_monster = self.monster_booster(undead_prophet)  # beta
        print(f"The undead prophet, {checked_monster.proper_name} returns!")
        return checked_monster  # beta
        #  return undead_prophet

    def exit_boss_generator(self):
        # called from meta_monster_generator(), if encounter == 99
        rndm_boss_names = ['Gwarlek', 'Srentor', 'Borrnol', 'Sentollor', 'Morluk',
                           'Twinbelor', 'Sornog', 'Grenyor', 'Fallraur', 'Timboth', 'Surj',
                           'Morozzor', 'Tharbor', 'Tenbrok', 'Lorrius', 'Filwor',
                           'Hahrmon', 'Kardon', 'Corbrin', 'Billentor', 'Weggard',
                           'Norrus', 'Fellbrion', 'Sajanus', 'Qorag', 'Sorenmor',
                           'Kraw', 'Kullador', 'Qendor', 'Willenbor', 'Valwar',
                           'Moonror']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        exit_boss = monster_cls()
        exit_boss.hit_points = math.ceil(exit_boss.hit_points * 1.25)
        first_name = random.choice(rndm_boss_names)
        exit_boss.proper_name = f"{first_name} the Elite {exit_boss.name} guardian"
        # exit_boss.hit_points = math.ceil(self.maximum_hit_points * 1.5)
        exit_boss.level = self.level
        exit_boss.number_of_hd = self.level
        exit_boss.dot_multiplier = self.dungeon.level
        exit_boss.experience_award = 450 * self.level
        exit_boss.weapon_bonus = self.wielded_weapon.damage_bonus
        checked_monster = self.monster_booster(exit_boss)
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"In the archway to the staircase leading down to {self.dungeon.name} "
              f"stands {checked_monster.proper_name}!\n"
              f"Without fear, without thought, the guardian looks upon you and readies itself for battle...")

        return checked_monster
        #  return exit_boss

    def king_monster_generator(self):
        # called from meta_monster_generator(), if encounter == 98
        rndm_king_names = ['Tartyrtum', 'Amarrok', 'Aaryn', 'Baldrick', 'Farrendal',
                           'Dinenlell', 'Jorn', 'Tyrne', 'Fen', 'Jagod', 'Bevel',
                           'Elrik', 'Thayadore', 'Grummthel', 'Aureus', 'Sylgor',
                           'Hahr', 'Astor', 'Cordast', 'Breckenborn', 'Megarrd',
                           'Gorrik', 'Nannuk', 'Borrodred', 'Metalbeard', 'Geffen',
                           'Jortindale', 'Koffgen', 'Tyrus', 'Tybrius', 'Tyr',
                           'Hammersthorn']
        rndm_epithets = ['the Wise', 'the Lesser', 'the Elder', 'the Fierce', 'of the Eleven', 'of the Twelve',
                         'of the Elders', 'the Brave', 'the Insane', 'the Great', 'the Grand Magistrate',
                         'the Grand King-Priest', 'of the Seven Riddles', 'the Strong', 'the Able', 'the Bloodsoaked',
                         'the Accursed', 'the Abandoned', 'the Absolutist', 'the Avenger', 'the Battle-weary',
                         'the Blackhearted', 'the Blind', 'the Bloodthirsty', 'the Conqueror', 'the Cruel',
                         'the Crusader', 'the Damned'
                         ]

        king_monster = random.choice(king_boss_list)
        name = random.choice(rndm_king_names)
        epithet = random.choice(rndm_epithets)
        king_monster.proper_name = f"{name} {epithet}"
        king_monster.hit_points = math.ceil(self.maximum_hit_points * 1.25)
        king_monster.level = self.level
        king_monster.number_of_hd = self.level
        king_monster.weapon_bonus = self.wielded_weapon.damage_bonus
        king_monster.dot_multiplier = self.dungeon.level
        king_monster.experience_award = 350 * self.level
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        checked_monster = self.monster_booster(king_monster)  # beta
        print(f"The undead King {checked_monster.proper_name} returns!")
        return checked_monster  # beta
        #  return king_monster

    def monster_likes_you(self, monster):
        # called from main loop after encounter with regular monster
        if dice_roll(1, 20) > 19 and monster.intelligence > 12 and monster.charisma > 14 and self.charisma > 11:
            print(f"The {monster.name} likes you!")
            sleep(1)
            upgradeable = True

            while upgradeable:

                if self.armor.ac < 18 or self.shield.ac < 3 or self.wielded_weapon.damage_bonus < 15 or \
                        self.wielded_weapon.to_hit_bonus < 6 or self.boots.ac < 3 \
                        or self.hit_points < self.maximum_hit_points:
                    upgradeable = True

                else:
                    upgradeable = False

                if not upgradeable:
                    gold_gift = random.randint(100, 5000)
                    print(f"{monster.he_she_it.capitalize()} gives you {gold_gift} GP!")
                    self.gold += gold_gift
                    pause()
                    return True

                gift_item = dice_roll(1, 6)

                if gift_item == 1:
                    if (self.armor.ac + self.armor.armor_bonus) < 18:
                        if self.armor.name != "Padded Armor":
                            self.armor.armor_bonus += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.armor.name} "
                                  f"with an Armor Bonus +{self.armor.armor_bonus}!")
                        else:
                            self.armor = LeatherArmor()
                            print(f"{monster.he_she_it.capitalize()} gives you {self.armor.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 2:
                    if self.shield.ac < 3:
                        if self.shield.name != "No Shield":
                            self.shield.ac += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.shield.name} "
                                  f"to AC {self.shield.ac}!")
                        else:
                            self.shield = Buckler()
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.shield.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 3:

                    if self.wielded_weapon.damage_bonus < 15:

                        if self.wielded_weapon.name != "Short Sword":
                            self.wielded_weapon.damage_bonus += 1
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.wielded_weapon.name} "
                                  f"damage bonus to + "
                                  f"{self.wielded_weapon.damage_bonus}!")
                            pause()
                            return True

                        else:
                            self.wielded_weapon = BroadSword()
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.wielded_weapon.name}!")
                            pause()
                            return True
                    else:
                        continue

                if gift_item == 4:
                    if self.wielded_weapon.to_hit_bonus < 6:
                        if self.wielded_weapon.name != "Short Sword":
                            self.wielded_weapon.to_hit_bonus += 1
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.wielded_weapon.name} "
                                  f"to-hit bonus to + "
                                  f"{self.wielded_weapon.to_hit_bonus}!")
                            pause()
                            return True

                        else:
                            self.wielded_weapon = BroadSword()
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.wielded_weapon.name}!")
                            pause()
                            return True
                    else:
                        continue

                if gift_item == 5:
                    if self.boots.ac < 3:

                        if self.boots.name != "Leather Boots":
                            self.boots.ac += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.boots.name} "
                                  f"to AC {self.boots.ac}!")
                        else:
                            self.boots = ElvenBoots()
                            print(f"{monster.he_she_it.capitalize()} gives you a pair of {self.boots.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 6:
                    if self.hit_points < self.maximum_hit_points:
                        self.hit_points = self.maximum_hit_points
                        print(f"{monster.he_she_it.capitalize()} heals you to full strength!")
                        pause()
                        return True
                    else:
                        continue

        else:
            return False

    def quick_move(self, monster):
        # called from main loop
        self.hud()
        quick_move_roll = dice_roll(1, 20)  # - self.stealth
        if quick_move_roll == 20:
            print(f"The {monster.name} makes a quick move...")
            sleep(1.5)
            # pack inventory logic:
            pack_item_types_to_steal = []
            belt_item_types_to_steal = [self.potions_of_strength, self.potions_of_healing,
                                        self.town_portals, self.elixirs, self.antidotes]
            for i in self.pack.keys():  # gather all available
                if len(self.pack[i]) > 0:  # item types to steal based on player's current item TYPES and put them
                    pack_item_types_to_steal.append(i)  # in available_item_types_to_steal = []

            if len(pack_item_types_to_steal) > 0:
                item_type = random.choice(pack_item_types_to_steal)  # Get random item *TYPE* you want to "steal"
                if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type" in their pack
                    # pop random item from that item type. -1 because indexes start at 0
                    stolen_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                    print(f"{monster.he_she_it.capitalize()} steals the {stolen_item.name} "
                          f"from your pack!")
                    pause()
                    return True  # True means monster gets away clean

            # if pack is empty, the thief moves to the belt.
            # Belt inventory is handled differently.
            # belt inventory logic:
            elif sum(belt_item_types_to_steal) > 0:
                item_string = ""
                # Define list of attributes you are allowed to change
                self_dict = self.__dict__  # create self_dict variable as actual copy of player dict attribute
                stealing_lst = []
                # the working dict and 'for' loop just takes the place of many 'if:' statements
                working_dict = {'potions_of_strength': self.potions_of_strength,
                                'potions_of_healing': self.potions_of_healing,
                                'town_portals': self.town_portals, 'elixirs': self.elixirs,
                                'antidotes': self.antidotes}
                # add all items > 0 in working dict to stealing list
                for key, value in working_dict.items():
                    if value > 0:
                        stealing_lst.append(key)
                random_stolen_item = random.choice(stealing_lst)
                # I am proud of this next bit of code :)
                grammar_dict = {'potions_of_strength': 'potion of strength',
                                'potions_of_healing': 'potion of healing',
                                'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir',
                                'antidotes': 'vial of antidote'}
                for key, value in grammar_dict.items():
                    if random_stolen_item == key:
                        item_string = value
                print(f"{monster.he_she_it.capitalize()} steals a {item_string} right off of your belt!")
                self_dict[random_stolen_item] -= 1
                pause()
                return True  # True means monster gets away clean
            else:
                print(f"You have nothing {monster.he_she_it} wants to steal!")
                pause()
                # sleep(2)
                return True  # Changing this to False means your inventory is empty and monster sticks around to fight
        else:
            return False  # False here means monster failed check, and he sticks around to fight; invisible to player

    def reduce_health(self, damage):
        # called from main loop after monster does damage to human player
        self.hit_points -= damage
        # if self.hit_points < 0:  # restore after testing
        #    self.hit_points = 0  # restore after testing
        return

    def check_dead(self):
        # called from main loop after damage and calculations
        # I am proud of this code...it was very difficult for me and took many hours
        if self.hit_points > 0:
            return False
        else:
            self.hud()
            if self.necrotic and self.poisoned:
                print(f"You are necrotic, poisoned, unconscious and moribund!")
            elif self.necrotic:
                print(f"You are necrotic, unconscious and moribund!")
            elif self.poisoned:
                print(f"You are poisoned, unconscious and moribund!")
            else:
                print(f"You are unconscious and moribund!")
            sleep(1)
            print(f"Death resistance throw!")
            sleep(1)
            successes = 0
            fails = 0
            attempt = 0
            while successes < 3 or fails < 3:
                if successes == 3:
                    print(f"You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False  # player is NOT dead
                if fails >= 3:
                    print(f"Death resistence has failed!")
                    sleep(1)
                    return True  # player IS dead
                death_save = dice_roll(1, 20)
                attempt += 1
                print(f"Attempt {attempt}: {death_save}")
                sleep(1)
                if death_save == 20:
                    print(f"20 Roll! You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False  # player is NOT dead
                if death_save > 9:
                    successes += 1
                    if successes == 1:
                        print(f"{successes} Successful save..")
                    else:
                        print(f"{successes} Successful saves..")
                    sleep(1)
                if 10 > death_save > 1:
                    fails += 1
                    if fails == 1:
                        print(f"{fails} Failed save..")
                    else:
                        print(f"{fails} Failed saves..")
                    sleep(1)
                if death_save == 1:
                    fails += 2
                    print(f"Rolling a 1 adds 2 failed saves. ")
                    print(f"{fails} Failed saves..")
                    sleep(1)
            return True  # player IS dead

    def initiative(self, monster):
        # called from main loop after encountering monster.
        self.hud()
        if self.level > 6:
            player_initiative = dice_roll(1, 20) + self.dexterity_modifier + self.acumen
        else:
            player_initiative = dice_roll(1, 20) + self.dexterity_modifier
        if monster.level > 6:  # beta testing
            monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier + monster.evil_bonus
        else:
            monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier
        print(f"Your initiative: {player_initiative}\n{monster.name} initiative: {monster_initiative}")
        pause()  # remove after testing
        if player_initiative >= monster_initiative:
            return True
        else:
            return False

    def melee(self, monster):
        # called from main loop if player chooses to (F)ight
        one_roll = ["You awkwardly strike, and lose your footing..",
                    "Off balance and late, you manage a pitiful attempt and fail.",
                    "Your aim is poor; you miserably fail to land a blow..",
                    "Distracted and unfocused, you lose your concentration and miss.."]
        miss_list = [f"Your {self.wielded_weapon.name} bounces off {monster.his_her_its} {monster.armor_name}!",
                     f"{monster.he_she_it.capitalize()} nimbly moves aside!",
                     f"{monster.he_she_it.capitalize()} deflects your blow!",
                     f"{monster.he_she_it.capitalize()} dodges your blow!",
                     f"{monster.his_her_its.capitalize()} {monster.armor_name} absorbs the damage!"]
        hit_list = ["You land a stabbing blow!", "You successfully land a cutting blow!",
                    f"You manage to wound {monster.him_her_it}!", f"You wound {monster.him_her_it}!",
                    f"You slash {monster.him_her_it}!", f"You land a blow and wound {monster.him_her_it}!",
                    f"Your {self.wielded_weapon.name} lands and wounds {monster.him_her_it}!"]
        strength_bonus = 1
        if self.potion_of_strength_effect:
            strength_bonus = 1.33
        if self.quantum_strength_effect:
            strength_bonus = 2
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"You strike at the {monster.name}..")
        print(f"Melee Attack Roll: {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print(random.choice(one_roll))
            sleep(1)
            pause()
            self.hud()
            return 0
        if roll_d20 == 20 or \
                (roll_d20 + self.acumen + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus) \
                - monster.armor_class >= 10:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"

        else:
            critical_bonus = 1
            hit_statement = random.choice(hit_list)
        print(f"Dexterity modifier: {self.dexterity_modifier}\nAcumen: {self.acumen}")
        if self.wielded_weapon.to_hit_bonus > 0:
            print(f"Weapon to-hit bonus: {self.wielded_weapon.to_hit_bonus}")
        roll_total = roll_d20 + self.acumen + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus
        print(f"Your Total Attack Roll: {roll_total}")
        print(f"Monster armor class {monster.armor_class}")
        if roll_d20 == 20 or roll_d20 + self.acumen + \
                self.dexterity_modifier + self.wielded_weapon.to_hit_bonus >= monster.armor_class:
            damage_roll = dice_roll((self.level * critical_bonus), self.hit_dice)
            damage_to_opponent = math.ceil(
                (damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus) * strength_bonus)
            if damage_to_opponent > 0:
                print(hit_statement)
                sleep(1)
                print(f"{self.level * critical_bonus}d{self.hit_dice} Damage Roll: {damage_roll}\n"
                      f"Strength modifier: {self.strength_modifier}")
                if self.wielded_weapon.damage_bonus > 0:
                    print(f"Weapon bonus: {self.wielded_weapon.damage_bonus}")
                if strength_bonus > 1:
                    print(f"x Strength Bonus Multiplier: {strength_bonus}")
                print(f"Your Damage Total: {damage_to_opponent}")
                print(f"You inflict {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"Your attack is barely effective. You manage 1 point of damage.")  # zero damage result
                sleep(1)
                return 1
        elif self.extra_attack:  # self.level > 4
            print(random.choice(miss_list))
            # print("You missed..")
            sleep(1)
            print("Extra chance to hit!")
            sleep(1)
            roll_d20 = dice_roll(1, 20)
            if roll_d20 == 20 or roll_d20 + self.acumen + self.dexterity_modifier + \
                    self.wielded_weapon.to_hit_bonus >= monster.armor_class:
                damage_roll = dice_roll(self.level, self.hit_dice)
                damage_to_opponent = \
                    math.ceil((damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus)
                              * strength_bonus)
                print(random.choice(hit_list))
                print(f"You inflict {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(random.choice(miss_list))
                # print("You miss again..")
                pause()
                self.hud()
                return 0
        else:
            print(random.choice(miss_list))
            # print(f"You missed...")
            pause()
            self.hud()
            return 0

    def npc_melee(self, ally, monster_name, monster_armor_class):
        # called from npc_attack_logic() for npcs who use melee
        pronoun = 'his'
        if ally.name == "Si'Kira":
            pronoun = 'her'
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"{ally.name} strikes at the {monster_name} with {pronoun} {ally.wielded_weapon.name}..")
        print(f"Attack Roll: {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print(f"{ally.name} misses..")
            pause()
            self.hud()
            return 0
        if roll_d20 == 20 or (roll_d20 + self.acumen + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus) \
                - monster_armor_class >= 10:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = f"{ally.name} HITS!"
        print(f"Dexterity modifier: {ally.dexterity_modifier}\nAcumen: {ally.acumen}")
        if ally.wielded_weapon.to_hit_bonus > 0:
            print(f"Weapon to-hit bonus {ally.wielded_weapon.to_hit_bonus}")
        roll_total = roll_d20 + ally.acumen + ally.dexterity_modifier + ally.wielded_weapon.to_hit_bonus
        print(f"{ally.name} Total Attack Roll: {roll_total}")
        print(f"Monster armor class {monster_armor_class}")
        if roll_d20 == 20 or roll_d20 + ally.acumen + \
                ally.dexterity_modifier + ally.wielded_weapon.to_hit_bonus >= monster_armor_class:
            damage_roll = dice_roll((ally.level * critical_bonus), ally.hit_dice)
            damage_to_opponent = math.ceil((damage_roll + ally.strength_modifier + ally.wielded_weapon.damage_bonus)
                                           * ally.strength_bonus)
            if damage_to_opponent > 0:
                print(hit_statement)
                sleep(1)
                print(f"{ally.level * critical_bonus}d{ally.hit_dice} Damage Roll: {damage_roll}\n"
                      f"Strength modifier: {ally.strength_modifier}")
                if ally.wielded_weapon.damage_bonus > 0:
                    print(f"Weapon bonus: {ally.wielded_weapon.damage_bonus}")
                if ally.strength_bonus > 1:
                    print(f"x Strength Bonus Multiplier: {ally.strength_bonus}")
                print(f"{ally.name} Total Damage: {damage_to_opponent}")
                print(f"{ally.name} does {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"{ally.name}'s attack is barely effective. It does 1 point of damage.")  # zero damage result
                sleep(1)
                return 1
        elif ally.level > 4:
            print(f"{ally.name} missed..")
            sleep(2)
            print("Extra Attack Skill chance to hit!")
            sleep(2)
            roll_d20 = dice_roll(1, 20)
            if roll_d20 == 20 or roll_d20 + ally.acumen + ally.dexterity_modifier + \
                    ally.wielded_weapon.to_hit_bonus >= monster_armor_class:
                damage_roll = dice_roll(ally.level, ally.hit_dice)
                damage_to_opponent = \
                    math.ceil((damage_roll + ally.strength_modifier + ally.wielded_weapon.damage_bonus)
                              * ally.strength_bonus)
                print(f"{ally.name} attacks again for {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"{ally.name} misses again.")
                pause()
                self.hud()
                return 0
        else:
            print(f"{ally.name} missed...")
            pause()
            self.hud()
            return 0

    def turn_undead(self, monster):
        # monster must make wisdom protection roll or be turned away
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            print(f"Turn Undead")
            sleep(1)
            self.hud()
            if "Turn Undead" not in monster.immunities and "All" not in monster.immunities and monster.undead:
                vulnerability_modifier = 0
                if "Turn Undead" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Turn Undead" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + \
                    self.wisdom_modifier + vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Protection Roll: {monster_roll}")
                # monster_mod = math.floor((monster.wisdom - 10) / 2)
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc > monster_total:  # with >= tie goes to player... with > tie goes to monster
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    # print(f"The {monster.name} runs in fear!!")
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} runs in fear!!")
                    else:
                        print(f"The {monster.name} runs in fear!!")
                    sleep(1.5)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} listens with deaf ears..")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Turn Undead!!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Turn Undead!!")
                        sleep(1)
                else:
                    print(f"Turn Undead is only effective against undead creatures!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Turn Undead is a Battle Effect only!")
            sleep(1)
            return

    def banish(self, monster):
        # monster must make a successful charisma protection roll or be banished from existence on this plane
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            print(f"Banish")
            sleep(1)
            self.hud()
            if "Banish" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Banish" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Banish" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Protection Roll: {monster_roll}")
                monster_charisma_modifier = math.floor((monster.charisma - 10) / 2)
                print(f"{monster.name} Charisma Modifier: {monster_charisma_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster_charisma_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.hud()
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    print(f"BE GONE!!")
                    sleep(1)
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} phases out of existence on this plane!!")
                    else:
                        print(f"The {monster.name} phases out of existence on this plane!!!!")
                    sleep(1)
                    print(f"You perceive a slight breeze as the air "
                          f"around you collapses into the brief void left behind..")
                    sleep(2)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is unfazed by your attempts!!")
                    else:
                        print(f"The {monster.name} is unfazed by your attempts!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Banish!!")
                else:
                    print(f"The {monster.name} is immune to Banish!!")
                sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Banish is a Battle Effect only!")
            sleep(1)
            return

    def fear(self, monster):
        # player wisdom vs monster wisdom. only works on living
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            print(f"Fear.")
            sleep(1)
            self.hud()
            if "Fear" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Fear" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Fear" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Protection Roll: {monster_roll}")
                # monster_mod = math.floor((monster.wisdom - 10) / 2)
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:  # with >= tie goes to player... with > tie goes to monster
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} runs in fear!!")
                    else:
                        print(f"The {monster.name} runs in fear!!")
                    sleep(1.5)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} ignores your wiles!!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if not monster.undead:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Fear!!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Fear!!")
                        sleep(1)
                else:
                    print(f"Fear is only effective against the living!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Turn Undead is a Battle Effect only!")
            sleep(1)
            return

    def quantum_purify(self, monster):
        # cures poisoned and necrotic condition
        # works only when poisoned or necrotic, but once engaged, also has powerful hit point healing!
        if monster is None:
            print(f"Purify")
        else:
            print(f"Purify (BATTLE)")
        sleep(1)
        quantum_unit_cost = 2
        self.hud()
        if not self.poisoned and not self.necrotic:
            print(f"Your flesh is not corrupted!")
            sleep(1)
            return 0
        else:
            print(f"You quiet your mind and grasp at the elusive Quantum Knowledge...")
            sleep(1)
            self.quantum_units -= quantum_unit_cost
            self.hud()
            print(f"You feel a cleansing of the flesh..")
            sleep(1)
            self.poisoned = False
            self.poisoned_turns = 0
            self.necrotic = False
            self.necrotic_turns = 0
            print(f"The foul corruption leaves your body..")
            sleep(1)
            if self.hit_points < self.maximum_hit_points:
                # number_of_dice = (3 + self.level)  # consider changing to self.quantum_level
                # heal = dice_roll(number_of_dice, 4) + number_of_dice + self.quantum_level
                if self.quantum_level < 3:
                    heal = math.ceil(self.maximum_hit_points * .66)
                else:
                    heal = math.ceil(self.maximum_hit_points * .75)
                print(f"You heal {heal} hit points")  # remove after testing
                self.hit_points += heal
                if self.hit_points > self.maximum_hit_points:
                    self.hit_points = self.maximum_hit_points
                # self.hud()
                print(f"Your wounds feel better!")
                sleep(1)
            pause()
            return 0

    def quantum_petrifaction(self, monster):
        # like sleep and charm, but always successful.
        # player has 1 free crit, thereafter monster must pass Constitution protection roll
        # 2 failed rolls after initial attack = permanent petrifaction for monster.
        # player gets exp reward, but no gold or loot
        quantum_unit_cost = 4
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            print(f"Quantum Petrifaction")
            sleep(1)
            self.hud()
            if "Petrifaction" not in monster.immunities and "All" not in monster.immunities:
                self.quantum_units -= quantum_unit_cost
                if "Petrifaction" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Petrifaction" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                print(f"Before {monster.he_she_it} even realizes what is happening, {monster.his_her_its} "
                      f"flesh ripples into a stone replica of {monster.his_her_its} normal state!")
                sleep(1)
                input(f"Press (ENTER) to attack: ")
                self.hud()
                print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                sleep(1.5)
                damage_modifier = 2
                if "Quantum Petrifaction" in monster.vulnerabilities:
                    damage_modifier = 3
                # if "Quantum Petrifaction" in monster.resistances or "All" in monster.resistances:
                #    damage_modifier = 1
                total_fails = 0
                while True:
                    self.hud()
                    damage_to_monster = dice_roll((self.level * damage_modifier), self.hit_dice)
                    total_fails += 1
                    print(f"You inflict {damage_to_monster} hit points!")
                    pause()
                    self.hud()
                    monster.reduce_health(damage_to_monster)
                    if not monster.check_dead():
                        level_advantage = 0
                        if self.level > monster.level:
                            level_advantage = self.level - monster.level
                        player_dc = self.base_dc + self.acumen + \
                            self.wisdom_modifier + vulnerability_modifier + level_advantage
                        print(f"Player base DC = {self.base_dc}\n"
                              f"Wisdom Modifier: {self.wisdom_modifier}\n"
                              f"Acumen: {self.acumen}")
                        if vulnerability_modifier != 0:
                            print(f"+ Monster Vulnerability Modifier: {vulnerability_modifier}")
                        if level_advantage > 0:
                            print(f"+ Level Advantage: {level_advantage}")
                        sleep(1)
                        print(f"DC Total: {player_dc}")
                        sleep(1)
                        monster_saving_throw = dice_roll(1, 20)
                        monster_total = monster_saving_throw + monster.constitution_modifier + resistance_modifier
                        print(f"Monster Protection Roll: {monster_saving_throw}")
                        sleep(1)
                        print(f"Monster Constitution Modifier: {monster.constitution_modifier}")
                        if resistance_modifier != 0:
                            print(f"Monster Resistance Modifier: {resistance_modifier}")
                        sleep(1)
                        print(f"Total: {monster_total}")
                        sleep(1)

                        if monster_total >= player_dc:  # dnd
                            print(f"The {monster.name} is restored!")
                            pause()
                            return 0  # no damage sent back because already sent to monster.reduce_health()
                        else:
                            if total_fails == 3:
                                print(f"The {monster.name} forever succumbs to the petrification of stone!")
                                sleep(1)
                                print(f"You are victorious!")
                                sleep(1)
                                self.in_proximity_to_monster = False  # monster is gone. no loot.
                                monster.gold = 0  # gold has been turned to stone
                                return 0
                            else:
                                print(f"It remains stone-petrified!")
                                sleep(1)
                                print(f"You attack again!")
                                sleep(1.5)
                                continue
                    else:
                        print(f"You have vanquished the {monster.name}!")
                        sleep(1)
                        monster.gold = 0  # gold has been turned to stone
                        self.in_proximity_to_monster = False  # monster is stone, no loot.
                        return 0  # no damage sent to main
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Quantum Petrifaction Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Quantum Petrifaction Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Petrifaction is a Battle Effect only!")
            sleep(1)
            return

    def gravity_well(self, monster):
        # like sleep and charm, but always successful.
        # initial damage is rolled and then player has 1 free crit,
        # thereafter monster must pass strength protection roll.
        # player gets exp reward, but no gold or loot
        quantum_unit_cost = 5
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            print(f"Gravity Well")
            sleep(1)
            self.hud()
            if "Gravity Well" not in monster.immunities and "All" not in monster.immunities:
                self.quantum_units -= quantum_unit_cost
                if "Gravity Well" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen

                print(f"Focusing the Quantum Weirdness on the ground beneath the {monster.name}, "
                      f"a growing void of crushing gravity opens between worlds!!")
                sleep(1)
                print(f"It is pulled in by the insatiable force!")
                sleep(1)
                initial_damage = dice_roll(10, 10)
                print(f"The aberrant void inflicts {initial_damage} hit points!")
                sleep(1.5)
                pause()
                monster.reduce_health(initial_damage)
                if not monster.check_dead():
                    damage_modifier = 3
                    if "Gravity Well" in monster.vulnerabilities:
                        damage_modifier = 4
                    if "Gravity Well" in monster.resistances or "All" in monster.resistances:
                        damage_modifier = 1
                    # total_fails = 0
                    while True:
                        self.hud()
                        print(f"The {monster.name} remains trapped in the gravity well!")
                        sleep(1)
                        input(f"Press (ENTER) to attack: ")
                        self.hud()
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        damage_to_monster = dice_roll((self.level * damage_modifier), self.hit_dice)
                        # total_fails += 1
                        print(f"You inflict {damage_to_monster} hit points!")
                        sleep(1.5)
                        self.hud()
                        monster.reduce_health(damage_to_monster)
                        if not monster.check_dead():
                            level_advantage = 0
                            if self.level > monster.level:
                                level_advantage = self.level - monster.level
                            player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                                vulnerability_modifier + level_advantage
                            print(f"Player base DC = {self.base_dc}\n"
                                  f"Wisdom Modifier: {self.wisdom_modifier}\n"
                                  f"Acumen: {self.acumen}")
                            if vulnerability_modifier != 0:
                                print(f"+ Monster Vulnerability Modifier: {vulnerability_modifier}")
                            if level_advantage > 0:
                                print(f"+ Level Advantage: {level_advantage}")
                            sleep(1)
                            print(f"DC Total: {player_dc}")
                            sleep(1)
                            monster_saving_throw = dice_roll(1, 20)
                            monster_total = monster_saving_throw + monster.strength_modifier
                            print(f"Monster Protection Roll: {monster_saving_throw}")
                            sleep(1)
                            print(f"Monster Strength Modifier: {monster.strength_modifier}")
                            sleep(1)
                            print(f"Total: {monster_total}")
                            sleep(1)

                            if monster_total >= player_dc:  # dnd
                                print(f"The {monster.name} breaks out of the gravitational hold!")
                                pause()
                                return 0  # no damage sent back because already sent to monster.reduce_health()
                            else:
                                print(f"It attempts to break free!")
                                sleep(1)
                                print(f"It is pulled back in!")
                                sleep(1.5)
                                continue

                        else:
                            print(f"You have vanquished the {monster.name}!")
                            sleep(1)
                            monster.gold = 0  # gold has been lost to the void
                            self.in_proximity_to_monster = False  # monster is gone, no loot.
                            return 0  # no damage sent to main

                else:
                    print(f"You have vanquished the {monster.name}!")
                    sleep(1)
                    monster.gold = 0  # gold has been lost to the void
                    self.in_proximity_to_monster = False  # monster is gone, no loot.
                    return 0  # no damage sent to main
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Gravity Well Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Gravity Well Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Gravity Well is a Battle Effect only!")
            sleep(1)
            return

    def hold_monster(self, monster):
        # like sleep and charm, but pits player wisdom against monster strength
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            print(f"Hold Monster")
            sleep(1)
            self.hud()
            if "Hold Monster" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Hold Monster" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Hold Monster" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                # turn_roll = dice_roll(1, 20)
                # player_total = (turn_roll + self.wisdom_modifier + self.acumen + vulnerability_modifier)
                # The difficulty class ("DC") of the Protection Roll should be based on the quantum manipulator:
                # 8 + acumen + casting ability modifier.
                # The GM rolls a d20 on behalf of the monster, adds the appropriate saving modifier based on
                # the monster's stats, and compares to the quantum manipulator's save DC.
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"{monster.name} Strength Modifier: {monster.strength_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.strength_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc > monster_total:
                    self.quantum_units -= quantum_unit_cost  # level 3 effect. uses 3 units
                    print(f"The {monster.name} is held fast by Quantum Forces!")
                    sleep(1)
                    input(f"Press (ENTER) to attack: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= difficulty_class:  #
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        #
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It has broken free!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} resists!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Hold Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Hold Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Hold Monster is a Battle Effect only!")
            sleep(1)
            return

    def quantum_web(self, monster):
        # web is a match of player's intuition as reflected by wisdom, vs the monster's ability to dodge
        # a web that is shooting toward it.
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            print(f"Web")
            sleep(1)
            self.hud()
            if "Web" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Web" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Web" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                # turn_roll = dice_roll(1, 20)
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + vulnerability_modifier)
                # print(f"Quantum Check: {turn_roll}")
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                sleep(1)
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Dexterity Protection Roll: {monster_roll}")
                print(f"{monster.name} Dexterity Modifier: {monster.dexterity_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.dexterity_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_total >= monster_total:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} is webbed..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    sleeping_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {sleeping_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll > sleeping_difficulty_class:  #
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        # pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It broke free!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} dodges!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Quantum Web Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Quantum Web Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Web is a Battle Effect only!")
            sleep(1)
            return

    def quantum_charm(self, monster):
        # Charm matches the player's Charisma vs the monster's wisdom;
        # your power of persuasion vs their perception
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            print(f"Charm")
            sleep(1)
            self.hud()
            if "Charm" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Charm" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Charm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                # turn_roll = dice_roll(1, 20)
                # total = (turn_roll + self.charisma_modifier + self.acumen + vulnerability_modifier)
                # print(f"Quantum Check: {turn_roll}\nCharisma Modifier: {self.charisma_modifier}\n"
                #      f"Acumen: {self.acumen}")
                if vulnerability_modifier > 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.charisma_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Charisma Modifier: {self.charisma_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is charmed..")
                    else:
                        print(f"The {monster.name} is charmed..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    charm_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {charm_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= charm_difficulty_class:
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        # pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It breaks free from your charm and comes to its senses!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is not persuaded by your charms!")
                    else:
                        print(f"The {monster.name} is not persuaded by your charms!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    print(f"The undead ignore your wiles!!")
                    sleep(1)
                else:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to being charmed!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to being charmed!")
                        sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Charm is a Battle Effect only!")
            sleep(1)
            return

    def quantum_sleep(self, monster):
        # sleep matches the player's intelligence vs the monster's wisdom;
        # your knowledge of quantum nature vs their perception
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            print(f"Sleep")
            sleep(1)
            self.hud()
            if "Sleep" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Sleep" in monster.vulnerabilities:
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Sleep" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                # turn_roll = dice_roll(1, 20)
                # total = (turn_roll + self.intelligence_modifier + self.acumen + vulnerability_modifier)
                # print(f"Quantum Check: {turn_roll}\nIntelligence Modifier: {self.intelligence_modifier}\n"
                #      f"Acumen: {self.acumen}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.intelligence_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Intelligence Modifier: {self.intelligence_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerability_modifier > 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Roll: {monster_roll}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"{monster.name} Wisdom modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is sleeping..")
                    else:
                        print(f"The {monster.name} is sleeping..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    sleeping_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {sleeping_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= sleeping_difficulty_class:
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It woke up!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} isn't sleepy!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    print(f"Undead do not sleep!!")
                    sleep(1)
                else:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Quantum Sleep!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Quantum Sleep!")
                        sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Sleep is a Battle Effect only!")
            sleep(1)
            return

    def quantum_strength(self, monster):
        # heal to full strength and get *2 melee damage multiplier (defined in melee())
        if monster is None:
            print(f"Quantum Strength")
        else:
            print(f"Quantum Strength (BATTLE)")
        sleep(1)
        self.hud()
        quantum_unit_cost = 2
        rndm_phrases = [
            "Drawing on all of your innate understanding, you draw out the Quantum Energies.",
            "Retrieving the memories of the effect, you calm yourself and harness the weird energies..",
            "Quietly retreating into the recesses of memory, you grasp at the weird energies.."
        ]
        phrase = random.choice(rndm_phrases)
        print(f"{phrase}")
        sleep(1)
        print(f"Great power courses through your body!")
        sleep(1)
        self.quantum_strength_effect = True
        self.quantum_units -= quantum_unit_cost
        self.quantum_strength_uses = -1  # to compensate for end of turn calculation
        if self.hit_points < self.maximum_hit_points:  # in the rare case player has hit point overage,
            self.hit_points = self.maximum_hit_points  # this will not disrupt that advantage
        pause()
        return 0

    def quantum_medicine(self, monster):
        if monster is None:
            print(f"Quantum Medicine")
        else:
            print(f"Quantum Medicine (BATTLE)")
        sleep(1)
        self.hud()
        # perhaps use this math for higher healing effect:
        # number_of_dice = (3 + self.level - 1)  # 3 dice for lvl 1, 4 for lvl 2, 5 for lvl 3....
        # heal = dice_roll(number_of_dice, 4)  + (1 * number_of_dice)
        quantum_unit_cost = 1
        # number_of_dice = (3 + self.level + self.quantum_level)  # consider changing to self.quantum_level
        # heal = dice_roll(number_of_dice, 6) + number_of_dice + self.quantum_level
        heal = math.ceil(self.maximum_hit_points * .75)

        if self.hit_points < self.maximum_hit_points:
            print(f"You feel restorative powers welling up within you..")
            sleep(1)
            print(f"You heal {heal} points..")  # remove after testing
            self.hit_points += heal
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points
            # self.hit_points += math.floor(self.maximum_hit_points * .5)  # round down for cure light wounds.
            self.quantum_units -= quantum_unit_cost
        else:
            print(f"You are at maximum health!")
            sleep(1)
        pause()
        return 0

    def quantum_medicine_enhanced_npc_subfunction(self, npc):
        # called from quantum_medicine_enhanced() for each npc ally, if wounded
        if npc.hit_points < npc.maximum_hit_points:
            self.hud()
            print(f"{self.name} procures Enhanced Quantum Medicine for {npc.name}.")
            sleep(1)
            print(f"{npc.name} feels restorative powers welling up within..")
            sleep(1)
            print(f"{npc.name} heals to full strength..")  # remove after testing
            npc.hit_points = npc.maximum_hit_points

            if npc.retreating:
                npc.retreating = False
                npc.retreat_counter = 0
                print(f"{npc.name} is no longer retreating")
                sleep(1)

            pause()

    def quantum_medicine_enhanced(self, monster):
        # level 3 effect. consider adjusting, depending on playthrough;
        # player should be able to use this by the time allies are encountered!
        if monster is None:
            print(f"Quantum Medicine, Enhanced")
        else:
            print(f"Quantum Medicine, Enhanced (BATTLE)")
        sleep(1)
        someone_has_been_healed = False
        if self.sikira_ally or self.torbron_ally or self.magnus_ally or self.vozzbozz_ally:
            if self.sikira_ally and self.sikira.hit_points < self.sikira.maximum_hit_points:
                self.quantum_medicine_enhanced_npc_subfunction(self.sikira)
                someone_has_been_healed = True
            if self.torbron_ally and self.torbron.hit_points < self.torbron.maximum_hit_points:
                self.quantum_medicine_enhanced_npc_subfunction(self.torbron)
                someone_has_been_healed = True
            if self.magnus_ally and self.magnus.hit_points < self.magnus.maximum_hit_points:
                self.quantum_medicine_enhanced_npc_subfunction(self.magnus)
                someone_has_been_healed = True
            if self.vozzbozz_ally and self.vozzbozz.hit_points < self.vozzbozz.maximum_hit_points:
                self.quantum_medicine_enhanced_npc_subfunction(self.vozzbozz)
                someone_has_been_healed = True

        self.hud()
        quantum_unit_cost = 3
        heal = math.ceil(self.maximum_hit_points * .90)
        if self.hit_points < self.maximum_hit_points:
            someone_has_been_healed = True
            print(f"You procure Enhanced Quantum Medicine.")
            sleep(1)
            print(f"You feel restorative powers welling up within you..")
            sleep(1)
            print(f"You heal {heal} points..")  # remove after testing
            self.hit_points += heal
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points

        if someone_has_been_healed:
            self.quantum_units -= quantum_unit_cost

        else:
            if self.sikira_ally or self.torbron_ally or self.magnus_ally or self.vozzbozz_ally:
                print("All in the party are at maximum health.")
            else:
                print(f"You are at maximum health.")
            sleep(1)
        pause()
        return 0

    def protection_from_evil(self, monster):
        # everything but a 1 roll will succeed
        if monster is None:
            print(f"Protection from Evil")
        else:
            print(f"Protection from Evil (BATTLE)")
        sleep(1)
        quantum_unit_cost = 1
        self.hud()
        rndm_phrases = [
            "Concentrating and calming yourself, you attempt to harness your innate Quantum Knowledge..",
            "Quieting your mind, you focus inward to harness the Quantum Energies..",
            "The world around you becomes muted and still as you introspectively draw upon your innate Quantum Skill.."
        ]
        effect_phrase = random.choice(rndm_phrases)
        prot_roll = dice_roll(1, 20)
        print(f"{effect_phrase}")
        sleep(1.5)
        if prot_roll > 1:
            self.protection_effect = True
            self.protection_effect_uses = -1  # to compensate for end of turn calculation
            self.protection_effect_value = (1 + self.acumen)
            self.quantum_units -= quantum_unit_cost
            print(f"You have succeeded!")
            sleep(1)
            print(f"You gain a Quantum Protection advantage + {self.protection_effect_value}!")
            pause()
            return 0
        else:
            print(f"You are unable to glean the Quantum Effects..")
            self.quantum_units -= quantum_unit_cost
            pause()
            return 0

    def quantum_help1(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Quantum Missile: Multiple glowing projectiles, corresponding to your Quantum Knowledge and randomness"
              f"\nare derived from other realities and launched at your enemy. "
              f"Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Quantum Sleep: Your knowledge of Quantum Weirdness allows you to attempt to lull your enemy into a\n"
              f"dream-like and utterly vulnerable state. Initial success based on Player Intelligence vs Enemy Wisdom\n"
              f"Final success depends on Enemy AC.")
        print()
        print(f"Quantum Medicine: Quantum Actions at a subatomic level repair physical wounds, ignoring necrosis and "
              f"poison.\nEffectiveness equal to 75% of maximum hit points.")
        print()
        print(f"Protection from Evil: Through Quantum Probabilities, reduce the chances of successful enemy Quantum\n"
              f"attacks and paralyzing effects. Effectiveness depends on Quantum Knowledge Level. Duration depends on\n"
              f"player Constitution.")
        print()
        print(f"Turn Undead: Attempt to strike panic into the Undead by turning the very improbable forces responsible"
              f"\nfor their weird existence against them. Success based on Player Wisdom vs Enemy Wisdom")
        print()
        pause()
        return None

    def quantum_help2(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Web: Through improbabilities, shoot a giant web at your enemy, incapacitating them. Initial success\n"
              f"based on Player Wisdom vs Enemy Dexterity. Final success depends on Enemy AC.")
        print()
        print(f"Quantum Purify: Works only when poisoned or necrotic, but once engaged, Quantum Weirdness at the "
              f"molecular level purifies the flesh from these\n"
              f"effects and also increases Hit Points.")
        print()
        print(f"Quantum Strength: Harnessing Quantum Energies, your Strength and melee damage are increased\n"
              f"for a maximum duration based on your Quantum Knowledge level and Strength Modifier.")
        print()
        print(f"Quantum Blaze: Rays of intense flame strike your enemy. Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Quantum Charm: Use your powers of persuasion to lull your enemy into a vulnerable sleep. Initial\n"
              f"success based on Player Charisma vs Enemy Wisdom. Final success depends on Enemy AC.")
        print()
        pause()
        return None

    def quantum_help3(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Lightning: Harness an electrical storm to be cast at your enemy, causing burns and arcflash damage.\n"
              f"Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Hold Monster: Employ Quantum Forces to hold and incapacitate your enemy. Success based on \n"
              f"Player Wisdom vs Enemy Strength. Final success depends on Enemy AC.")
        print()
        print(f"Phantasm: By Quantum Tunneling, create a terrifyingly debilitating mental illusion, capturing the\n"
              f"mind of your enemy and causing agonizing mental damage. Success based on Player Wisdom vs Enemy\n"
              f"Intelligence. (Undead are unbelieving.)")
        print()
        print(f"Immolation: A winding trail of flame encircles your enemy, closing until forming a complete immersion\n"
              f"of deadly fire. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Vortex: A watery twister forms around your enemy, disorienting, and causing crushing damage.\n"
              f"Success based on Player Wisdom vs Enemy Strength.")
        print()
        print(f"Quantum Medicine, Enhanced: Quantum Actions at a subatomic level repair physical wounds, ignoring "
              f"necrosis and poison.\n"
              f"Effectiveness equal to 90% of maximum hit points. In addition, heals any and all allies to "
              f"full strength.\nIf procured during battle, healed allies no longer retreat, and immediately re-enter "
              f"the fight.")
        pause()
        return None

    def quantum_help4(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Quantum Firewall: Through Spooky Action at a Distance, a wall of fire forms, seemingly from out of "
              f"your hands,\n"
              f"looming toward your enemy at great speed. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Quantum Petrifaction: 100% chance to petrify monster, after which, player has 1 free crit, "
              f"thereafter, enemy\n"
              f"must pass Constitution protection roll. 2 failed rolls after initial attack = permanent "
              f"petrification.\n"
              f"Player gets exp reward, but no gold or loot.")
        print()
        print(f"Fear: Strike terror into the hearts of the living with Quantum Weirdness, sending them retreating.\n"
              f"Success based on Player Wisdom vs Enemy Wisdom. (Undead are unbelieving)")
        print()
        print(f"Finger of Death: Concentrating powerful Quantum Energies into a single finger, great pain and high\n"
              f"damage befall any enemy touched. Success based on Player Wisdom vs Enemy Constitution.")
        print()
        print(f"Banish: At the will of the Manipulator, a Quantum Tunnel between worlds claims the enemy's existence,\n"
              f"transferring it offworld. Success based on Player Wisdom vs Enemy Charisma.")
        print()
        pause()
        return None

    def quantum_help5(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Disentangle: Quantum Energy shoots from your hands toward your enemy.\n"
              f"On a failed roll, the enemy takes massive damage. All Quantum Particles within the enemy, across\n"
              f"all realities are disentangled, if hit points reach 0. A disentangled enemy and its entire\n"
              f"inventory, are gone forever; In fact, they never existed. Player receives experience\n"
              f"reward but no Gold or Loot. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Ice Storm: A Quantum squall of frozen death hurls toward your enemy causing overwhelming cold and\n"
              f"force damage. Success based on Player Wisdom vs Enemy Constitution.")
        print()
        print(f"Firestorm: Ice Storm's counterpart, encompassed of seething flame, causing high burn damage.\n"
              f"Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Gravity Well: 100% chance to successfully incapacitate your enemy in an impossible Quantum Gravity\n"
              f"Singularity which causes initial crushing damage. Player has 1 free crit. Target must make successful "
              f"strength\n"
              f"protection roll. Upon failed save, enemy remains trapped and player gets additional free crit.\n"
              f"Enemy and all items are lost to the crushing gravity. Player gets exp reward, but no gold or loot\n"
              f"unless enemy item is protected by Quantum Weirdness.")
        print()
        pause()
        return None

    def quantum_help6(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"QUANTUM MASTER EFFECTS:")
        print()
        print(f"Quantum Spoken Word: Through impossibly, unimaginably small probabilities, the Master utters a single\n"
              f"word. If the enemy has less than 125 Hit Points, death results instantly. No protection roll,\n"
              f"no defense possible.")
        print()
        print(f"Quantum Mooncrusher: The Quantum Master rends otherworldly, crushed moon matter into existence and,\n"
              f"with amplified and compensatory gravity, propels it upon an enemy for a devastating attack yielding\n"
              f"extremely high force and crushing damage. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Skeletal Remains: The Master pulls finite Quantum Energies from the ground, impossibly re-animating\n"
              f"fallen skeletal warriors lost to time and sending them forth as a stampeding army, resulting in\n"
              f"extreme force, bludgeoning, and melee damage. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Negative Energy Plague: The Quantum Master harnesses Dark Energy and re-focuses it to form a\n"
              f"plague of mental agony causing severe damage to all creatures- living and undead. Success based on\n"
              f"Player Wisdom vs Enemy Intelligence.")
        print()
        pause()
        return None

    def quantum_effects(self, monster):
        # called from main loop
        if self.quantum_units > 0:
            printable_quantum_book = {1: {1: "Quantum Missile",
                                          2: "Sleep",
                                          3: "Quantum Medicine",
                                          4: "Protection from Evil",
                                          5: "Turn Undead"},
                                      2: {1: "Web",
                                          2: "Purify",
                                          3: "Quantum Strength",
                                          4: "Scorch",
                                          5: "Charm"},
                                      3: {1: "Lightning",
                                          2: "Hold Monster",
                                          3: "Phantasm",
                                          4: "Immolation",
                                          5: "Vortex",
                                          6: "Quantum Medicine, Enhanced"},
                                      4: {1: "Firewall",
                                          2: "Quantum Petrifaction",
                                          3: "Fear",
                                          4: "Finger of Death",
                                          5: "Banish"},
                                      5: {1: "Quantum Disentangle",
                                          2: "Ice Storm",
                                          3: "Firestorm",
                                          4: "Gravity Well"},
                                      6: {1: "Quantum Spoken Word",
                                          2: "Quantum Mooncrusher",
                                          3: "Skeletal Remains",
                                          4: "Negative Energy Plague"}

                                      }
            quantum_book = {1: {0: self.quantum_help1,
                                1: self.quantum_missile,
                                2: self.quantum_sleep,
                                3: self.quantum_medicine,
                                4: self.protection_from_evil,
                                5: self.turn_undead},
                            2: {0: self.quantum_help2,
                                1: self.quantum_web,
                                2: self.quantum_purify,
                                3: self.quantum_strength,
                                4: self.quantum_blaze,
                                5: self.quantum_charm},
                            3: {0: self.quantum_help3,
                                1: self.quantum_lightning,
                                2: self.hold_monster,
                                3: self.phantasm,
                                4: self.immolation,
                                5: self.vortex,
                                6: self.quantum_medicine_enhanced},
                            4: {0: self.quantum_help4,
                                1: self.firewall,
                                2: self.quantum_petrifaction,
                                3: self.fear,
                                4: self.finger_of_death,
                                5: self.banish},
                            5: {0: self.quantum_help5,
                                1: self.quantum_disentangle,
                                2: self.ice_storm,
                                3: self.fire_storm,
                                4: self.gravity_well},
                            6: {0: self.quantum_help6,
                                1: self.quantum_spoken_word,
                                2: self.moon_crusher,
                                3: self.skeletal_remains,
                                4: self.negative_energy_plague}
                            }
            while True:
                self.hud()
                try:
                    print(f"Your Quantum Knowledge level: {self.quantum_level}")
                    q_level = int(input(f"Quantum Level to cast: "))

                    if self.quantum_level >= q_level and self.quantum_units >= q_level:
                        # create key and value lists from nested dict in order to produce cleanly printable dictionary
                        key_lst = list(printable_quantum_book[q_level].keys())
                        value_list = list(printable_quantum_book[q_level].values())
                        working_dict = {key_lst[i]: value_list[i] for i in range(len(key_lst))}
                        for key, value in working_dict.items():
                            print(f"{key}: {value}")
                        q_to_cast = int(input(f"Number of Quantum Effect to cast (or 0 for HELP): "))

                        # quantum_function = quantum_book[q_level][q_to_cast]  # (monster)  # beta removed (monster)
                        # and added to function calls below:
                        if q_to_cast == 0:  # if HELP, call function, which will return here and loop continues
                            # noinspection PyArgumentList
                            quantum_book[q_level][q_to_cast](monster)
                            # pycharm is unhappy calling this method through a reference to the method buried in a dict
                            # quantum_function(monster)  # beta used to be simply quantum_function

                        else:  # if not HELP, return the damage from function to the main loop
                            # noinspection PyArgumentList
                            return quantum_book[q_level][q_to_cast](monster)
                            # return quantum_function(monster)

                    else:
                        if self.quantum_level < q_level:
                            print(f"You have not yet acquired that level of Quantum knowledge!")
                            sleep(1)
                            continue

                        if self.quantum_units < q_level:
                            print(f"You do not have enough Quantum Energy Units!")
                            sleep(1)
                            continue

                except (ValueError, KeyError):
                    print(f"Invalid input")
                    sleep(.25)
                    return None  # creates condition for a continue statement in main loop so a turn is not wasted
        else:
            print(f"You have no Quantum unit energy!")
            pause()
            return None  # creates condition for a continue statement in main loop so a turn is not wasted

    def vozzbozz_moon_crusher(self, monster):
        player_total = self.vozzbozz.base_dc + self.vozzbozz.wisdom_modifier + self.vozzbozz.acumen
        print(f"Vozzbozz base DC: {self.vozzbozz.base_dc}")
        print(f"Wisdom modifier: {self.vozzbozz.wisdom_modifier}")
        print(f"Acumen: {self.vozzbozz.acumen}")
        print(f"Total: {player_total}")
        sleep(1)
        monster_roll = dice_roll(1, 20)
        monster_mod = monster.dexterity_modifier
        monster_total = monster_roll + monster_mod
        print(f"Monster Protection Roll: {monster_roll}")
        print(f"Monster Dexterity Modifier: {monster_mod}")
        print(f"Monster Total: {monster_total}")
        if player_total >= monster_total:
            critical_bonus = 1
            if dice_roll(1, 20) == 20:
                critical_bonus = 2
            number_of_dice = 20 * critical_bonus
            quantum_hit_die = 6
            damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # 2nd attack=force damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)

            print(f"Vozzbozz closes his eyes for a moment.")
            sleep(1)
            print(f"Upon opening them, they burn brighter than the sun!")
            pause()
            self.hud()
            print(f"With a world-shaking and awe-inspiring eruption, "
                  f"a sky-filling blanket of flaming moon-matter materializes above and falls upon your enemy!!")
            print(f"{number_of_dice}d{quantum_hit_die} + {number_of_dice}d{quantum_hit_die} force damage + "
                  f"1 per die rolled: "
                  f"{damage_to_opponent}")
            print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"The great storm of fire and stone explodes directly on target in surreal "
                  f"glory and inflicts {total_damage_to_opponent} points of damage!")
            pause()
            self.hud()
            return total_damage_to_opponent
        else:
            critical_bonus = 1
            if dice_roll(1, 20) == 20:
                critical_bonus = 2
            number_of_dice = 20 * critical_bonus
            damage_to_opponent = (dice_roll(number_of_dice, 6) + (1 * number_of_dice) +
                                  dice_roll(number_of_dice, 6) + (1 * number_of_dice)) / 2  # 2nd attack=force damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz closes his eyes for a moment.")
                sleep(1)
                print(f"His focus is momentarily disrupted by the {monster.name}!")
                pause()
                self.hud()
                print(f"Other-worldly moon matter materializes above and falls upon your enemy..")
                print(f"{number_of_dice}d8 + {number_of_dice}d8 force damage + 1 per die rolled: "
                      f"{damage_to_opponent}")
                print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                print(f"The great storm of fire and stone explodes directly on target in surreal "
                      f"glory, but due to the interruption, it only inflicts {total_damage_to_opponent} points\n"
                      f"of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent

    def vozzbozz_word_kill(self, monster):
        # if monster < 125 hp, it dies
        print(f"Vozzbozz smiles for an instant, then his face is drained of its humanity..")
        sleep(1)
        self.hud()
        if monster.hit_points < 125:
            print(f"He cries out in a world-shaking voice..")
            sleep(1)
            print(f"SUPPLICIUM!!")
            sleep(1.5)
            print(f"The {monster.name} drops like a rock!!!")
            pause()
            return monster.hit_points
        else:
            print(f"The {monster.name} has too much life energy to succumb to the Quantum Spoken Word effect!")
            pause()
            return 0

    def vozzbozz_skeletal_remains(self, monster):
        print(f"Vozzbozz Base DC: {self.vozzbozz.base_dc}")
        print(f"Wisdom modifier: {self.vozzbozz.wisdom_modifier}")
        print(f"Acumen: {self.vozzbozz.acumen}")
        player_total = self.vozzbozz.base_dc + self.vozzbozz.wisdom_modifier + self.vozzbozz.acumen
        print(f"Total: {player_total}")
        critical_bonus = 1
        if dice_roll(1, 20) == 20:
            critical_bonus = 2
        monster_roll = dice_roll(1, 20)
        monster_mod = monster.constitution_modifier
        monster_total = monster_roll + monster_mod
        print(f"Monster Protection Roll: {monster_roll}")
        print(f"Monster Constitution Modifier: {monster_mod}")
        print(f"Monster Total: {monster_total}")
        if player_total >= monster_total:
            #
            number_of_dice = 15 * critical_bonus
            quantum_hit_die = 12
            force_dmg_hit_die = 8
            damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, force_dmg_hit_die) + (1 * number_of_dice)  # 2nd attack = force damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz forms a fist and then beckons the ground with his free hand..")
                sleep(1)
                print(f"Without warning, the ground swells with the thundering cacophony of countless skeletal\n"
                      f"warriors arising from an abysmal black chasm!!")
                sleep(1)
                print(f"Some upon skeletal horseback, others on foot, but with one mind and purpose, they swarm upon\n"
                      f"your enemy, thrusting ever forward in a voracious clashing of bone, steel and shield!!")
                pause()
                self.hud()
                print(f"{number_of_dice}d{quantum_hit_die} + {number_of_dice}d{force_dmg_hit_die} force damage "
                      f"+ 1 per skeleton bludgeoning damage: {damage_to_opponent}")
                print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                # print(f"It hits for {total_damage_to_opponent} points of damage..")
                print(f"The great swarm of armor, axe, sword and spear inflicts "
                      f"{total_damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent
            else:
                print(f"For all of its fear-inspiring appearance, the skeletal horde"
                      f" fails to land any damage!")  # 0 damage
                sleep(1)
                return 0
        else:
            number_of_dice = 15 * critical_bonus
            quantum_hit_die = 12
            damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # no force damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
            print(f"Vozzbozz forms a fist and then beckons the ground with his free hand..")
            sleep(1)
            print(f"Without warning, the ground swells with the thundering cacophony of countless skeletal\n"
                  f"warriors arising from an abysmal black chasm!!")
            sleep(1)
            print(f"The {monster.name} distracts the Master for a moment..")
            pause()
            self.hud()
            print(f"The skeletal horde takes form but does not inflict damage to its fullest potential..")
            sleep(1)
            print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per skeleton bludgeoning damage = {damage_to_opponent}")
            print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"It hits for {total_damage_to_opponent} points of damage..")
            pause()
            self.hud()
            return total_damage_to_opponent

    def vozzbozz_negative_energy_plague(self, monster):
        print(f"Vozzbozz Base DC: {self.vozzbozz.base_dc}")
        print(f"Wisdom modifier: {self.vozzbozz.wisdom_modifier}")
        print(f"Acumen: {self.vozzbozz.acumen}")
        player_total = self.vozzbozz.base_dc + self.vozzbozz.wisdom_modifier + self.vozzbozz.acumen
        print(f"Total: {player_total}")
        sleep(1)
        monster_roll = dice_roll(1, 20)
        monster_mod = round((monster.intelligence - 10) / 2)
        monster_total = monster_roll + monster_mod
        print(f"Monster Protection Roll: {monster_roll}")
        print(f"Monster Intelligence Modifier: {monster_mod}")

        print(f"Monster Total: {monster_total}")
        critical_bonus = 1
        if dice_roll(1, 20) == 20:
            critical_bonus = 2
        if player_total >= monster_total:
            #
            number_of_dice = 15 * critical_bonus
            quantum_hit_die = 12
            crushing_die = 8
            damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, crushing_die) + (1 * number_of_dice)  # 2nd attack = crushing damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz grasps at the air, until his entire shape fades to a mere black silhouette\n"
                      f"of stars and celestial bodies floating through!!")
                sleep(1)
                print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                      f"from his hands toward your enemy!!")
                sleep(1)
                print(f"With universal abhorrence, the negative energy plague entangles the {monster.name}!!")
                sleep(1)
                print(f"{number_of_dice}d{quantum_hit_die} necrotic damage + {number_of_dice}d{crushing_die} "
                      f"crushing damage + 1 per die rolled mental anguish: {damage_to_opponent}")
                print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                print(f"The great, empty darkness inflicts "
                      f"{total_damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent
            else:
                print(f"For all of its fear-inspiring appearance, the plague"
                      f" fails to land any damage!")  # 0 damage
                sleep(1)
                return 0
        else:
            number_of_dice = 15 * critical_bonus
            quantum_hit_die = 12
            damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # no crushing damage
            melee_bonus = dice_roll(self.vozzbozz.acumen, self.vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
            print(f"Vozzbozz grasps at the air, until his entire shape fades to a mere silhouette of blackness, with\n"
                  f"stars and celestial bodies floating through!!")
            sleep(1)
            print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                  f"from his hands toward your enemy!!")
            sleep(1)
            print(f"The {monster.name} distracts Vozzbozz for just a moment..")
            pause()
            self.hud()
            print(f"The plague takes form but does not inflict damage to its fullest potential..")
            sleep(1)
            print(
                f"{number_of_dice}d{quantum_hit_die} necrotic damage + 1 per die rolled mental damage: "
                f"{damage_to_opponent}")
            print(f"{self.vozzbozz.acumen}d{self.vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"It hits for {total_damage_to_opponent} points of damage..")
            pause()
            self.hud()
            return total_damage_to_opponent

    def vozzbozz_attack(self, monster):
        print(f"Vozzbozz attacks with Quantum Energy!!")
        sleep(1)
        if monster.hit_points < 100:
            return self.vozzbozz_word_kill(monster)
        else:
            rndm_effect_lst = [self.vozzbozz_moon_crusher, self.vozzbozz_skeletal_remains,
                               self.vozzbozz_negative_energy_plague]
            rndm_effect = random.choice(rndm_effect_lst)
            return rndm_effect(monster)

    def quantum_spoken_word(self, monster):
        # everything but a 1 roll will succeed
        # if monster < 125 hp, it dies
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Spoken Word" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Spoken Word" in monster.vulnerabilities:
                    vulnerable = True
                self.quantum_units -= quantum_unit_cost
                print(f"Spoken Word.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.acumen)
                print(f"Clearing your mind, you attempt to harness the weird energies...")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                if roll_d20 == 1 and not vulnerable:
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                else:
                    if monster.hit_points < 125:
                        print(f"SUPPLICIUM!!")
                        sleep(1.5)
                        return monster.hit_points
                    else:
                        print(f"The {monster.name} has too much life energy to succumb to the quantum effect!")
                        pause()
                        return 0
        else:
            print(f"Quantum Spoken Word is a Battle Effect only..")
            sleep(1)
            return

    def quantum_disentangle(self, monster):
        # Quantum weirdness shoots to your enemy.
        # A creature targeted by this spell must make a Dexterity protection roll.
        # On a failed save, the target takes full effect damage.
        # The target is disentangled if this damage leaves it with 0 hit points.

        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Disentangle" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Disentangle" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Disentangle" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Disentangle.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + 40
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Quantum Weirdness released from your hand shoots toward your enemy!")
                        sleep(1)
                        print(f"{number_of_dice}d{quantum_hit_die} roll + 40 force damage: {damage_to_opponent}")
                        print(f"The {monster.name} suffers {damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        monster.reduce_health(damage_to_opponent)
                        if not monster.check_dead():
                            return 0  # damage already returned to reduce_health function
                        else:
                            if monster.proper_name != "None":
                                print(f"{monster.proper_name} has been disentangled from all existence!!")
                            else:
                                print(f"The {monster.name} has been disentangled from all existence!!")
                            sleep(1.5)
                            monster.gold = 0

                            self.in_proximity_to_monster = False
                            # pause()
                            return 0
                    else:
                        print(f"It fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    print(f"Quantum Weirdness released from your hand shoots toward your enemy!")
                    sleep(1)
                    print(f"The {monster.name} dodges!")
                    sleep(1)
                    pause()
                    self.hud()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Quantum Disentangle!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Quantum Disentangle!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Disentangle is a Battle Effect only..")
            sleep(1)
            return

    def firewall(self, monster):
        # everything but a 1 roll will succeed
        # on a successful dexterity protection roll, monster takes 50% damage.
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            if "Firewall" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Firewall" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Firewall" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Firewall.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Firewall..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"A tiny burning cinder, no larger than a grain of sand "
                          f"pops into existence and is snuffed out just as suddenly..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 10
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # print(f"Attack roll: {roll_d20}")
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A red-hot wall of dreadful flames forms from your hand and speeds toward your enemy!")
                        print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The flaming wall of fire envelopes the target and inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 10
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice,
                                                              quantum_hit_die) + (1 * number_of_dice)))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The Firewall takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die rolled = "
                          f"{damage_to_opponent} (ROUNDED)")
                    # print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Firewall!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Firewall!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Firewall is a Battle Effect only..")
            sleep(1)
            return

    def finger_of_death(self, monster):
        # everything but a 1 roll will succeed
        # on a successful constitution protection roll, monster takes 50% damage.
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            if "Finger of Death" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Finger of Death" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Finger of Death" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Finger of Death.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies...... ")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 10
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Your hands throb with blinding Quantum Energy!")
                        sleep(1)
                        print(f"{number_of_dice}d{quantum_hit_die} roll + number of dice: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"You extend a white-hot finger, merely touching your enemy, inflicting "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Your effect fails to land any damage!")  # 0
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 10
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, quantum_hit_die) +
                                                    (4 * number_of_dice)))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"Your hands throb with red-hot Quantum Energy..")
                    sleep(1)
                    # print(f"The effect takes form but does not to its fullest potential..")
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 2 * number of dice rolled = "
                          f"{damage_to_opponent} (ROUNDED)")
                    # print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    sleep(1)
                    print(f"You extend a glowing finger and touch your enemy, inflicting "
                          f"{total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Finger of Death!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Finger of Death!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Finger of Death is a Battle Effect only..")
            sleep(1)
            return

    def moon_crusher(self, monster):
        # everything but a 1 roll will succeed
        # on a successful dexterity protection roll, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Mooncrusher" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Mooncrusher" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Mooncrusher" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Mooncrusher.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird Quantum Energies "
                    f"to rend the Mooncrusher..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"A tiny burning cinder, no larger than a grain of sand "
                          f"pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier

                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    crushing_dmg_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, crushing_dmg_die) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a world-shaking and awe-inspiring eruption, "
                              f"a swarm of burning moon-matter appears above and falls upon your enemy!!")
                        print(f"{number_of_dice}d{quantum_hit_die} + {number_of_dice}d{crushing_dmg_die} "
                              f"crushing damage + 1 per die rolled: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great storm of fire and stone explodes directly on target in surreal "
                              f"glory and inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # no crush
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The Mooncrusher takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die rolled = {damage_to_opponent}")
                    print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Quantum Mooncrusher!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Quantum Mooncrusher!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Mooncrusher is a Battle Effect only..")
            sleep(1)
            return

    def skeletal_remains(self, monster):
        # everything but a 1 roll will succeed.
        # on a successful dexterity protection roll, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Skeletal Remains" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Skeletal Remains" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Skeletal Remains" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Skeletal Remains.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Skeletal Remains..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"A tiny jawbone pops into existence and is hurled upon your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    force_dmg_die = 8
                    no_of_skeletons = dice_roll(number_of_dice, quantum_hit_die)
                    damage_to_opponent = no_of_skeletons + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, force_dmg_die) + (1 * number_of_dice)  # 3rd attack = bludgeoning
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Before you or your enemy can see it, you both sense the ground swell with the\n"
                              f"thundering cacophony of {no_of_skeletons} skeletal warriors arising from a "
                              f"black chasm!!")
                        sleep(1)
                        print(f"Some on horseback, others on foot, but with one mind and purpose, they swarm upon\n"
                              f"your enemy, thrusting ever forward in a voracious clashing of bone, steel and shield!!")
                        sleep(1)
                        print(f"{number_of_dice}d{quantum_hit_die} + {number_of_dice}d{force_dmg_die} "
                              f"force damage + 1 per die rolled bludgeoning damage: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        # print(f"It hits for {total_damage_to_opponent} points of damage..")
                        print(f"The great swarm of armor, axe, sword and spear inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, the skeletal horde"
                              f" fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # no f dmg
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The skeletal horde takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per skeleton bludgeoning damage = "
                          f"{damage_to_opponent}")
                    print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Skeletal Remains!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Skeletal Remains!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Skeletal Remains is a Battle Effect only..")
            sleep(1)
            return

    def negative_energy_plague(self, monster):
        # everything but a 1 roll will succeed
        # on a successful intelligence protection roll, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Negative Energy Plague" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Negative Energy Plague" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Negative Energy Plague" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Negative Energy Plague.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Negative Energy Plague..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    # print(f"A tiny jawbone pops into existence and is hurled upon your enemy..")
                    # sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = round((monster.intelligence - 10) / 2)
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Intelligence Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    crushing_dmg_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, crushing_dmg_die) + (1 * number_of_dice)  # 2nd attack = crushing dmg
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                              f"from your hands toward your enemy!!")
                        sleep(1)
                        print(f"With universal abhorrence, the negative energy plague entangles the {monster.name}!!")
                        sleep(1)
                        print(f"{number_of_dice}d{quantum_hit_die} necrotic damage + "
                              f"{number_of_dice}d{crushing_dmg_die} crushing damage + 1 per die "
                              f"rolled mental anguish: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great, empty darkness inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, the plague"
                              f" fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)  # no crush
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The plague takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(
                        f"{number_of_dice}d{quantum_hit_die} necrotic damage + 1 per die rolled mental damage: "
                        f"{damage_to_opponent}")
                    print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Negative Energy Plague!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Plague!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Negative Energy Plague is a Battle Effect only..")
            sleep(1)
            return

    def ice_storm(self, monster):
        # everything but a 1 roll will succeed
        # on a successful constitution protection Roll, monster takes 50% damage.
        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Ice Storm" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Ice Storm" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Ice Storm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Ice Storm.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies "
                    f"to create the Ice Storm..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"A single snowflake pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (self.acumen * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a crackling rumble, a frigid storm of ice and hail thrusts forth from your hand!!")
                        print(
                            f"{number_of_dice}d{quantum_hit_die} roll + {number_of_dice} + "
                            f"({self.acumen} * number of dice rolled): "
                            f"{damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great freezing storm explodes on target and does "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, quantum_hit_die) +
                                                   (self.acumen * number_of_dice))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The storm does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(
                        f"{number_of_dice}d{quantum_hit_die} roll + ({self.acumen} * number of dice rolled): "
                        f"{damage_to_opponent} (ROUNDED) ")
                    # print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Ice Storm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Ice Storm!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Ice Storm is a Battle Effect only..")
            sleep(1)
            return

    def fire_storm(self, monster):
        # everything but a 1 roll will succeed
        # on a successful dexterity protection Roll, monster takes reduced damage.
        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Fire Storm" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Fire Storm" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Fire Storm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Fire Storm.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies "
                    f"to create the Fire Storm..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"A single glowing ember pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (self.acumen * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a deafening roar, a storm of searing hot flames thrusts forth from your hand!!")
                        print(
                            f"{number_of_dice}d{quantum_hit_die} roll + {number_of_dice} + "
                            f"({self.acumen} * number of dice rolled): "
                            f"{damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The scorching storm explodes on target and does "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 12
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, quantum_hit_die) +
                                                   (self.acumen * number_of_dice))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The storm does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + ({self.acumen} * number of dice rolled) = "
                          f"{damage_to_opponent} (ROUNDED) ")
                    # print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent

            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Fire Storm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Fire Storm!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Fire Storm is a Battle Effect only..")
            sleep(1)
            return

    def phantasm(self, monster):
        # phantasm matches your wisdom vs monster intelligence
        quantum_unit_cost = 3
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            if "Phantasm" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerable = False
                if "Phantasm" in monster.vulnerabilities:
                    vulnerable = True
                    vulnerability_modifier = self.acumen
                resistance_modifier = 0
                if "Phantasm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Phantasm.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies "
                      f"to create the illusion..")
                sleep(1)
                print(f"Quantum Check: {roll_d20}")  # anything but a natural 1 is success
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print(f"The Phantasm pops into existence as a cloudy blur, and promptly vanishes..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Acumen: {self.acumen}")
                if vulnerable:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = math.floor((monster.intelligence - 10) / 2)
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Intelligence Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:  # > tie goes to defender >= tie goes to player
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (self.acumen * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"The Phantasmal illusion takes form through weird Quantum "
                              f"tunneling and completely seizes the mind of your enemy!")
                        print(f"{number_of_dice}d{quantum_hit_die} roll + {self.acumen} per die: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The terrible vision inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, quantum_hit_die) +
                                                    (1 * number_of_dice)))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The Phantasmal illusion takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die rolled = "
                          f"{damage_to_opponent} (ROUNDED)")
                    # print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.undead:
                    print(f"Undead do not believe!!")
                    sleep(1)
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Phantasm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Phantasmal Forces!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Phantasm is a Battle Effect only..")
            sleep(1)
            return

    def quantum_lightning(self, monster):
        # lightning matches player wisdom against monster AC
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Lightning" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Lightning" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Lightning" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Lightning.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The Lightning crackles into existence "
                          f"and spreads randomly, completely missing the {monster.name}..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"{number_of_dice} bolts of Quantum Lightning materialize from nothingness and "
                              f"hit their target!")
                        print(f"{number_of_dice}d{quantum_hit_die} roll + 1 burn damage per bolt: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Arcflash Damage: {melee_bonus}")
                        print(f"They do {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own Weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = (dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice))

                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The lightning takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die rolled = "
                          f"{damage_to_opponent} (ROUNDED)")

                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Quantum Lightning!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Quantum Lightning attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Lightning is a Battle Effect only..")
            sleep(1)
            return

    def immolation(self, monster):
        # immolation matches player wisdom against monster dexterity
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Immolation" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Immolation" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Immolation" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Immolation.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The wreath of flame crackles into existence "
                          f"and spreads wildly, completely missing your target..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                vulnerability_modifier = 0
                if vulnerable:
                    vulnerability_modifier = self.acumen
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if vulnerability_modifier > 0:
                    print(f"Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_total = monster_roll + monster.dexterity_modifier + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster.dexterity_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_dc >= monster_total:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A serpentine trail of fire materializes from nothingness and "
                              f"wreathes your target in scorching flame!")
                        print(f"{number_of_dice}d{quantum_hit_die} roll: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"It inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own Weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die)
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = damage_to_opponent
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The trail of fire takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll: {damage_to_opponent} (ROUNDED)")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Quantum Immolation Effects!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Quantum Immolation attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Immolation is a Battle Effect only..")
            sleep(1)
            return

    def vortex(self, monster):
        # vortex matches player wisdom against monster strength
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Vortex" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Vortex" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Vortex" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Vortex.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The watery twister materializes and spreads wildly, completely missing your target..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                vulnerability_modifier = 0
                if vulnerable:
                    vulnerability_modifier = self.acumen
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.acumen + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")
                if vulnerability_modifier > 0:
                    print(f"Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_total = monster_roll + monster.strength_modifier + resistance_modifier
                print(f"Monster Protection Roll: {monster_roll}")
                print(f"Monster Strength Modifier: {monster.strength_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_dc >= monster_total:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A twisting vortex of roaring water materializes from nothingness and "
                              f"wraps your target with impossible crushing force!")
                        sleep(1)
                        print(f"{number_of_dice}d{quantum_hit_die} roll: {damage_to_opponent}")
                        print(f"{self.acumen}d{self.hit_dice} Damage bonus: {melee_bonus}")
                        print(f"It inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own Weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 8
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, quantum_hit_die))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The twister takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll: {damage_to_opponent} (ROUNDED)")
                    # print(f"{self.acumen}d{self.hit_dice} Damage bonus: {melee_bonus}")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Vortex Effects!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Vortex attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Vortex is a Battle Effect only..")
            sleep(1)
            return

    def quantum_missile(self, monster):
        # q_missile matches player wisdom vs monster AC
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            if "Quantum Missile" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Quantum Missile" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Quantum Missile" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Missile.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to aim the "
                      f"Quantum Missile at the {monster.name}..")
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The projectiles go awry..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")

                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    # number_of_dice = (3 + (self.level - 1)) * critical_bonus  #consider changing to self.quantum_level
                    number_of_dice = (1 + self.acumen) * critical_bonus
                    quantum_die = 6
                    damage_to_opponent = (dice_roll(number_of_dice, quantum_die) + (1 * number_of_dice))
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"{number_of_dice} glowing projectiles materialize from nothingness and "
                              f"hit their target!")
                        print(f"{number_of_dice}d{quantum_die} roll + 1 force damage per projectile: "
                              f"{damage_to_opponent}\n"
                              f"{self.acumen}d{self.hit_dice} Damage bonus: {melee_bonus}\n"
                              f"Total: {total_damage_to_opponent}")
                        print(f"They do {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"It blocks the glowing projectiles!")  # zero damage result
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (1 + self.acumen) * critical_bonus
                    quantum_die = 6
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, quantum_die) + (1 * number_of_dice)))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The glowing projectiles take form but do not inflict damage to their fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_die} roll + 1 per die rolled: {damage_to_opponent}\n"
                          f"Total: {total_damage_to_opponent} (ROUNDED)")
                    print(f"They do {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent

            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Quantum Missile attack!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Quantum Missile attack!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Missile is a Battle Effect only..")
            sleep(1)
            return

    def quantum_blaze(self, monster):
        # blaze is player's wisdom vs monster AC
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            if "Blaze" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Blaze" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Blaze" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = monster.evil_bonus
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Blaze.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.acumen)
                print(f"Focusing your innate understanding, you attempt to grasp the weirdness..")
                print(f"Quantum Check: {roll_d20}")
                sleep(1.5)
                self.hud()
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The rays of flame fly off chaotically..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = "Blazing rays of scorching flame are summoned by Quantum Weirdness and strike " \
                                    "your enemy!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Acumen: {self.acumen}")

                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    # number_of_dice = (3 + (self.level - 1)) * critical_bonus
                    number_of_dice = (self.level + self.acumen) * critical_bonus
                    quantum_hit_die = 6
                    damage_to_opponent = dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        # print(f"Quantum Blaze = {number_of_dice}d{quantum_hit_die}(dice) + 1 * number of dice")
                        print(f"{number_of_dice}d{quantum_hit_die} + "
                              f"{number_of_dice} rays (1 force damage per ray): {damage_to_opponent}\n"
                              f"{self.acumen}d{self.hit_dice} Damage bonus: {melee_bonus}\n"
                              f"Total: {total_damage_to_opponent}")
                        print(f"They inflict {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"{monster.he_she_it.capitalize()} dodges the blazing rays!")  # zero damage result
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (1 + self.acumen) * critical_bonus
                    quantum_hit_die = 6
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, quantum_hit_die) + (1 * number_of_dice)))
                    # melee_bonus = dice_roll(self.acumen, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent)
                    print("Your attempt to harness the Quantum Weirdness lacks focus..")
                    sleep(1)
                    print(f"The blazing rays take form but do not inflict damage to their fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d{quantum_hit_die} roll + 1 per die rolled: {damage_to_opponent}\n"
                          f"Total: {total_damage_to_opponent} (ROUNDED)")
                    print(f"They inflict {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent

            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Quantum Blaze!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Quantum Blaze!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Blaze is a Battle Effect only..")
            sleep(1)
            return

    def evade(self, monster):
        # called from main loop, using return value from battle_menu_choices(), (if player has no allies)
        if self.encounter < 21:
            print(f"You attempt a stealthy evasive maneuver..")
            sleep(1)
            monster_roll = dice_roll(1, 20)
            monster_total = monster_roll + monster.dexterity_modifier
            player_roll = dice_roll(1, 20)
            evade_success = player_roll + self.dexterity_modifier + self.stealth + self.acumen
            if self.level > 3:
                evade_success += self.acumen
            print(f"Stealth Check: {player_roll}")
            print(f"Dexterity Modifier: {self.dexterity_modifier}")
            print(f"Stealth bonus: {self.stealth}")
            if self.level > 3:
                print(f"Acumen: {self.acumen}")

            print(f"Total: {evade_success}")
            sleep(1)
            print(f"Enemy Roll: {monster_roll}")
            print(f"Enemy Dexterity Modifier: {monster.dexterity_modifier}")
            print(f"Enemy Total: {monster_total}")
            if evade_success >= monster_total or evade_success == 20:
                print(f"You slip into the shadows..")
                sleep(1)
                print(f"Your stealth and dexterity have served you well!")
                sleep(1)
                print(f"The {monster.name} looks at {monster.his_her_its} surroundings, and departs,"
                      f" obviously confused.")
                sleep(1)
                print(f"You have successfully evaded the {monster.name}!")
                pause()
                self.hud()
                return True

            else:
                print(f"The {monster.name} swiftly blocks your escape!")
                sleep(.5)
                print(f"You are rooted to the spot. You must stand your ground!")
                pause()
                self.hud()
                return False

        else:
            # bosses cannot be evaded.
            if monster.proper_name != "None":
                print(f"{monster.proper_name} is far too adept to be evaded!")
            else:
                print(f"The {monster.name} is far too adept to be evaded!!")
            sleep(.5)
            print(f"You are rooted to the spot. You must stand your ground!")
            pause()
            self.hud()
            return False

    # INVENTORY AND ITEMS

    def chemist_main(self):
        rndm_aroma_lst = ['agarwood', 'angelica root', 'anise', 'basil', 'bergamot', 'calamodin', 'calamus', 'camphor',
                          'cardamom', 'cedar', 'camomile', 'cinnamon', 'citron', 'clary sage', 'clove', 'davana',
                          'eucalyptus',
                          'frankincense', 'galbanum', 'hemlock', 'jasmine', 'lavender', 'lemongrass', 'mugwort oil',
                          'pennyroyal', 'peppermint', 'sage', 'sandalwood', 'sassafras', 'garden mint', 'spikenard',
                          'spruce oil', 'star anise oil', 'tea tree oil', 'tarragon oil', 'tsuga oil', 'valerian',
                          'vanilla sweet grass', 'warionia', 'vetiver', 'wintergreen', 'yarrow oil']

        while True:
            self.hud()
            rndm_aroma = random.choice(rndm_aroma_lst)
            print(f"(In Town, Quantum Chemist Shop)")
            print(f"Jahns, the Fieldenberg Quantum Chemist is here, busying himself at the crucible.\n"
                  f"Mortars and pestles litter the counter and the smell of {rndm_aroma} fills the air...")

            '''if self.hit_points < self.maximum_hit_points:
                print("The aura fills your nostrils and lungs...healing you to full strength!")
                self.hit_points = self.maximum_hit_points
                pause()
                self.hud()'''

            print(f"Your gold: {self.gold} GP")
            chemist_choice = input(
                "(P)urchase quantum items, (S)ell quantum items, Display your (I)nventory, or "
                "(E)xit the chemist: ").lower()

            if chemist_choice == 'p':
                self.buy_chemist_items()
                continue

            elif chemist_choice == 's':
                self.sell_chemist_items()
                continue

            elif chemist_choice == 'i':
                self.inventory()
                continue

            elif chemist_choice == 'e':
                return

            else:
                continue

    def sell_chemist_items(self):
        # this code for belt item inventory works, but was written very early on and is extremely amateurish.
        # it handles belt inventory in a clunky way, e.g. self.elixirs is simply an integer, and there is no
        # belt dictionary like self.pack

        # create new instances of all objects:
        healing_potion = HealingPotion()
        strength_potion = StrengthPotion()
        scroll_of_town_portal = TownPortalImplements()
        elixir = Elixir()
        antidote = Antidote()

        while True:
            self.hud()
            belt = [self.potions_of_healing, self.town_portals, self.potions_of_strength, self.elixirs, self.antidotes]
            if sum(belt) == 0:
                print(f"You have no quantum items to sell..")
                pause()
                return

            print(f"Your gold: {self.gold} GP")
            print(f"You currently carry the following quantum items:")
            print(f"1: Potions of Strength - Quantity: {self.potions_of_strength}")
            print(f"2: Potions of Healing - Quantity: {self.potions_of_healing}")
            print(f"3: Scrolls of Town Portal - Quantity: {self.town_portals}")

            print(f"4: Clarifying Elixirs - Quantity: {self.elixirs}")
            print(f"5: Poison Antidote Vials - Quantity: {self.antidotes}")
            print(f"Your gold: {self.gold} GP")
            type_to_sell = input(f"Pick item to sell by number, or go (B)ack: ").lower()

            if type_to_sell == 'b':
                return

            elif type_to_sell == '1':
                your_item = "potions of strength"

                if self.potions_of_strength < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '2':
                your_item = "potions"

                if self.potions_of_healing < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '3':
                your_item = "scrolls of town portal"

                if self.town_portals < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '4':
                your_item = "clarifying elixirs"

                if self.elixirs < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '5':
                your_item = "vials of antidote"

                if self.antidotes < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            else:
                print(f"Invalid..")
                continue

            try:
                number_of_items_to_sell = int(input(f"Enter number of {your_item} to sell: "))

                if type_to_sell == '1' and number_of_items_to_sell > 0:

                    if self.potions_of_strength >= number_of_items_to_sell:
                        self.potions_of_strength -= number_of_items_to_sell
                        gold_received = (strength_potion.sell_price * number_of_items_to_sell)
                        self.gold += gold_received
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_received} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '2' and number_of_items_to_sell > 0:

                    if self.potions_of_healing >= number_of_items_to_sell:
                        self.potions_of_healing -= number_of_items_to_sell
                        gold_received = (healing_potion.sell_price * number_of_items_to_sell)
                        self.gold += gold_received
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_received} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '3' and number_of_items_to_sell > 0:

                    if self.town_portals >= number_of_items_to_sell:
                        self.town_portals -= number_of_items_to_sell
                        gold_received = (scroll_of_town_portal.sell_price * number_of_items_to_sell)
                        self.gold += gold_received
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_received} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '4' and number_of_items_to_sell > 0:

                    if self.elixirs >= number_of_items_to_sell:
                        self.elixirs -= number_of_items_to_sell
                        gold_received = (elixir.sell_price * number_of_items_to_sell)
                        self.gold += gold_received
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_received} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '5' and number_of_items_to_sell > 0:

                    if self.antidotes >= number_of_items_to_sell:
                        self.antidotes -= number_of_items_to_sell
                        gold_received = (antidote.sell_price * number_of_items_to_sell)
                        self.gold += gold_received
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_received} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                else:
                    print(f"Invalid entry..")

            except ValueError:
                print("Invalid input")
                continue

    def buy_chemist_items(self):
        # create new instances of all objects:
        healing_potion = HealingPotion()
        strength_potion = StrengthPotion()
        scroll_of_town_portal = TownPortalImplements()
        elixir = Elixir()
        antidote = Antidote()

        chemist_dict = {
            'Potions of Giant Strength': [strength_potion],
            'Potions of Healing': [healing_potion],
            'Town Portal Scrolls': [scroll_of_town_portal],
            'Elixirs': [elixir],
            'Antidotes': [antidote]
        }
        while True:
            self.hud()
            print(f"Jahns has items for sale in the following categories:")
            # create a list of item types:
            item_type_lst = list(chemist_dict.keys())
            # create a dictionary from list of item types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Pick item type by number, Display your (I)nventory, or go (B)ack: ").lower()

            if buy_or_exit == 'i':
                self.inventory()
                continue

            elif buy_or_exit == 'b':
                return
                # break

            elif buy_or_exit not in ('i', 'b'):
                try:
                    item_type_index_to_buy = int(buy_or_exit)
                    # item_type_index_to_buy = int(input(f"Enter the category of the item to buy by number: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue

                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    chemist_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (chemist_dict[item_type_to_buy]):
                        item_dict[item] = (chemist_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Pick item by number, Display your (I)nventory, or go (B)ack: ").lower()

                    if buy_or_exit == 'i':
                        self.inventory()
                        continue

                    elif buy_or_exit == 'b':
                        break

                    elif buy_or_exit not in ('i', 'b'):
                        try:
                            item_index_to_buy = int(buy_or_exit)
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (chemist_dict[item_type_to_buy])[item_index_to_buy]

                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue

                        try:
                            number_of_items = int(input(f"How many would you like to buy: "))

                        except ValueError:
                            print("Invalid entry..")
                            sleep(1)
                            continue

                        if number_of_items > 0:
                            purchase_price = sale_item.buy_price * number_of_items

                            if self.gold >= purchase_price:

                                if self.level >= sale_item.minimum_level:
                                    self.gold -= purchase_price
                                    # replace these if statements with dictionary in future

                                    if sale_item.name == 'Scroll of Town Portal':
                                        self.town_portals += number_of_items

                                    elif sale_item.name == 'Potion of Strength':
                                        self.potions_of_strength += number_of_items

                                    elif sale_item.name == 'Potion of Healing':
                                        self.potions_of_healing += number_of_items

                                    elif sale_item.name == 'Clarifying Elixir':
                                        self.elixirs += number_of_items

                                    elif sale_item.name == 'Vial of Antidote':
                                        self.antidotes += number_of_items
                                    self.hud()
                                    print(f"You buy {number_of_items} {sale_item.name}s")
                                    # (self.pack[sale_item.item_type]).append(sale_item)
                                    self.item_type_inventory(sale_item.item_type)
                                    pause()
                                    break

                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            print(f"Zero..")
                            continue

    def item_management_sub_menu(self):
        while True:
            self.hud()
            item_to_manage = input(
                f"Manage (W)eapons, (A)rmor, (S)hields, (B)oots, (C)loaks, View your (I)nventory, or "
                f"(E)xit Item Management: ").lower()

            if item_to_manage == 'w':
                self.item_management('Weapons', self.wielded_weapon)
                continue

            elif item_to_manage == 'a':
                self.item_management('Armor', self.armor)
                continue

            elif item_to_manage == 's':
                self.item_management('Shields', self.shield)
                continue

            elif item_to_manage == 'b':
                self.item_management('Boots', self.boots)
                continue

            elif item_to_manage == 'c':
                self.item_management('Cloaks', self.cloak)
                continue

            elif item_to_manage == 'i':
                self.inventory()
                continue

            elif item_to_manage == 'e':
                return

            else:
                continue

    def blacksmith_main(self):
        while True:
            # you can make this into a dictionary, with each value being a function
            # something like
            # if blacksmith_choice in blacksmith_main_dict:
            #   blacksmith_function = (blacksmith_main_dict[blacksmith_choice])
            #   blacksmith_function()
            # elif blacksmith_choice == 'e':
            #   return
            self.hud()
            print(f"(In Town, Blacksmith Shop)")
            print(f"Lucino, the Fieldenberg blacksmith is here, hammering at his anvil.\n"
                  f"He notices you, grumbles, and continues hammering...")
            print(f"Your gold: {self.gold} GP")
            blacksmith_choice = input(
                "(P)urchase items, (L)iquidate items, (M)anage your inventory items, "
                "View (I)nventory, or (E)xit the blacksmith: ").lower()

            if blacksmith_choice == 'p':
                self.buy_blacksmith_items()
                continue

            elif blacksmith_choice == 'l':
                self.sell_blacksmith_items()
                continue

            elif blacksmith_choice == 'm':
                self.item_management_sub_menu()

            elif blacksmith_choice == 'i':
                self.inventory()
                continue

            elif blacksmith_choice == 'e':
                return

            else:
                continue

    def buy_blacksmith_items(self):
        # create new instances of all objects:
        short_axe = ShortAxe()
        broad_sword = BroadSword()
        great_sword = GreatSword()
        elvish_great_sword = ElvishGreatSword()
        quantum_sword = QuantumSword()
        battle_axe = BattleAxe()
        great_axe = GreatAxe()
        elvish_great_axe = ElvishGreatAxe()
        quantum_axe = QuantumAxe()
        leather_armor = LeatherArmor()
        studded_leather_armor = StuddedLeatherArmor()
        scale_mail = ScaleMail()
        half_plate = HalfPlate()
        full_plate = FullPlate()
        buckler = Buckler()
        kite_shield = KiteShield()
        quantum_tower_shield = QuantumTowerShield()
        elven_boots = ElvenBoots()
        ancestral_footsteps = AncestralFootsteps()
        elven_cloak = ElvenCloak()

        blacksmith_dict = {
            'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                        quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
            'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
            'Shields': [buckler, kite_shield, quantum_tower_shield],
            'Boots': [elven_boots, ancestral_footsteps],
            'Cloaks': [elven_cloak]
        }
        while True:
            self.hud()
            print(f"Armory for sale:")
            # create a list of blacksmith item types:
            item_type_lst = list(blacksmith_dict.keys())
            # create a dictionary from list of blacksmith items types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Pick item type by number, Display your (I)nventory, or go (B)ack: ").lower()
            # if buy_or_exit not in ('i', 'p', 'b'):
            #    self.hud()
            #    continue
            if buy_or_exit == 'i':
                self.inventory()
                continue
            elif buy_or_exit == 'b':
                return
            elif buy_or_exit not in ('i', 'b'):
                try:
                    item_type_index_to_buy = int(buy_or_exit)
                    # item_type_index_to_buy = int(input(f"Enter the number of the category of the item to buy: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    blacksmith_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (blacksmith_dict[item_type_to_buy]):
                        item_dict[item] = (blacksmith_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Pick item by number, Display your (I)nventory, or go (B)ack: ").lower()
                    if buy_or_exit == 'i':
                        self.inventory()
                        continue
                    elif buy_or_exit == 'b':
                        break
                    elif buy_or_exit not in ('i', 'b'):
                        try:
                            item_index_to_buy = int(buy_or_exit)
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (blacksmith_dict[item_type_to_buy])[item_index_to_buy]
                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        confirm_purchase = input(
                            f"Purchase {sale_item.name} for {sale_item.buy_price} GP (y/n)? ").lower()
                        if confirm_purchase == 'y':
                            if self.gold >= sale_item.buy_price:
                                if self.level >= sale_item.minimum_level:
                                    if not self.duplicate_item(sale_item.item_type, sale_item):
                                        self.hud()
                                        print(f"You buy the {sale_item.name}")
                                        self.gold -= sale_item.buy_price
                                        (self.pack[sale_item.item_type]).append(sale_item)
                                        self.item_type_inventory(sale_item.item_type)
                                        pause()
                                        continue
                                    else:
                                        print(f"You already have a {sale_item.name}")
                                        pause()
                                        continue
                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            continue

    def item_management(self, item_type, current_item):
        self.hud()
        if len(self.pack[item_type]) > 0:
            print(f"Your current {item_type} inventory:")
            (self.pack[item_type]).sort(key=lambda x: x.buy_price)
            item_mgmt_dict = {}
            for item in (self.pack[item_type]):
                item_mgmt_dict[item] = (self.pack[item_type]).index(item)
            for key, value in item_mgmt_dict.items():
                print(value + 1, ':', key)  # value is index. indexing starts at zero, so add 1
            print()
        else:
            print(f"You have nothing in your {item_type} inventory..")
            pause()
            return
        old_item = current_item
        print(f"You are currently using: ")
        if item_type == 'Weapons':
            print(f"{self.wielded_weapon}, Sell Price: {self.wielded_weapon.sell_price} GP")

        elif item_type == 'Armor':
            print(f"{self.armor}, Sell Price: {self.armor.sell_price} GP")

        elif item_type == 'Shields':
            if self.shield.name != 'No Shield':
                print(f"{self.shield}, Sell Price: {self.shield.sell_price} GP")
            else:
                print(f"{self.shield.name}")
        elif item_type == 'Boots':
            print(f"{self.boots}, Sell Price: {self.boots.sell_price} GP")

        elif item_type == 'Cloaks':
            print(f"{self.cloak}, Sell Price: {self.cloak.sell_price} GP")
        swap_or_exit = input(f"(S)wap item, or go (B)ack: ").lower()
        if swap_or_exit == "b":
            return
        elif swap_or_exit == "s":

            try:
                new_item_index = int(input(f"Enter the number of the item from your inventory that you wish to use: "))
                new_item_index -= 1  # again, indexing starts at 0 so add 1
                if item_type == 'Weapons':
                    new_weapon = (self.pack[item_type])[new_item_index]  # SYNTAX FOR INDEX
                    print(f"{new_weapon}")
                    self.wielded_weapon = new_weapon
                elif item_type == 'Armor':
                    new_armor = (self.pack[item_type])[new_item_index]
                    print(f"{new_armor}")
                    self.armor = new_armor
                elif item_type == 'Shields':
                    new_shield = (self.pack[item_type])[new_item_index]
                    print(f"{new_shield}")
                    self.shield = new_shield
                elif item_type == 'Boots':
                    new_boots = (self.pack[item_type])[new_item_index]
                    print(f"{new_boots}")
                    self.boots = new_boots
                elif item_type == 'Cloaks':
                    new_cloak = (self.pack[item_type])[new_item_index]
                    print(f"{new_cloak}")
                    self.cloak = new_cloak
                # CALCULATE STEALTH AND ARMOR CLASS. NOTICE INDENT
                self.calculate_stealth()
                self.calculate_armor_class()
            except (IndexError, ValueError):
                print("Invalid entry..")
                sleep(1)
                return
            print(f"You are now using the {(self.pack[item_type])[new_item_index]}.")
            if old_item.name != 'No Shield':
                print(f"You place the {old_item.name} in your inventory.")
                (self.pack[item_type]).pop(new_item_index)  # INDEX SYNTAX
                (self.pack[item_type]).append(old_item)  # old_weapon represents an object, not an index
                # (self.pack[item_type]).sort(key=lambda x: x.buy_price)
                pause()
            else:
                print(f"You are well equipped.")
                pause()

    def check_if_pack_empty(self):
        non_empty_item_type_lst = []
        for key in self.pack:
            if len(self.pack[key]) > 0:
                non_empty_item_type_lst.append(key)
        number_of_items_in_pack = len(non_empty_item_type_lst)
        if number_of_items_in_pack < 1:
            return True
        else:
            return False

    def sell_blacksmith_items(self):
        # sell_blacksmith_items() allows you to sell items from self.pack
        while True:
            cls()
            # self.hud()
            # print(f"You have items eligible to sell in the following categories:")
            non_empty_item_type_lst = []
            # make a list of non-empty inventory item keys from player's pack inventory
            for key in self.pack:
                if len(self.pack[key]) > 0:
                    non_empty_item_type_lst.append(key)
            number_of_items_in_pack = len(non_empty_item_type_lst)
            if number_of_items_in_pack < 1:
                print(f"Your pack is empty.")
                pause()
                return

            else:
                # print(non_empty_item_type_lst)  # remove after testing
                # make a dictionary from the non_empty item type list. index, and print
                print(f"You have items eligible to sell in the following categories:")
                item_type_dict = {}
                for item_type in self.pack:
                    if len(self.pack[item_type]) and item_type != 'Rings of Protection' and \
                            item_type != 'Rings of Regeneration':
                        item_type_dict[item_type] = non_empty_item_type_lst.index(item_type)
                for key, value in item_type_dict.items():
                    print(value + 1, ':', key)

                try:
                    print(f"Your gold: {self.gold} GP")
                    sell_or_exit = input("(S)ell items, (L)iquidate entire contents of pack, or go (B)ack: ").lower()
                    if sell_or_exit not in ('s', 'l', 'b'):
                        cls()
                        # self.hud()
                        continue
                    if sell_or_exit == 'l':
                        self.sell_everything()
                        return
                    if sell_or_exit == 'b':
                        break
                    item_type_index_to_sell = int(input(f"Enter the number of the category of the item to sell: "))
                    item_type_to_sell = non_empty_item_type_lst[item_type_index_to_sell - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue

            while True:
                cls()
                # self.hud()
                persistent_item_type = item_type_to_sell
                print(f"Your {item_type_to_sell} inventory eligible for sale:")
                # self.item_type_inventory(item_type_to_sell)
                sell_all = []
                mgmt_dict = {}
                for item in (self.pack[item_type_to_sell]):
                    mgmt_dict[item] = (self.pack[item_type_to_sell]).index(item)
                for key, value in mgmt_dict.items():
                    print(value + 1, ':', key.name, '- Sell price:', key.sell_price, 'GP')
                    sell_all.append(key.sell_price)
                gold_for_all_items = sum(sell_all)
                if not len(sell_all):
                    # if gold_for_all_items == 0:
                    print(f"You have no {item_type_to_sell} to sell.")
                    pause()
                    break
                else:
                    print(f"Total sell price for all {item_type_to_sell}: {gold_for_all_items} GP")
                print(f"Your gold: {self.gold} GP")
                sell_or_exit = input(
                    f"Show entire (I)nventory, (S)ell an item, Sell (A)ll {item_type_to_sell} or go (B)ack: ").lower()
                if sell_or_exit not in ('i', 's', 'a', 'b'):
                    cls()
                    # self.hud()
                    continue
                elif sell_or_exit == 'a':

                    while True:
                        yes_or_no = input(f"Sell all {item_type_to_sell} for {gold_for_all_items} GP? (y/n)? ").lower()
                        if yes_or_no not in ('y', 'n'):
                            continue
                        elif yes_or_no == 'y':
                            print(f"You sell all of your {item_type_to_sell} for {gold_for_all_items} GP.")
                            self.gold += gold_for_all_items
                            (self.pack[item_type_to_sell]).clear()

                            if self.check_if_pack_empty():
                                print(f"You have no more {persistent_item_type.lower()} to sell, and your pack is "
                                      f"now completely empty.")
                                pause()
                                return

                            else:
                                pause()
                                break

                        elif yes_or_no == 'n':
                            break

                elif sell_or_exit == 'i':
                    self.inventory()
                    continue

                elif sell_or_exit == 'b':
                    break

                elif sell_or_exit == 's':

                    try:

                        item_index_to_sell = int(input(f"Enter the number of the item you wish to sell: "))
                        item_index_to_sell -= 1  # again, indexing starts at 0 and is awkward
                        sold_item = (self.pack[item_type_to_sell])[item_index_to_sell]
                    except (IndexError, ValueError):
                        print("Invalid entry..")
                        sleep(1)
                        continue

                    confirm_sale = input(f"Sell the {sold_item.name} for {sold_item.sell_price} GP (y/n)? ").lower()
                    if confirm_sale == 'y':
                        print(f"You sell the {sold_item.name} for {sold_item.sell_price} GP")
                        self.gold += sold_item.sell_price
                        (self.pack[item_type_to_sell]).pop(item_index_to_sell)
                        print(f"Your gold: {self.gold} GP")
                        pause()
                        cls()
                        # self.hud()

                        if len(self.pack[item_type_to_sell]) > 0:
                            self.item_type_inventory(item_type_to_sell)
                            print(f"Your gold: {self.gold} GP")
                            sell_again = input(
                                f"(S)ell more {persistent_item_type} (B)ack to main market menu or "
                                f"(E)xit to town: ").lower()

                            if sell_again == 's':
                                continue

                            elif sell_again == 'b':
                                break

                            else:
                                # if sell_again not in ('y', 'n'):
                                return
                        else:
                            # print(f"Your gold: {self.gold} GP")
                            if self.check_if_pack_empty():
                                print(f"You have no more {persistent_item_type.lower()} to sell, and your pack is "
                                      f"now completely empty.")
                                pause()
                                return
                            else:
                                print(f"You have no more {persistent_item_type.lower()} to sell...")
                                pause()
                                break
                    else:
                        continue

    def sell_everything(self):
        # this code took me many hours to come up with.
        # allows for liquidation of self.pack
        liquidate_lst = []
        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
        mgmt_dict = {}
        for each_category in item_type_lst:
            if len(self.pack[each_category]):
                for item in (self.pack[each_category]):
                    mgmt_dict[item] = (self.pack[each_category]).index(item)
        for key, value in mgmt_dict.items():
            print(key.name, '- Sell price:', key.sell_price, 'GP')
            liquidate_lst.append(key.sell_price)
        total = sum(liquidate_lst)
        print(f"Total: {total}")
        confirm_liquidate = input(f"Sell everything in your pack for {total} GP? ").lower()  # dungeoneer's pack
        if confirm_liquidate == 'y':
            for each_category in item_type_lst:
                (self.pack[each_category]).clear()
            print(f"You sell your entire armory inventory for {total} GP.")
            self.gold += total
            pause()
            return
        else:
            return

    def use_scroll_of_town_portal(self):
        # called from main loop
        if self.town_portals < 1:
            self.hud()
            print(f"You have no scrolls of town portal!")
            sleep(1.25)
            self.hud()
            return False
        else:
            self.hud()
            self.town_portals -= 1
            random_floppy_rw_sound()
            same_line_print(f"The quantum portal appears before you; an impossible tunneling between distant "
                            f"places..")
            dot_dot_dot(15)
            sleep(1.5)
            return True

    def poison_ingestion(self):
        # called from fountain_event(),
        self.hud()
        self.dot_multiplier = self.dungeon.level
        self.dot_turns = dice_roll(1, 5)
        rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                 "An unnerving frailty spreads throughout your body...",
                                 "Pain and tenderness courses through your body.."
                                 ]
        poisoned_phrase = random.choice(rndm_poisoned_phrases)
        print(f"{poisoned_phrase}")
        sleep(1.5)
        print(f"You have been poisoned!")
        self.poisoned = True
        self.poisoned_turns = 0
        pause()
        self.hud()
        return self.poisoned

    def drink_potion_of_strength(self):
        self.hud()
        rndm_drinking_phrases = [
            "Tilting it to your lips, you drain the tiny blue vial and the strength of giants surges through you!",
            "Retrieving the vial from your belt, you pop the cork and down the sweet liquid...\n"
            "Great power and vitality  courses through your body!",
            "No sooner is the tincture running down your throat, than does the great\n"
            "and overwhelming strength and vitality fill your body! You feel invincible!"
        ]
        drink_phrase = random.choice(rndm_drinking_phrases)
        if self.potions_of_strength > 0:
            print(f"{drink_phrase}")
            self.potion_of_strength_effect = True
            self.potions_of_strength -= 1
            self.potion_of_strength_uses = -1  # to compensate for end of turn calculation
            if self.hit_points < self.maximum_hit_points:  # in the rare case player has hit point overage,
                self.hit_points = self.maximum_hit_points  # this will not disrupt that advantage
            pause()
            return self.potion_of_strength_effect
        else:
            print(f"You have no potions of giant strength!")
            sleep(1)
            self.hud()
            return False

    def hint_event_1(self):
        # hint_events move the story along by subtle hints to the player, revealed over time in the game, as
        # they progress.
        # hint_events take place in the tavern (so far). they correspond to boss_clues:
        # hint_event_1 occurs after boss_clue_1, (which occurs after victory over dungeon exit boss lvl 1)
        # hint_event_2 after boss_clue_2, etc. the boss_clues occur after defeating the dungeon_exit boss
        # hint_event_1 is a meeting with vozzbozz, introduction to tor'bron the barbarian, and another hint
        # about the symbol of the wicked queen, which the player finds during boss_clue_1
        cls()
        print(f"As soon as she sees you, Jenna motions discreetly toward the hallway leading away from the bar.")
        sleep(1)
        print(f"You direct your eyes that way and casually make your way down the hall...")
        sleep(1)
        pause()
        cls()
        print(f"Jenna catches up to you at end of the hallway. Ye are {self.name}, are ye not?'\n"
              f"Nodding and instinctively looking about for eavesdroppers, you re-focus on her concerned look.")
        if len(self.vanquished_foes):
            vanquished_foes = convert_list_to_string_with_commas_only(self.vanquished_foes)
            print(f"'I know of ye.' Your puzzled look speaks for you, as she continues,\n"
                  f"'We 'ave 'eard of it.. how ye' 'ave defeated {vanquished_foes}...and others!'")
        pause()
        cls()
        teletype(f"'There is somethin' ye should know!' Her level of anxiety gives you pause; it seems out of\n"
                 f"character for her.\n'Ye should seek out Vozzbozz!' Pausing with a far away look, she nods.\n"
                 f"'I'm headin' back to the bar, and we'll make like we never spoke o' this..'\n"
                 f"'Vozzbozz is in the barroom. He's the one with the raven on 'is shoulder!'\n"
                 f"The meeting ends as abruptly as it began. Jenna disappears toward the bar as you slowly\n"
                 f"start to follow a good distance behind, impatient and confused.\n")
        pause()
        cls()
        # meeting with vozzbozz and introduction to tor'bron
        teletype_txt_file('hint_event_1.txt')
        pause()

        cls()
        teletype(f"{self.name},\nThe guardian of {self.dungeon.name} has, in its possession, an ornate dagger "
                 f"of very fine craftsmanship.\nIt is imperative you retrieve it. Return here with it so that "
                 f"matters may progress.\n"
                 f"\n                                                     -V\n")
        self.boss_hint_1_event = True
        pause()
        return

    def hint_event_2(self):
        print(f"As soon as she sees you, Jenna directs your attention to the opposite side of the room by raising\n"
              f"her chin in that general direction.\nAt the very same booth as last time, sits the hulking barbarian, "
              f"Tor'bron.")
        sleep(2)

        if self.sikira_ally:
            print(f"Both you and Si'Kira turn to behold him. With a curt slap on the back, Si'Kira says, 'Good "
                  f"luck, {self.name}! From the looks of him, you'll need it!'\nShe leaves your side and makes for "
                  f"the bar.")
            pause()
            cls()
        print(f"You cautiously approach him...")
        sleep(1)
        pause()
        cls()
        teletype(f"'Well! {self.name}!', he bellows in his booming voice. 'Sit!' Something in his dour demeanor\n"
                 f"tells you it is not an invitation, but an order. You marvel at the size and strength of the man.\n"
                 f"His jet black hair lays long on his head, and covers his body in a wiry patchwork.\n"
                 f"Long sideburns flank a strong jawbone, and his deep-set amber eyes burn with gripping intensity.\n"
                 f"'And where is it? Do you have it?', he asks, his tone tense and distrustful.\n"
                 f"You carefully retrieve the dagger and pass it to him across the table. Roughly and without "
                 f"regard,\n"
                 f"he swipes it from you, yanks it from its sheath and launches it across the room, over the heads\n"
                 f"of all the patrons on this side of the bar, until it abruptly lodges in the wall with a bang.")
        if len(self.vanquished_foes):
            vanquished_foes = convert_list_to_string_with_commas_only(self.vanquished_foes)
            teletype(f"'The slayer of {vanquished_foes}...\n...and others besides!'\n")
        teletype(f"'When first I saw you, I was...', he searches for the word. '..skeptical!'\n"
                 f"But now, things are different! Now I know you are able-bodied and strong! Good! Very good, this!' "
                 f"He nods.\n"
                 f"A sting of disrespect hits you. After the toil and struggle to retrieve the prized dagger, "
                 f"you are\n"
                 f"now realizing it was nothing more than a test to prove your mettle to this stranger!\n"
                 f"'You must be Tor'bron!', you say as you slide into the booth. His eyes\n"
                 f"narrow slightly and he takes a sip of ale. Continuing, you say, 'I heard Vozzbozz address you\n"
                 f"the last time we saw each other. And may I add, I never doubted *your* abilities!'\n"
                 f"Still alert, he thinks about your words. His glowering slowly turns to what must be a smile.\n"
                 f"Then, he laughs, a deep and hearty laugh. Instantly, he fiercely slams the table with his fist,\n"
                 f"so that the entire room shakes and becomes silent. He raises his huge hand, pointing\n"
                 f"straight at you. 'Good! Don't ever doubt them!' And again he smiles and laughs as the tavern "
                 f"ambience"
                 f"\ngradually returns. Reaching his tree-trunk arm toward you, he slams you on the shoulder with a"
                 f" heavy hand.\n"
                 f"You are thankful for the {self.armor.name.lower()} you wear; without it, the blow would "
                 f"undoubtedly "
                 f"have been an injury!\nInstinctively reaching for the aching shoulder, you reply plainly, "
                 f"'I certainly will not..'\n")
        pause()
        cls()
        # meet Tor'bron, get hints
        teletype_txt_file('hint_event_2.txt')
        pause()
        cls()
        self.boss_hint_2_event = True
        return

    def hint_event_3(self):
        # another meeting with vozzbozz. meet Magnus the dwarf
        print(f"Upon entering, you are met with the familiar sites, sounds and smells of the inn. Scanning the bar\n"
              f"area, you immediately notice the nasty-looking knife, still lodged in the wall. Before you even have\n"
              f"time to react, Lazarus swiftly lands on your shoulder. 'The master awaits you!', he says plainly,\n"
              f"in his smooth tone. Off to your left, Vozzbozz sits in his regular booth, across from a proud-looking\n"
              f"and rather stout dwarf.")
        sleep(1)
        if self.sikira_ally:  # this conditional is actually unnecessary, since Sikira is encountered before this point
            print(f"'Your friends await you.', says Si'Kira with disinterest.\n"  # disinterested means neutral 
                  f"'Join us, will you?', you ask, invitingly, as you gesture to the booth.\n"
                  f"Shaking her head and striding toward the bar she says, 'I choose my own friends.'")
            pause()
            cls()

        print(f"You approach the booth, and as you arrive, Lazarus deftly glides to Vozzbozz' shoulder.")
        pause()
        cls()
        if self.armor.ac > 11:
            print(f"The heavily-armored dwarf looks at you seemingly uninterested and simply says,\n"
                  f"That be some decent {self.armor.name.lower()} ye got there, lad'. He takes a sip of his ale.")
        print(f"The dwarf slides out of the booth and motions that you should take his place. He then slides in next\n"
              f"to Vozzbozz and across from you.\n")
        print(f"'Ah, {self.name}! Meet my good friend, Magnus Stormbringer.', says Vozzbozz curtly. "
              f"The dwarf promptly reaches his\n"
              f"hand across the table and takes yours with a firm, brief grip and a nod.\n"
              f"'Well met', he says, sincerely, in an alarmingly deep voice.")
        pause()
        cls()
        # another meeting, get hints
        teletype_txt_file('hint_event_3.txt')
        pause()
        cls()
        if self.sikira_ally:  # this conditional is actually unnecessary, since Sikira is encountered before this point
            # it just feels right to include it
            teletype(f"'The Dark She-Elf makes five..', interjects the bird.\n"
                     f"Magnus briefly looks at Lazarus, and you suddenly deduce it has been the raven who has been "
                     f"eavesdropping in the dungeon\ndepths below and reporting on your victories all this time.\n"
                     f"Motioning to Si'Kira, he says, 'Ye think yer friend there will lend her sword?'\n" 
                     f"With a smirk, you respond immediately, 'Without a doubt.'\n")

        teletype(f"Magnus looks at you gravely. 'We will be meeting with Tor'Bron outside, and then joining "
                 f"you in the depths presently!'\n"
                 f"'Well then, until we meet again..', you say, draining your mug.\n"
                 f"'Until then!', your companions say in unison as they drink. You rise to your feet and "
                 f"approach the bar.\n")
        pause()
        cls()
        if self.sikira_ally:  # same as above
            print(f"With a tall mug in a smooth, slender hand, Si'Kira remarks, 'That was quick. I have not yet "
                  f"finished my ale!'\nYou ignore the pressing urgency which weighs on you and respond, 'Please, "
                  f"take your time. In fact, I will join you.'\nJenna glides over and slams a mug on the bar. "
                  f"You regard your beautiful companion for a moment,\nand try to ignore the hint of suspicion "
                  f"surrounding her. Thus far she has been a worthy ally,\nbut you remain unsure about completely "
                  f"trusting her.\n"
                  f"She notices you staring, and her prepossessing red eyes light up. You share a drink, and a smile,\n"
                  f"and forget, for a little while..\n")
            pause()
            cls()
        self.boss_hint_3_event = True
        return

    def hint_event_logic(self):
        # called from tavern()
        if self.boss_hint_1 and not self.boss_hint_1_event:
            self.hint_event_1()
            return
        if self.boss_hint_2 and not self.boss_hint_2_event:
            self.hint_event_2()
            return
        if self.boss_hint_3 and not self.boss_hint_3_event:
            self.hint_event_3()
            return

    def jennas_level_1_gab(self, opening_phrase):
        if self.town_portal_exists:
            opening_phrase = f"'Feelin' chatty, love?', queries Jenna in a coy tone.\nI've 'eard ye entered" \
                             f" town through a portal. 'Tis good, sir. 'Cept a word o' caution:\n" \
                             f"Make good use of yer time here while it's open. Ye don't want ta be wastin' yer\n" \
                             f"portals, seein' as scrolls can be rare!"
        teletype(f"{opening_phrase}\n")
        treasure_chest_discovery = f"level {self.dungeon.level} treasure chest"
        if treasure_chest_discovery not in self.discovered_interactives:
            teletype(f"She continues, '{self.dungeon.name} is full of dangers for the "
                     f"unwary,\n"
                     f"but there are treasures to be had as well. 'Tis said that there be a pit below the "
                     f"dungeon\n"
                     f"where ye may find gold, but it be full of monsters, traps, and fiends. Search carefully\n"
                     f"and thoroughly if ye venture there!'\n")
        else:
            teletype(f"With a big, welcoming smile, she says, 'I 'eard it said ye 'ave found treasure in the "
                     f"pit below {self.dungeon.name}!'\n"
                     f"'Care to spend some o' that loot?', she adds with a wink.")

        """micro_boss_discovery = f"level {self.dungeon.level} micro boss"
        if micro_boss_discovery not in self.discovered_interactives:
            teletype(f"Lowering her tone, she goes on, 'I've also 'eard it said that there's an elite enemy\n"
                     f"down there, just waitin' for unsuspectin' adventurers in a dead ended corridor!'\n"
                     f"'Take good care, now, and be wise!'\n")"""
        pause()

    def talk_to_jenna(self):  # expand these statements for immersive realism
        cls()
        opening_phrase = f"'Feelin' chatty, love?', queries Jenna in a coy tone."
        random_jenna_business = [f"'I'm a bit busy, here, love..'\n", f"'There's always loot to be found in the "
                                 "dungeons. Ye can sell what ye don't need, here in town!'\n",
                                 f"'The Sauengard dungeons "
                                 "were once part of a magnificent kingdom many years ago; Before it became overrun "
                                 "by fiends, brigands and the undead.'\n", f"'Working on yer Charisma will give ye a "
                                 "better chance for positive outcomes with monsters!'\n", f"'Gaining Constitution "
                                 f"will help ye resist poison and necrosis.\nIt also will gain ye hit points and "
                                 f"resist paralyzing effects!'\n",
                                 f"'Wisdom is important for procuring the Weirdness fer Quantum effects, and will "
                                 f"become more important as you progress.'\n", f"'Protection from Evil helps ye "
                                 f"resist the Quantum Attacks and Paralyzing effects of monsters.'\n",
                                 f"'Acumen enhances many things, including initiative, melee"
                                 f" attacks, and Quantum Effects.\nAcumen will increase with your experience "
                                 f"level.'\n", f"'I heard about ancient religious altars in the dungeons.\nThey say "
                                 f"ye must be strong if ye plan on demolishing them!'\n"]
        if self.dungeon.level == 1:
            self.jennas_level_1_gab(opening_phrase)
        else:
            teletype(random.choice(random_jenna_business))
            pause()

    def tavern(self):
        # called from town_navigation()
        self.hud()
        print(f"You have come upon the Slumbering Bear Inn- a handsome building with all the trimmings and character\n"
              f"one would expect of a tavern in a town such as this. Above the door hangs an angled sign\n"
              f"with *THE SLUMBERING BEAR* printed above an angry, roaring bear that appears to be "
              f"anything but sleepy...")
        pause()
        # tavern_theme()
        self.hint_event_logic()
        while True:
            self.hud()

            if self.boss_hint_1:
                print(f"(In Town, The Slumbering Bear Inn)")
                print(f"Jenna catches your gaze and nods discreetly. 'Let me know if ye be needin' anything, love.'")

            else:
                print(f"The barroom is bustling as always, but Jenna, the barkeep, notices you and calls over,\n"
                      f"very matter-of-factly, \"What do ye be needin' love?\"")

            inn_choice = input(f"(R)oom for the evening - 10 GP\n(T)alk to Jenna\n(S)ave Character to disk\n"
                               f"(E)xit the inn\n"
                               f"--> ").lower()

            if inn_choice == 'r':

                if self.hit_points < self.maximum_hit_points or self.quantum_units < self.maximum_quantum_units \
                        or self.necrotic or self.poisoned:
                    self.hud()

                    if self.gold >= 10:
                        self.gold -= 10
                        print(f"You find your way to your room, which is upstairs. "
                              f"The accommodations are clean, tidy and welcoming.")
                        sleep(1)
                        print(
                            f"Removing your armor and accoutrements, you wash up and fall into a deep, restful sleep.")
                        sleep(1)
                        print(f"Your body and mind feel better.")
                        sleep(1)

                        if self.hit_points < self.maximum_hit_points:
                            self.hit_points = self.maximum_hit_points
                        self.recover_quantum_energy()
                        self.poisoned = False
                        self.poisoned_turns = 0
                        self.necrotic = False
                        self.necrotic_turns = 0
                        self.potion_of_strength_effect = False
                        self.potion_of_strength_uses = 0
                        self.quantum_strength_effect = False
                        self.quantum_strength_uses = 0
                        self.protection_effect = False
                        self.protection_effect_uses = 0
                        self.end_of_turn_calculation()
                        continue

                    else:
                        print(f"You do not have enough gold!")
                        pause()
                        continue

                else:
                    self.hud()
                    print(f"Jenna chuckles as she shakes her head at you. \"Ye are in the pink, love!\"\n"
                          f"\"What ye be needin' a room fer?\" She hurries off to her busy routines...")
                    sleep(1.5)
                    print(f"You realize she's right! You are in perfect condition!")
                    pause()
                    continue

            elif inn_choice == 't':
                self.hud()
                self.talk_to_jenna()
                continue

            elif inn_choice == 's':
                self.save_character()
                continue

            elif inn_choice == 'e':
                self.hud()
                print(f"You walk out the door, but not before turning to see Jenna's wink and bright smile.\n"
                      f"'Don't be a stranger, now, love! Ye are always welcome!'")
                sleep(1.25)
                pause()
                return

            else:
                continue

    def recover_quantum_energy(self):
        # called from fountain_event() and tavern()
        if self.quantum_units < self.maximum_quantum_units:
            self.quantum_units = self.maximum_quantum_units
            print(f"Your Quantum Energy is restored!")
        else:
            print(f"You are refreshed.")
        pause()
        return

    def drink_antidote(self):
        # called from main loop
        if self.antidotes > 0:
            self.hud()
            if not self.poisoned:
                print(f"You are not poisoned!")
                sleep(1)
                self.hud()
                return False  # false means you do NOT use a turn
            else:
                print(f"You retrieve the amber vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.antidotes -= 1
                self.hud()
                print(f"You feel a vibrant sensation..")
                sleep(1)
                self.poisoned = False
                self.poisoned_turns = 0
                print(f"The poison has left your body..")
                sleep(1)

                pause()
                return True  # True means you DO use a turn
        else:
            print(f"You have no vials of antidote!")
            sleep(1)
            self.hud()
            return False  # False means you do NOT use a turn

    def drink_elixir(self):
        # called from main loop
        if self.elixirs > 0:
            self.hud()
            if not self.necrotic:
                print(f"Your flesh is not corrupted!")
                sleep(1)
                self.hud()
                return False  # false means you do NOT use a turn
            else:
                print(f"You retrieve the emerald vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.elixirs -= 1
                self.hud()
                print(f"You feel a cleansing of the flesh..")
                sleep(1)
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The foul corruption leaves your body..")
                sleep(1)
                pause()
                return True  # True means you DO use a turn
        else:
            print(f"You have no elixirs!")
            sleep(1)
            self.hud()
            # pause()
            return False  # False means you do NOT use a turn

    def drink_healing_potion(self):
        # called from main loop
        self.hud()
        if self.potions_of_healing > 0:

            if self.hit_points >= self.maximum_hit_points:
                print(f"You are already at maximum health!")
                sleep(1)
                self.hud()
                return False  # False means you don't waste a turn
            else:
                print(f"You retrieve the vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.potions_of_healing -= 1
                # number_of_dice = (1 + self.level)
                # heal = dice_roll(number_of_dice, 4) + number_of_dice
                heal = math.ceil(self.maximum_hit_points * .66)
                print(f"You heal {heal} hit points")  # remove after testing
                self.hit_points += heal
                if self.hit_points > self.maximum_hit_points:
                    self.hit_points = self.maximum_hit_points
                self.hud()
                print(f"Your vitality increases.")
                sleep(1)
                pause()
                return True  # True means you use up a turn
        else:
            print("You have no potions of healing!")
            sleep(1)
            self.hud()
            return False  # False means you don't waste a turn

    def duplicate_item(self, item_type, possible_duplicate):
        # check if an item is a duplicate of an item in player's pack:
        duplicate_item_name_lst = []
        inv_dict = Counter(item for item in self.pack[item_type])
        # print(inv_dict)  # for testing
        for key, value in inv_dict.items():
            duplicate_item_name_lst.append(key.name)
        # print(duplicate_item_name_lst)  # for testing
        if possible_duplicate.name in duplicate_item_name_lst or \
                possible_duplicate.name == self.wielded_weapon.name or \
                possible_duplicate.name == self.armor.name or \
                possible_duplicate.name == self.shield.name or \
                possible_duplicate.name == self.boots.name:
            return True
        else:
            return False

    def item_type_inventory(self, item_type):  # list items in inventory by type

        if item_type != 'Town Portal Implements' and item_type != 'Elixirs' \
                and item_type != 'Potions of Strength' and item_type != 'Healing' \
                and item_type != 'Antidotes':  # if item not in belt inventory
            print(f"Your {item_type}:")
            self.pack[item_type].sort(key=lambda x: x.name)
            stuff_dict = Counter(item.name for item in self.pack[item_type])
            for key, value in stuff_dict.items():
                # print(key, ':    ', value, sep='')
                if value > 1:
                    print(value, ' ', key, 's', sep='')
                    # print(key, 's', ':    ', value, sep='')
                else:
                    print(value, ' ', key, sep='')
            number_of_items = len(self.pack[item_type])
            # print(f"You now have {number_of_items} items in your {item_type} inventory.")
            if number_of_items:
                return True
            else:
                # print(f"You currently have no {item_type} in your inventory.")
                return False
        elif item_type == 'Town Portal Implements':
            if self.town_portals > 0:
                print(f"You have {self.town_portals} Scrolls of Town Portal")
                return True
            else:
                print(f"You have no scrolls of town portal.")
                return False
        elif item_type == 'Potions of Strength':
            if self.potions_of_strength > 0:
                print(f"You have {self.potions_of_strength} Potions of Strength")
                return True
            else:
                print(f"You have no Potions of Strength.")
                return False
        elif item_type == 'Healing':
            if self.potions_of_healing > 0:
                print(f"You have {self.potions_of_healing} Potions of Healing")
                return True
            else:
                print(f"You have no potions of healing.")
                return False
        elif item_type == 'Elixirs':
            if self.elixirs > 0:
                print(f"You have {self.elixirs} Clarifying Quantum Elixirs")
                return True
            else:
                print(f"You have no Elixirs.")
                return False
        elif item_type == 'Antidotes':
            if self.antidotes > 0:
                print(f"You have {self.antidotes} Vials of Antidote")
                return True
            else:
                print(f"You have no Vials of Antidote.")
                return False

    def inventory(self):
        self.hud()
        print(
            f"You are wielding: \nA {self.wielded_weapon.name}. Damage bonus: {self.wielded_weapon.damage_bonus}, "
            f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}")
        if self.shield.name != 'No Shield':
            print(f"A {self.shield.name}. Armor class: {self.shield.ac}")
        print(
            f"You are wearing:\n{self.armor.name}. Armor class: {self.armor.ac}, Armor bonus: {self.armor.armor_bonus}")
        print(f"{self.cloak.name}. Stealth: {self.cloak.stealth}")
        if self.ring_of_reg.name != "No Ring of Regeneration":
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != "No Ring of Protection":
            print(f"A Ring of Protection + {self.ring_of_prot.protect} ")
        print(f"On your belt, you are carrying:")
        print(f"A coil of rope")  # like indiana jones and his whip.
        belt = [self.town_portals, self.potions_of_healing, self.potions_of_strength, self.elixirs, self.antidotes]
        if sum(belt) > 0:
            if self.potions_of_strength > 0:
                print(f"{self.potions_of_strength} Potions of Strength")
            if self.potions_of_healing > 0:
                print(f"{self.potions_of_healing} Potions of Healing")
            if self.town_portals > 0:
                print(f"{self.town_portals} Town Portal Scrolls")
            if self.elixirs > 0:
                print(f"{self.elixirs} Clarifying Elixirs")
            if self.antidotes > 0:
                print(f"{self.antidotes} Vials of Antidote")

        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
        print(f"Your pack contains:")  # dungeoneer's pack

        current_items = []
        for each_item in item_type_lst:
            if len(self.pack[each_item]) > 0:
                current_items.append(each_item)
                self.item_type_inventory(each_item)  # call item_type_inventory() for each item in inv.
                # print(current_items)  # for testing
        if not len(current_items):
            print(f"Nothing but cobwebs..")
            pause()
            return
        else:
            pause()
            return

    def found_weapon_substitution(self, found_item):
        if self.wielded_weapon.damage_bonus < (self.level * 2) or self.wielded_weapon.to_hit_bonus < 3:
            # found_item.damage_bonus = self.level
            if found_item.name == self.wielded_weapon.name:
                if self.wielded_weapon.damage_bonus < (self.level * 2):
                    self.wielded_weapon.damage_bonus += 1  # = found_item.damage_bonus + 1
                    print(f"Quantum Weirdness fills the air...\nYour {self.wielded_weapon.name} "
                          f"damage bonus is enhanced to + {self.wielded_weapon.damage_bonus}!")
                    pause()
                    return
                elif self.wielded_weapon.to_hit_bonus < 3:
                    self.wielded_weapon.to_hit_bonus += 1  # = found_item.damage_bonus + 1
                    print(f"Quantum Weirdness fills the air...\nYour {self.wielded_weapon.name} "
                          f"to-hit bonus is enhanced to + {self.wielded_weapon.to_hit_bonus}!")
                    pause()
                    return
            else:
                print(f"You have found {found_item.a_an} {found_item.name}. Damage bonus: {found_item.damage_bonus}. "
                      f"To-hit bonus: {found_item.to_hit_bonus}.")
                print(f"You are currently wielding a {self.wielded_weapon.name}. "
                      f"Damage bonus: {self.wielded_weapon.damage_bonus}. "
                      f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}.")
            while True:
                replace_weapon = input(f"Do you wish to wield the {found_item.name} instead? y/n: ").lower()
                if replace_weapon == 'y':
                    old_weapon = self.wielded_weapon
                    self.wielded_weapon = found_item
                    print(f"You are now wielding the {found_item.name}")
                    print(f"Damage bonus: {self.wielded_weapon.damage_bonus}. "
                          f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}")
                    if not self.duplicate_item(old_weapon.item_type,
                                               old_weapon):  # old_weapon not in self.pack['Weapons']:
                        (self.pack[found_item.item_type]).append(old_weapon)
                        print(f"You place the {old_weapon.name} upon your back..")

                    else:
                        print(f"You drop the {old_weapon.name}.")
                    pause()
                    return
                elif replace_weapon == 'n':
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} on your back.")
                    else:
                        print(f"You choose not to wield the {found_item.name}, but you cannot carry any more weapons "
                              f"of this type. You leave it.")
                    pause()
                    return False
                elif replace_weapon not in ("y", "n"):
                    continue
        else:
            # print(f"Wielded_weapon.damage_bonus already >= self.level * 2 and/or, to-hit == 3!!!")  # rm after testing
            # pause()  # remove after testing
            return

    def found_armor_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if (self.armor.ac + self.armor.armor_bonus) < (found_item.ac + found_item.armor_bonus):
            print(f"You have found {found_item.name}!! Armor Class: {found_item.ac}")
            if self.armor.armor_bonus > 0:
                print(f"Your current {self.armor.name} Armor Class: {self.armor.ac}, Bonus: +{self.armor.armor_bonus}")
            else:
                print(f"Your current {self.armor.name} Armor Class: {self.armor.ac}")

            while True:
                replace_armor = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_armor == 'y':
                    old_armor = self.armor
                    self.armor = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(found_item.item_type, old_armor):
                        (self.pack[found_item.item_type]).append(old_armor)
                        print(f"You place the {old_armor.name} in your pack..")
                    else:
                        print(f"You drop your {old_armor.name}.")
                    pause()
                    return
                elif replace_armor == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type, found_item):
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} in your pack.")

                    else:
                        print(f"However, you cannot carry any more armor of this type. You leave it.")
                    pause()
                    return

                elif replace_armor not in ("y", "n"):
                    continue
        else:
            # print(f"Worn armor ac + armor_bonus >= found item...")  # remove after testing
            # pause()  # remove after testing
            return

    def found_shield_substitution(self, sub_item):
        if self.shield.ac < sub_item.ac:
            print(f"You have found {sub_item.a_an} {sub_item.name}!! Armor Class: {sub_item.ac}")
            if self.shield.name == 'No Shield':
                print(f"You currently hold no shield in your off hand.")
            else:
                print(f"Your current {self.shield.name} Armor Class: {self.shield.ac}")
            while True:
                replace_shield = input(f"Do you wish to wield the {sub_item.name} instead? y/n: ").lower()
                if replace_shield == 'y':
                    old_shield = self.shield
                    self.shield = sub_item
                    print(f"You are now wielding the {sub_item.name}")
                    self.calculate_armor_class()
                    if old_shield.name == 'No Shield':
                        pause()
                        return
                    elif not self.duplicate_item(old_shield.item_type,
                                                 old_shield):  # old_shield not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(old_shield)
                        print(f"You place the {old_shield.name} on your back..")
                    else:
                        print(f"You drop the old {old_shield.name}.")
                    pause()
                    return
                elif replace_shield == 'n':
                    print(f"You choose not to wield the {sub_item.name}.")
                    if not self.duplicate_item(sub_item.item_type,
                                               sub_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(sub_item)
                        print(f"You place the {sub_item.name} on your back.")

                    else:
                        print(f"However, you cannot carry any more shields of this type. You leave it.")
                    pause()
                    return
                elif replace_shield not in ("y", "n"):
                    continue
        else:
            # print(f"Wielded shield >= found item...")  # remove after testing
            # pause()  # remove after testing
            return

    def found_boots_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if self.boots.ac < found_item.ac:
            print(f"You have found a pair of {found_item.name}!! Armor Class: {found_item.ac}")
            print(f"Your current {self.boots.name} Armor Class: {self.boots.ac}")
            while True:
                replace_boots = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_boots == 'y':
                    old_boots = self.boots
                    self.boots = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(old_boots.item_type,
                                               old_boots):  # old_boots not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_boots)
                        print(f"You place the {old_boots.name} in your pack..")  # dungeoneer's pack

                    else:
                        print(f"You drop your {old_boots.name}.")
                    pause()
                    return
                elif replace_boots == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place them in your pack.")  # dungeoneer's pack

                    else:
                        print(f"However, you cannot carry any more boots like this. You leave them.")
                    pause()
                    return
                elif replace_boots not in ("y", "n"):
                    continue
        else:
            # print(f"Worn boots >= found item...")  # remove after testing
            # pause()  # remove after testing
            return

    def found_cloak_substitution(self, found_item):

        if self.cloak.stealth < math.ceil(self.dexterity * .25):
            if found_item.name == self.cloak.name:
                # found_item.stealth += 1
                self.cloak.stealth += 1
                self.calculate_stealth()
                print(f"Quantum Weirdness fills the air...\nYour {self.cloak.name} is enhanced to stealth +"
                      f" {self.cloak.stealth}!")

                pause()
                return
            else:
                print(f"You have found {found_item.a_an} {found_item.name}!! Stealth: {found_item.stealth}")
                print(f"Your current {self.cloak.name} Stealth: {self.cloak.stealth}")
            while True:
                replace_cloak = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_cloak == 'y':
                    old_cloak = self.cloak
                    self.cloak = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_stealth()
                    if not self.duplicate_item(old_cloak.item_type,
                                               old_cloak):  # old_cloak not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_cloak)
                        print(f"You roll up the {old_cloak.name} and place it in your pack..")  # dungeoneer's pack
                    else:
                        print(f"You drop your {old_cloak.name}.")
                    pause()
                    return
                elif replace_cloak == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} in your pack.")  # dungeoneer's pack
                    else:
                        print(f"You cannot carry any more cloaks like this. You leave it.")  # can't carry any more
                    pause()
                    return
                elif replace_cloak not in ("y", "n"):
                    continue
        else:
            # print(f"Stealth already >= .25 * dex...")  # remove after testing
            # pause()  # remove after testing
            return

    def found_ring_of_reg_substitution(self, found_item):

        if self.ring_of_reg.name == "No Ring of Regeneration":
            # self.ring_of_regeneration and default class object has 0 regenerate
            self.ring_of_reg = found_item
            print(f"Quantum Weirdness fills the air...")
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate} appears on your finger!")
            sleep(1)
            print(f"It becomes permanently affixed..fused to your flesh and bone!")
            self.regenerate()  # this is fair. this could save you from poison or necrosis
            pause()
            return

        elif self.ring_of_reg.regenerate < math.ceil(self.maximum_hit_points * .15):
            # old_ring = self.ring_of_reg
            self.ring_of_reg.regenerate = (self.ring_of_reg.regenerate + 1)
            print(f"Quantum Weirdness fills the air...")
            print(f"Your {self.ring_of_reg.name} is enhanced to + {self.ring_of_reg.regenerate} !")
            pause()
            return

        else:
            # print("Ring of reg already equal to or more than 15% of max hit points")  # remove after testing
            # pause()  # remove after testing
            return

    def found_ring_of_prot_substitution(self, found_item):

        if self.ring_of_prot.name == "No Ring of Protection":  # default ring is transparent placeholder
            self.ring_of_prot = found_item
            # (self.pack[found_item.item_type]).append(found_item) you can't sell rings. new rule
            print(f"Quantum Weirdness fills the air...")
            print(f"A Ring of Protection + {self.ring_of_prot.protect} appears on your finger!")
            sleep(1)
            print(f"Tunneling through realities, it permanently fuses to flesh and bone!")
            pause()
            return

        elif self.ring_of_prot.protect < math.ceil(self.wisdom * .20):
            self.ring_of_prot.protect += 1
            print(f"Quantum Weirdness fills the air...")
            print(f"Your {self.ring_of_prot.name} is enhanced to + {self.ring_of_prot.protect} !")
            pause()
            return

        else:
            # print("Ring of prot already equal to or more than 20% of wisdom")  # remove after testing
            # pause()  # remove after testing
            return

    def loot(self):
        # Called from main loop

        if self.encounter < 21:  # regular monster
            loot_difficulty_class = 10
            treasure_chest_difficulty_class = 20
        else:  # boss
            loot_difficulty_class = 8
            treasure_chest_difficulty_class = 16

        # chance to get treasure chest
        possible_treasure_chest = dice_roll(1, 20)
        if self.encounter < 21:  # regular monster
            if possible_treasure_chest >= treasure_chest_difficulty_class:
                self.treasure_chest()
                return  # return after treasure chest for regular monster
        else:  # boss. function then continues to give regular loot after treasure chest
            if possible_treasure_chest >= treasure_chest_difficulty_class:
                self.treasure_chest()

        # regular loot
        loot_dict = top_level_loot_dict
        while True:
            # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
            loot_roll = dice_roll(1, 20)
            self.hud()
            # print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
            # pause()
            # item_class = random.choice(list(loot_dict.keys()))
            # new_item_instance = random.choice(loot_dict[item_class])()  # Calling class __init__ method
            if loot_roll >= loot_difficulty_class:
                key = random.choice(list(loot_dict.keys()))
                # rndm_item_index = random.randrange(len(loot_dict[key]))
                # found_item = loot_dict[key][rndm_item_index]
                found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                # print(found_item)  # REMOVE AFTER TESTING *****************************************************

                if self.level >= found_item.minimum_level:
                    if found_item.item_type == 'Armor':
                        self.found_armor_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Shields':
                        self.found_shield_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Cloaks':
                        self.found_cloak_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Weapons':
                        self.found_weapon_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Regeneration':
                        self.found_ring_of_reg_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Protection':
                        self.found_ring_of_prot_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Boots':
                        self.found_boots_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Town Portal Implements':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.town_portals += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Healing':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_healing += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Potions of Strength':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_strength += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Elixirs':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.elixirs += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Antidotes':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.antidotes += 1
                        pause()
                        continue

                else:
                    # print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                    # pause()  # remove after testing
                    continue
            else:
                # extra chance for potion. this makes it a little too easy. consider restoring it with lower chances
                """extra_chance = dice_roll(1, 20)
                if extra_chance >= 11  # loot_difficulty_class:
                    print(f"You see a potion of healing!")
                    sleep(.5)
                    print(f"You grab it..")
                    self.potions_of_healing += 1
                    pause()
                    # continue
                self.hud()"""
                self.hud()
                return  # self.dungeon_description()

    def treasure_chest(self):
        # called from treasure_chest_event(),
        # also called from from loot()
        successful_tries = 0
        print(f"You see a treasure chest!")
        sleep(1.5)
        gold_roll = dice_roll(1, 20) * self.dungeon.level + 1
        print(f"Inside is {gold_roll} gold pieces!")
        self.gold += gold_roll
        sleep(1.5)
        pause()
        loot_difficulty_class = 7
        loot_dict = top_level_loot_dict
        while True:
            # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
            loot_roll = dice_roll(1, 20)
            self.hud()
            # print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
            # pause()
            if loot_roll >= loot_difficulty_class:
                successful_tries += 1
                key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                # rndm_item_index = random.randrange(len(loot_dict[key]))
                # found_item = loot_dict[key][rndm_item_index]
                found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                # print(found_item)  # REMOVE AFTER TESTING *****************************************************
                if self.level >= found_item.minimum_level:
                    if found_item.item_type == 'Armor':
                        self.found_armor_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Shields':
                        self.found_shield_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Cloaks':
                        self.found_cloak_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Weapons':
                        self.found_weapon_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Regeneration':
                        self.found_ring_of_reg_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Protection':
                        self.found_ring_of_prot_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Boots':
                        self.found_boots_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Town Portal Implements':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.town_portals += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Healing':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_healing += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Potions of Strength':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_strength += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Elixirs':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.elixirs += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Antidotes':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.antidotes += 1
                        pause()
                        continue
                else:
                    # print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                    # pause()  # remove after testing
                    continue
            else:
                if successful_tries == 0:
                    print(f"Besides the gold, there remains nothing but cobwebs...")
                    sleep(1)
                    pause()
                return

    def treasure_chest_event(self):
        # called from event_logic()
        # the treasure_chest_event() is explicitly placed in the dungeon object at specific coordinates.
        # Calls treasure_chest()
        # treasure_chest() can also be called from loot() and awarded after battle
        treasure_chest_discovery = f"level {self.dungeon.level} treasure chest"
        if treasure_chest_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(treasure_chest_discovery)
            return self.treasure_chest()

        else:
            self.dungeon_description()
            print(f"There is an empty treasure chest here.")
            # print(f"An empty treasure chest lies at your feet.")
            pause()
            return

    def quantum_treasure_chest_event(self):
        # called from event_logic()
        # quantum_treasure_chest_event is explicitly placed in the dungeon object at specific coordinates
        successful_tries = 0
        quantum_treasure_chest_discovery = f"level {self.dungeon.level} quantum treasure chest"
        if quantum_treasure_chest_discovery not in self.discovered_interactives:
            print(f"You see a treasure chest with a Quantum lock!")
            sleep(1)
            print(f"You feel dangerous levels of energy surging from it..")
            sleep(1)
            lock_dc = 10
            while True:
                prompt = input("Do you wish to attempt to (U)nlock it with your Quantum knowledge or (I)gnore (U/I): ")
                if prompt == 'i':
                    return
                if prompt == 'u':
                    break
                self.hud()
            quantum_roll = dice_roll(1, 20)
            total = quantum_roll + self.wisdom_modifier
            print(f"Quantum Check Roll: {quantum_roll}")
            sleep(.5)
            print(f"Wisdom Modifier: {self.wisdom_modifier}")
            sleep(.5)
            print(f"Total: {total}")
            sleep(.5)
            print(f"Difficulty Class: {lock_dc}")
            sleep(.5)
            if total >= lock_dc:
                print(f"Success!")
                sleep(1.5)
                gold_roll = (dice_roll(1, 20) * self.dungeon.level) + 1
                print(f"Inside is {gold_roll} gold pieces!")
                self.gold += gold_roll
                sleep(1.5)
                pause()
                loot_difficulty_class = 7
                loot_dict = top_level_loot_dict
                while True:
                    # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ***********
                    loot_roll = dice_roll(1, 20)
                    self.hud()
                    print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
                    pause()
                    if loot_roll >= loot_difficulty_class:
                        successful_tries += 1
                        key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                        # rndm_item_index = random.randrange(len(loot_dict[key]))
                        # found_item = loot_dict[key][rndm_item_index]
                        found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                        # print(found_item)  # REMOVE AFTER TESTING ****************************************************
                        if found_item.minimum_level - self.level <= 2:
                            if found_item.item_type == 'Armor':
                                self.found_armor_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Shields':
                                self.found_shield_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Cloaks':
                                self.found_cloak_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Weapons':
                                self.found_weapon_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Rings of Regeneration':
                                self.found_ring_of_reg_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Rings of Protection':
                                self.found_ring_of_prot_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Boots':
                                self.found_boots_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Town Portal Implements':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.town_portals += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Healing':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.potions_of_healing += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Potions of Strength':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.potions_of_strength += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Elixirs':
                                print(f"You see a {found_item.name}!")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.elixirs += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Antidotes':
                                print(f"You see a {found_item.name}!")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.antidotes += 1
                                pause()
                                continue
                        else:
                            print(f"You see {found_item.a_an} {found_item.name}.")
                            sleep(1)
                            print(f"Even with the Quantum Weirdness of the chest, you are unable to use it.")
                            sleep(1)
                            pause()
                            continue
                    else:
                        # done with loot
                        if successful_tries == 0:
                            print(f"Besides the gold, there remains nothing but cobwebs...")
                            sleep(1)
                            pause()
                        # add chest to discovered interactives list, so it is no longer interactive
                        self.discovered_interactives.append(quantum_treasure_chest_discovery)
                        self.hud()
                        return  # self.dungeon_description()
            else:
                print(f"Your innate Quantum understanding has failed you.")
                sleep(1)
                print(f"You are unable to open the Quantum lock...")
                sleep(1)
                print(f"A wave of Quantum energy shoots toward you!")
                damage = dice_roll(self.level, self.hit_dice)
                self.reduce_health(damage)
                print(f"You suffer {damage} hit points!")
                pause()
                return
        else:
            print(f"There is an empty Quantum treasure chest here.")
            pause()
            return

    def increase_random_ability(self):
        # I was unable to come up with this code on my own.
        # Thanks to Angus Nicolson from Stack Overflow!
        # By editing player.__dict__ directly,
        # or a variable which you derived from it (ability_dict in the code below),
        # you can edit your object's attributes.
        # create a dictionary from self.__dict__
        # Note: Editing ability_dict_subset will not change the object's attributes,
        # because it was made from a dict comprehension.
        # You need to edit self.__dict__ or ability_dict.
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Choose random attribute name
        random_attribute = random.choice(list(ability_dict_subset.keys()))
        print(f"Weird Quantum forces surge through your body..")
        sleep(1.5)
        print(f"You have gained unnatural {random_attribute}!")
        ability_dict[random_attribute] += 1
        self.calculate_modifiers()
        pause()

    def decrease_random_ability(self):
        # I was unable to come up with this code on my own.
        # Thanks to Angus Nicolson from Stack Overflow!
        # By editing player.__dict__ directly,
        # or a variable which you derived from it (ability_dict in the code below),
        # you can edit your object's attributes.
        # create a dictionary from self.__dict__
        # Note: Editing ability_dict_subset will not change the object's attributes,
        # because it was made from a dict comprehension.
        # You need to edit self.__dict__ or ability_dict.
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Choose random attribute name
        random_attribute = random.choice(list(ability_dict_subset.keys()))
        print(f"You feel as though you have been robbed at the most visceral level..")
        sleep(1.5)
        print(f"Your {random_attribute} has dropped!")
        ability_dict[random_attribute] -= 1
        self.calculate_modifiers()
        pause()

    def increase_lowest_ability(self):
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Find the minimum attribute name
        min_attribute = min(ability_dict_subset, key=ability_dict_subset.get)
        print()  # remove after testing
        print(f"Weird sensations surge through your body..")
        sleep(1.5)
        print(f"You have gained {min_attribute}!")
        # Add one to min attribute
        ability_dict[min_attribute] += 1
        self.calculate_modifiers()
        pause()

    def decrease_lowest_ability(self):
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Find the minimum attribute name
        min_attribute = min(ability_dict_subset, key=ability_dict_subset.get)
        # print(min_attribute)  # remove after testing
        print(f"Weird discomfort surges through your body..")
        sleep(1.5)
        print(f"You have lost {min_attribute}!")
        # subtract one from min attribute
        ability_dict[min_attribute] -= 1
        self.calculate_modifiers()
        pause()

    def wicked_queen_event(self):
        # called from event_logic()
        wicked_queen_discovery = f"level {self.dungeon.level} wicked queen"
        if wicked_queen_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(wicked_queen_discovery)
            cls()
            queen_confrontation_theme()
            print_txt_file('queen_splash.txt')
            pause()
            cls()
            teletype_txt_file('queen_confrontation.txt')
            pause()
            return "Wicked Queen"
        else:
            return

    def legendary_monster_event(self):
        # called from event_logic()
        mini_boss_discovery = f"level {self.dungeon.level} mini boss"
        if mini_boss_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(mini_boss_discovery)
            return "Legendary Monster"
        else:
            return

    def elite_monster_event(self):
        # called from event_logic()
        micro_boss_discovery = f"level {self.dungeon.level} micro boss"
        if micro_boss_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(micro_boss_discovery)
            return "Elite Monster"
        else:
            return

    def altar_event(self):
        # called from event_logic()
        altar_demo_exp = self.level * 600
        altar_discovery = f"level {self.dungeon.level} altar"
        if altar_discovery not in self.discovered_interactives:
            rndm_occurrence_lst = [undead_prophet_returns, self.increase_random_ability, self.decrease_random_ability,
                                   undead_prophet_returns, self.increase_lowest_ability,
                                   self.lose_items, undead_prophet_returns, self.heal_event, undead_prophet_returns]
            rndm_occurrence = random.choice(rndm_occurrence_lst)

            rndm_altar_descriptions = ['There is a worn and crumbling altar of stone here. Carved into its\n'
                                       'cold surface are faded symbols from disgusting ancient religions.',
                                       'Here stands an altar of stone which has been abandoned long ago.\n'
                                       'Ancient and horrible religious symbols, now illegible, cover its cold surface.',
                                       'There is a mysterious, ancient, crumbling stone altar here.\n'
                                       'Inscribed upon its surface are countless half-worn\n'
                                       'disgusting symbols left behind by civilizations past.']
            rndm_altar_description = random.choice(rndm_altar_descriptions)
            print(f"{rndm_altar_description}")
            print(f"Along its sides are embedded ornate golden sculptures.")
            print(f"You shudder to think of the innocent lives lost to its many\n"
                  f"horrible false prophets and priests, now long dead.")
            throne_action = input(
                f"(R)emove gold, attempt to (D)emolish the altar, (V)andalize,  or (I)gnore: ").lower()
            if throne_action == 'v':
                print(f"With the hilt of your {self.wielded_weapon.name} you violate the ancient site\n"
                      f"with a bold warning message to any who would dare to revisit such evils upon the world...")
                sleep(1.5)
                print(f"As you finish, you stand to admire your work..")
                pause()
                return rndm_occurrence()
            elif throne_action == 'r':
                difficulty_class = 14
                remove_gold_roll = dice_roll(1, 20)
                if remove_gold_roll + self.intelligence_modifier > difficulty_class:
                    gold_value = (random.randint(7, 10) * self.dungeon.level) * self.acumen
                    print(f"The sculpture comes out, though not without difficulty or damage.")
                    sleep(1)
                    print(f"It is worth {gold_value} GP!")
                    self.gold += gold_value
                    pause()
                    return
                else:
                    return "Undead Prophet"  # undead_prophet_returns()
            elif throne_action == 'd':
                print(f"Removing the hammer from your pack, you begin hacking at the crumbling stone..")
                primary_difficulty_class = 15
                demolish_roll = dice_roll(1, 20)
                if demolish_roll + self.strength_modifier > primary_difficulty_class:  # strength to topple
                    print(f"You succeed in toppling the upper portion!")
                    sleep(1)
                    print(f"Using your rope and timbers from the refuse, you set up rigging.\n"
                          f"Then, with minimal effort, you are able to pull the foundation stones out.")
                    sleep(1.5)
                    print(f"You successfully demolish the altar!")
                    sleep(1.5)
                    self.experience += altar_demo_exp
                    print(f"You gain {altar_demo_exp} experience points!!")
                    self.discovered_interactives.append(altar_discovery)
                    sleep(1.5)
                    pause()
                    self.hud()
                    return self.increase_random_ability()
                else:
                    return "Undead Prophet"  # undead_prophet_returns()

            else:
                return  # ignore the altar
        else:
            print(f"The remains of a demolished ancient altar are here..Who would dare?")
            pause()
            return

    def throne_event(self):
        # because the throne has been stolen and repurposed by many kingdoms, it remains infinitely interactive.
        # however, the gems may only be pried once.
        # throne_discovery = f"level {self.dungeon.level} throne" # uncomment to only allow 1 interaction
        rndm_occurrence_lst = [nothing_happens, king_returns, self.increase_random_ability, self.teleporter_event,
                               nothing_happens, king_returns, self.increase_lowest_ability, self.lose_items,
                               king_returns, nothing_happens, self.heal_event, king_returns,
                               self.decrease_random_ability,
                               self.decrease_lowest_ability]
        rndm_occurrence = random.choice(rndm_occurrence_lst)
        rndm_throne_descriptions = ['There is a magnificent, gem-encrusted throne of gold here. Throughout its\n'
                                    'shimmering surface are countless runes and symbols.',
                                    'In the center of the room stands a majestic throne encrusted with many\n'
                                    'gems and jewels, all laid in gold. Ancient runes cover its glimmering surface.',
                                    'A great, golden throne, replete with many gems and inscribed with countless '
                                    'runes stands here.']
        rndm_throne_description = random.choice(rndm_throne_descriptions)
        print(f"{rndm_throne_description}")
        print(f"Judging by the sheer number of unique origins of the runes, this throne was undoubtedly")
        print(f"stolen from, and reclaimed by many different ancient kings, now long dead.")
        # pause()
        # if throne_discovery not in self.discovered_interactives:  # uncomment to only allow 1 interaction
        throne_action = input(f"(P)ry gems, attempt to (R)ead the Runes, (S)it on the throne or (I)gnore: ").lower()
        if throne_action == 's':
            print(f"You sit on the throne...")
            # self.discovered_interactives.append(throne_discovery)  # uncomment to only allow 1 interaction
            sleep(1.5)
            return rndm_occurrence()

        elif throne_action == 'p':
            gems_pried = f"level {self.dungeon.level} gems pried from throne"
            if gems_pried not in self.discovered_interactives:
                difficulty_class = 12
                pry_roll = dice_roll(1, 20)
                if pry_roll > difficulty_class:
                    gem_value = (random.randint(7, 15) * self.dungeon.level) * self.acumen
                    print(f"They pop out into your greedy hands!")
                    sleep(1.5)
                    print(f"They are worth {gem_value} GP!")
                    self.gold += gem_value
                    self.discovered_interactives.append(gems_pried)
                    pause()
                    return
                else:
                    return "King Boss"  # king_returns()
            else:
                print(f"There are no gems left to pry...")
                pause()
        elif throne_action == 'r':
            rune_experience = self.level * 700
            difficulty_class = 15
            read_roll = dice_roll(1, 20)
            if read_roll + self.wisdom_modifier > difficulty_class:  # wisdom to recognize language
                print(f"You recognize the ancient language!")
                sleep(1)
                translate = input(f"Do you want to attempt to translate it into the common tongue? (y/n)? ").lower()
                if translate == 'y':
                    difficulty_class = 8
                    translate_roll = dice_roll(1, 20)
                    if translate_roll + self.intelligence_modifier > difficulty_class:  # intelligence to translate
                        rndm_ancient_wisdom = ["Do not withhold good from those to whom you should give it\n"
                                               "If it is within your power to help.",
                                               "Do not plot harm against your "
                                               "neighbor when he lives in a sense of security with you.",
                                               "The wise will inherit honor, but the stupid ones glorify "
                                               "dishonor.",
                                               "Do not enter the path of the wicked, and do not walk in "
                                               "the way of evil men.\nShun it, do not take it; "
                                               "Turn away from it, and pass it by.",
                                               "The way of the wicked is like "
                                               "the darkness;\nThey do not know what makes them stumble.",
                                               "Above all the things that you guard, safeguard your heart, "
                                               "For out of it are the sources of life.",
                                               "Drink water from your own "
                                               "cistern\nAnd flowing water from your own well."]
                        rndm_wisdom = random.choice(rndm_ancient_wisdom)
                        print(f"The literal translation is, '{rndm_wisdom}...'")
                        sleep(1.5)
                        self.experience += rune_experience
                        print(f"You gain {rune_experience} experience points!!")
                        sleep(1.5)
                        pause()
                        self.loot()
                        return self.increase_random_ability()
                    else:
                        return "King Boss"  # king_returns()  # unable to translate
                else:
                    return  # player chooses not to translate
            else:
                return "King Boss"  # king_returns()  # player unable to recognize runes
        else:
            return  # ignore the throne

    def heal_event(self):
        # healing event called from fountain
        hit_point_overage = ((6 * self.dungeon.level) + 1)
        print(f"You feel vitality bubbling up within you...")
        sleep(1.5)
        if self.poisoned or self.necrotic:
            print(f"Your flesh no longer crawls with agony..")
            sleep(1)
            self.poisoned = False
            self.poisoned_turns = 0
            self.necrotic = False
            self.necrotic_turns = 0
            print(f"The foul corruption leaves your body..")
            sleep(1)
        if self.hit_points < self.maximum_hit_points:
            print(f"The restorative powers heal you to full strength!")
            sleep(1)
            self.hit_points = self.maximum_hit_points
        else:
            self.hit_points += hit_point_overage
            print(f"Your hit points have been unnaturally raised to {self.hit_points}!")
            sleep(1)
            print(f"You wonder how long this advantage will last..")
            sleep(1)
        pause()
        return

    def lose_items(self):
        # pack items get lost first, then if belt_items_to_lose sum > 0, belt items get lost
        belt_item_types_to_lose = [self.potions_of_strength, self.potions_of_healing,
                                   self.town_portals, self.elixirs, self.antidotes]
        available_item_types_to_lose = []
        for i in self.pack.keys():  # gather all available
            if len(self.pack[i]) > 0:  # item types to lose based on player's current item TYPES and put them
                available_item_types_to_lose.append(i)  # in available_item_types_to_lose = []
        if len(available_item_types_to_lose) > 0:
            item_type = random.choice(available_item_types_to_lose)  # Get random item *TYPE* you want to "steal"
            if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type"
                # pop random item from that item type. -1 because indexes start at 0
                lost_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                print(f"Your load feels lighter..")
                sleep(1)
                print(f"The {lost_item.name} from your pack is gone!")  # from your {item_type}")  # dungeoneer's pack
                pause()
                return
        elif sum(belt_item_types_to_lose) > 0:

            item_string = ""
            # Define list of attributes you are allowed to change
            self_dict = self.__dict__  # create variable as actual copy of player dict attribute
            stealing_lst = []
            # the working dict and 'for' loop just takes the place of many 'if:' statements
            working_dict = {'potions_of_strength': self.potions_of_strength,
                            'potions_of_healing': self.potions_of_healing,
                            'town_portals': self.town_portals, 'elixirs': self.elixirs,
                            'antidotes': self.antidotes}
            # add all items > 0 in working dict to stealing list
            for key, value in working_dict.items():
                if value > 0:
                    stealing_lst.append(key)
            random_stolen_item = random.choice(stealing_lst)
            # I am proud of this next bit of code :)
            grammar_dict = {'potions_of_strength': 'potion of strength',
                            'potions_of_healing': 'potion of healing',
                            'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir',
                            'antidotes': 'vial of antidote'}
            for key, value in grammar_dict.items():
                if random_stolen_item == key:
                    item_string = value
            print(f"Your load feels lighter...")
            sleep(1)
            print(f"A {item_string} has disappeared from your belt!")
            self_dict[random_stolen_item] -= 1
            pause()
            return
        else:
            return nothing_happens()  # pack and belt inventory empty

    def fountain_event(self):
        # WHITE GREEN CLEAR RED BLACK
        # Telengard has these 5 random events:
        # heal 3 * dungeon level + 1 hit points
        # poison 3 * dungeon level + 1 hit points
        # drunk
        # lose items
        # increase num of spells: Magic power SURGES through your body
        water_colors = ['white', 'green', 'bright green ', 'crystal clear',
                        'deep red', 'red', 'black', 'pitch black']
        water_color = random.choice(water_colors)
        print(f"A fountain flowing with {water_color} water is here.")
        sleep(1)
        print(f"The tranquil sound eases your mind.")
        sleep(1)
        drink = input(f"Do you wish to drink? ").lower()
        if drink == 'y':
            random_occurrence_list = [nothing_happens, self.recover_quantum_energy, self.poison_ingestion,
                                      self.increase_random_ability, self.lose_items, self.decrease_random_ability,
                                      self.increase_lowest_ability, self.heal_event, nothing_happens,
                                      self.decrease_lowest_ability]
            random_occurrence = random.choice(random_occurrence_list)
            random_occurrence()
        else:
            print("Ignore.")
            sleep(.25)
            return

    def teleporter_event(self):
        print(f"Zzzzzzap....You've been teleported.....")
        sleep(2)
        # self.dungeon_key += 1  # this will become random.randint(1, deepest dungeon level) in future
        # self.dungeon = dungeon_dict[self.dungeon_key]
        # self.x = random.randint(1, 18)
        # self.y = random.randint(1, 18)
        (self.x, self.y) = self.dungeon.teleporter_landing
        self.coordinates = (self.x, self.y)
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = self.dungeon.grid[self.y][self.x]
        pause()
        self.hud()
        return

    def pit_event(self):
        # falling into pits lands you at the dungeon.pit_landing coordinates
        print(f"The ground here is slippery, and quite unsteady..")
        sleep(1.5)
        print(f"You see a pit..")
        sleep(1.5)
        pit_difficulty_class = 9
        pit_outcome = dice_roll(1, 20)
        if (pit_outcome + self.dexterity_modifier + self.intelligence_modifier) > pit_difficulty_class:
            print(f"It appears to be about 3 fathoms deep.")
            sleep(1)
            descend_or_not = input(f"Do you wish to descend (y/n)? ").lower()
            if descend_or_not == 'y':
                self.in_a_pit = True
                print(f"Retrieving the rope from your belt, you deftly repel down the slick, "
                      f"treacherous pit walls.")
                # self.dungeon_key += 1
                # self.dungeon = dungeon_dict[self.dungeon_key]
                (self.x, self.y) = self.dungeon.pit_landing
                self.coordinates = (self.x, self.y)  # beta self.dungeon.pit_landing
                self.previous_x = self.x
                self.previous_y = self.y
                self.position = self.dungeon.grid[self.y][self.x]
                pause()
                self.hud()
                print(f"You have landed at the bottom of a pit. The foul, humid air hangs in a mist around you.")
                # print(self.dungeon.pit_intro)
                self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
                pause()
                return
            else:
                return
        else:
            print(f"The ground beneath your feet collapses!")
            sleep(1)
            # print(f"Desperately, you grope for a crag!")
            # sleep(1)
            # removed this code. now, either you fall in or you don't
            # if dice_roll(1, 20) >= 15:
            #    print(f"You succeed!")
            #    pause()
            #    return
            # else:
            self.in_a_pit = True
            print(f"You fall in!")
            damage = dice_roll(1, (3 * self.dungeon.level))  # dice_roll(1, self.dungeon.level)
            self.hit_points -= damage
            sleep(1)
            print(f"You suffer {damage} hit points..")
            sleep(1)
            pause()
            # falling into pits lands you on the same dungeon level, at the dungeon.pit_landing coordinates
            # self.dungeon_key += 1  # this can be used to land you on the next level down
            # self.dungeon = dungeon_dict[self.dungeon_key]  # this can be used to land you on the next level down
            (self.x, self.y) = self.dungeon.pit_landing
            self.coordinates = (self.x, self.y)  # beta
            self.previous_x = self.x
            self.previous_y = self.y
            self.position = self.dungeon.grid[self.y][self.x]
            self.hud()
            print(f"You have landed at the bottom of the pit. The foul, humid air hangs in a mist around you.")
            # print(self.dungeon.pit_intro)
            self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
            pause()
            return

    def staircase_description(self):
        # called from dungeon_description()
        # this is a 'description' of the spiral staircase, if player navigates to it *after* the map is initialized
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"The spiral staircase entrance to {self.dungeon.name} is here.")
        if self.dungeon.level > 1:
            previous_place = f"dungeon level {self.dungeon.level - 1}"
        else:
            previous_place = f"the Dark Mountain entrance"
        print(f"The stairs lead up to {previous_place}. However, there is no returning;\n"
              f"The door has been locked and barricaded. You must continue onward!")

    def pit_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the pit landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"High above you is a wide, gaping hole leading up to "
              f"{self.dungeon.name}.")

    def deaf_one_fog_remnant_description(self):
        # called from dungeon_description()
        # a description of the area where deaf one was, if he has been discovered on current dungeon level
        deaf_one_discovery = f"level {self.dungeon.level} deaf_one"
        if deaf_one_discovery in self.discovered_interactives:
            print(f"There is a lingering remnant of fog and a marshy smell here.")

    def elevator_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the elevator landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        # print(f"Mechanical Landing, {self.dungeon.name}")
        print(f"There is a landing for a mechanical contraption of ropes, pulleys and counterweights here.")
        print(f"The base is covered in an iron mesh, allowing the horribly foul air from deep below\n"
              f"{self.dungeon.casual_name} to escape to this level.")

    def teleporter_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the teleporter landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"The floor of {self.dungeon.name} has been scorched here, and there is a subtle, but discernible\n"
              f"bowl shape, about 3 yards across, which seems to have been perfectly carved from it.")

    def elevator_event(self):
        # elevators bring you 'up' from pits to main dungeon level: self.dungeon.elevator_landing
        # self.in_a_pit will be false at end of function
        # player must pass intelligence protection roll
        print(f"You feel a slight whirring..")
        sleep(1)
        difficulty_class = 9
        if dice_roll(1, 20) + self.intelligence_modifier >= difficulty_class:
            stay_or_jump = input(f"You see an elevation mechanism which can return you to the "
                                 f"main dungeon level.\nDo you wish to go back (U)p, or "
                                 f"(S)tay to explore this level further? ").lower()
            if stay_or_jump == 'u':
                print(f"A cage closes on your position.")
                sleep(1)
                print(f"You feel heavy for a moment..")
                sleep(2)
                self.hud()
                self.in_a_pit = False
                # self.dungeon_key -= 1  # this can be used for more powerful elevator, perhaps at advanced levels
                # self.dungeon = dungeon_dict[self.dungeon_key]  # when player has more experience?
                (self.x, self.y) = self.dungeon.elevator_landing
                self.coordinates = (self.x, self.y)
                self.previous_x = self.x
                self.previous_y = self.y
                self.position = self.dungeon.grid[self.y][self.x]
                print(f"You have arrived back at {self.dungeon.name}, dungeon level {self.dungeon.level}.")
                sleep(1)
                self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
                print(f"Watch your step.")
                sleep(1)
                pause()
                return
            else:
                return
        else:
            print(f"A cage closes upon you!")  # intelligence not enough to realize what is happening.
            sleep(1)
            print(f"You are being drawn upward!")
            sleep(2)
            self.hud()
            # self.dungeon_key -= 1
            # self.dungeon = dungeon_dict[self.dungeon_key]
            print(f"You have arrived back at {self.dungeon.name}, dungeon level {self.dungeon.level}.")
            sleep(2)
            self.in_a_pit = False
            (self.x, self.y) = self.dungeon.elevator_landing
            self.coordinates = (self.x, self.y)
            self.previous_x = self.x
            self.previous_y = self.y
            self.position = self.dungeon.grid[self.y][self.x]
            print(f"Watch your step.")
            sleep(1)
            self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
            pause()
            return

    def npc_defeats_monster_logic(self, monster, damage):
        # called from npc_attack_logic() to discern if npc defeats monster, and
        # monster dies mid-party-turn
        monster.reduce_health(damage)
        if monster.check_dead():
            self.hud()
            if self.encounter > 20:  # if fighting boss
                gong()
                if monster.proper_name != "None":
                    print(f"The party has vanquished {monster.proper_name}! "
                          f"You are victorious!")
                    self.vanquished_foes.append(monster.proper_name)
                else:
                    print(f"The party has vanquished the {monster.name}!")
                sleep(4)
                self.dungeon_theme()
            else:
                print(f"The party has defeated the {monster.name}..")

            return True
        else:
            return False

    def npc_attack_logic(self, monster):
        # called from main loop after player quantum or melee attack (or potion)
        if self.sikira_ally or self.vozzbozz_ally or self.torbron_ally or self.magnus_ally:
            victory = False
            if self.sikira_ally:
                if not self.sikira.retreating:
                    ally_dmg1 = self.npc_melee(self.sikira, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg1):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.torbron_ally:
                if not self.torbron.retreating:
                    ally_dmg2 = self.npc_melee(self.torbron, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg2):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.magnus_ally:
                if not self.magnus.retreating:
                    ally_dmg3 = self.npc_melee(self.magnus, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg3):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.vozzbozz_ally:
                if not self.vozzbozz.retreating:
                    ally_dmg4 = self.vozzbozz_attack(monster)
                    if self.npc_defeats_monster_logic(monster, ally_dmg4):
                        victory = True
                        return victory
                    else:
                        victory = False

            return victory

        else:  # player has no NPC allies
            return

    def encounter_deaf_one_event1(self):
        # called from event_logic()
        deaf_one_discovery = f"level {self.dungeon.level} deaf_one"
        random_orientation_lst = ["north", "south", "east", "west"]
        random_orientation = random.choice(random_orientation_lst)
        if deaf_one_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(deaf_one_discovery)
            self.hud()
            teletype(f"From the {random_orientation}, a seemingly autonomous, marshy, and knee-deep fog stretches "
                     f"toward you from out of the mire\nas a dark, humanoid silhouette begins to emerge. "
                     f"You behold his elongated, troll-like nose and ears, and deep-set eyes\nshrouded in black, "
                     f"the whites of which shine with a luminescence as brilliant as any moon you have ever beheld. "
                     f"\nHis garb is a mere patchwork of cloth strip wrappings, as though he were once "
                     f"mummified. His exposed portions\nof flesh appear gray and lifeless, with arms covered in "
                     f"tattoo markings, and his long, dark hair is a tangled mess.\n")
            pause()
            self.hud()
            teletype(f"Drawing your {self.wielded_weapon.name}, you attack!\n")
            pause()
            self.hud()
            teletype(f"Your weapon strikes his left arm and splinters into shards of white-hot steel! Unaffected and "
                     f"dismissive, he opens his palm,\nand your {self.wielded_weapon.name} re-appears, completely "
                     f"restored! He hands it to you with a nod.\n")
            pause()
            self.hud()
            teletype(f"'Be at ease, {self.name}.', he says in a smooth, even tone. 'I am not an enemy, and I cannot "
                     f"be harmed by such weapons.'\n'Who are you?', you insist.\nHe regards your question for a brief "
                     f"moment before saying, 'You may call me Deaf One'.\n'Deaf One?', You blurt out, almost "
                     f"involuntarily.\nWith a nod, he answers in a subdued, faraway voice, 'Though hearing, I hear "
                     f"in vain..'\nStill on your guard, yet feeling powerless in contrast to his obvious "
                     f"invulnerability, you begin to explain your quest.\n'Yes, I know why *you* are here.', "
                     f"he interrupts, plainly. "
                     f"'*I* am here', he pauses, 'to guide you. The exit of this dungeon is guarded\nby an enemy whom "
                     f"you are not yet prepared to face.'\n")
            pause()
            self.hud()
            teletype(f"Thinking back to your training, you recall Gorndam's words and warnings about physical power "
                     f"and its limitations in the face\nof mighty foes.\n'Your teacher was correct', Deaf one states "
                     f"with inexplicable context and knowledge, 'you must pursue and hone your innane\n"
                     f"understanding of the Quantum nature of our world.'\n")
            pause()
            self.hud()
            teletype(f"'Is it not too late for training, now that I am here?', you ask.\nPatiently, he responds, "
                     f"'I will ask you to simply ponder this question. Ask yourself, is Uncertainty essentially\n"
                     f"ontological, or, epistemological?'\n'Ontological..?', you begin.\n'Yes, is "
                     f"Quantum Uncertainty simply a feature of our reality, rather than a reflection\nof the "
                     f"limitations of our knowledge, or is it epistemological; fundamentally due to our own "
                     f"Uncertainty of Quantum Nature?'\n")
            pause()
            self.hud()
            teletype(f"'That is quite a concept to ponder..', you respond, rather incredulously.\n"
                     f"'Indeed.', he says, 'This question is at the heart of your advancement. It is the concept "
                     f"which will either\nfacilitate or prevent your comprehension of Weirdness.'\n'It is the principle"
                     f" which must be embraced, and never understood.', he concludes."
                     f"\nBefore you can respond with the myriad of "
                     f"questions in your mind, the marshy fog envelopes Deaf One,\nand his form becomes "
                     f"obscured with its whisperings until he is simply gone. All that remains is the cold, "
                     f"creeping mist.\n")
            pause()
            if self.hit_points < self.maximum_hit_points:
                self.hud()
                teletype(f"The remnants of the low-lying fog pulse with Weirdness...")
                sleep(1.5)
                self.heal_event()
            return

    def encounter_deaf_one_event2(self):
        # called from event_logic()
        deaf_one_discovery = f"level {self.dungeon.level} deaf_one"
        random_orientation_lst = ["north", "south", "east", "west"]
        random_orientation = random.choice(random_orientation_lst)
        if deaf_one_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(deaf_one_discovery)
            cls()
            teletype(f"From the {random_orientation}, a seemingly autonomous, marshy, and knee-deep fog stretches "
                     f"toward you.\nFrom out of the mire, Deaf One emerges and approaches you!\n")
            pause()
            cls()
            allies = []
            if self.sikira_ally:
                allies.append("Si'Kira")
            if self.magnus_ally:
                allies.append("Magnus")
            if self.torbron_ally:
                allies.append("Tor'bron")
            if self.vozzbozz_ally:
                allies.append("Vozzbozz")

            if len(allies):
                if len(allies) > 1:
                    teletype(f"With nearly perfectly synchronized actions, your allies ready themselves toward the "
                             f"perceived threat,\nas Deaf One remains perfectly still, relaxed, and disaffected.\n"
                             f"'Peace, my friends! Peace!', you cry out, while gesturing to the party to calm "
                             f"themselves.\n'He is not an enemy!'\nDeaf One nods, and you detect the hint of a smile "
                             f"forming on his gray flesh.")

            teletype(f"'Quite a journey it has been for you, {self.name}.', he begins in his smooth, even tone, "
                     f"his voice filling your mind, and the space around you.\n'Your adversary awaits at the end of "
                     f"this artery, to the east.', he says.\nThen, with genuine curiosity, he adds, "
                     f"'I have watched your progress with satisfaction. Have you pondered my question?'\n"
                     f"'I have', you say plainly.\n'And?' he queries.\n"
                     f"'And, the answer is; Yes. Quantum Uncertainty is either a feature of our reality, or a "
                     f"refection of the limitations of our knowledge.'\nA wide, toothy grin grows over his undying "
                     f"face. 'That is a good answer..', he says with sincerity.\nThen, his smile fades and is "
                     f"replaced with solemnity. '..but not the only answer!'\nHe smiles again and turns to leave.\n"
                     f"'Wait!' you call out impulsively. 'Will we ever meet again?', you ask.\n'Yes.', he says, "
                     f"pausing to turn over his shoulder. '*That* I can say with certainty.', he adds, with a cryptic "
                     f"narrowing of his eyes.\n")
            pause()
            cls()
            teletype(f"The marshy fog begins to envelope Deaf One, until his form becomes obscured and he is simply "
                     f"gone, along with the cold, creeping mist.\n")
            pause()
            if self.hit_points < self.maximum_hit_points:
                self.hud()
                teletype(f"The remnants of the low-lying fog pulse with Weirdness...")
                sleep(1.5)
                self.heal_event()
            return

    def encounter_the_party_event(self):
        # called from event_logic()
        party_discovery = f"level {self.dungeon.level} party_encounter"
        if party_discovery not in self.discovered_interactives:
            cls()
            self.discovered_interactives.append(party_discovery)
            self.torbron_ally = True
            self.magnus_ally = True
            self.vozzbozz_ally = True
            teletype(f"Due east, you see a group of 3 adventurers whom you immediately recognize. 'My friends!' "
                     f"you cry aloud.\n"
                     f"Tor'Bron, Magnus and Vozzbozz approach, and against the ominous backdrop and setting, "
                     f"you find new respect for their imposing appearance.\n'Well met, {self.name}.', states Vozzbozz "
                     f"plainly. 'And I speak for us all when I say you are a welcome ally, Si'Kira!', he adds.\n")
            pause()
            cls()
            teletype_txt_file('encounter_the_party.txt')
            pause()
            cls()

    def encounter_sikira_event(self):
        # called from event_logic()
        ally_discovery = f"level {self.dungeon.level} ally"
        rndm_orientation_lst = ["left", "right", "rear"]
        rndm_orientation = random.choice(rndm_orientation_lst)
        if ally_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(ally_discovery)
            # this is really an unnecessary check, but I decided to include it
            # just in case I forget to make level 21 monsters.
            if self.level < 20:
                monster_key = (self.level + 1)
            else:
                monster_key = self.level
            monster_cls = random.choice(monster_dict[monster_key])
            monster = monster_cls()
            self.hud()
            print(f"You see a beautiful Elven warrior here, battling an especially fierce {monster.name}.")
            print(f"Instinctively, you ready your {self.wielded_weapon.name} and rush to help.")
            print(f"The {monster.name} strikes at her wickedly, but she nimbly springs back, just out of reach.\n"
                  f"Noticing you, she motions to the {monster.name}'s {rndm_orientation} with a subtle twitch\n"
                  f"of her head, as she strikes back with her glorious, finely crafted sword.")
            pause()
            self.hud()
            print(f"Moving to the {monster.name}'s {rndm_orientation}, as directed, the {monster.name} suddenly"
                  f" senses your presence!\n"
                  f"{monster.attack_5_phrase}")
            print(f"The distraction serves as a perfect opportunity for attack, as she swings her great blade from\n"
                  f"a blind angle, felling her enemy with a single, precise cut. The {monster.name} falls dead\n"
                  f"without ever realizing it was in danger.")
            print(f"Placing your {self.wielded_weapon.name} on your back, you extend a hand. You remember a greeting\n"
                  f"that elves who visited Tinbar appreciated, and say, Well met, illuminated one!'.")
            pause()
            self.hud()
            print(f"You immediately sense a shift in the air. The petite warrior's alabaster countenance falls to\n"
                  f"a twisted grimace and her crimson eyes burn with hate. Her blade is at your throat before you\n"
                  f"can even react. 'What did ye call me?' she queries in a beautifully perfect voice, smoother\n"
                  f"than oil.")
            pause()
            self.hud()
            print(f"'Forgive me, friend!', you manage to respond. 'It was meant with deep respect! It is how\n"
                  f"Elf-kind enjoy being greeted where I am from!..'")
            print(f"'I AM NOT OF-THE-LIGHT!', she asserts, directly into your face. "
                  f"Your disarmed look speaks to your\n"
                  f"confusion, and she responds, 'And I have no need of your assistance, nor of\n"
                  f"your life!' You feel her blade move within a hair's breadth of your throat.")
            pause()
            self.hud()
            print(f"Again you plead, 'Please forgive my ignorance. I am from a far-off land. My name is {self.name}\n"
                  f"of Tinbar! My people and the Northern Library have all been destroyed by a terrible evil that\n"
                  f"I have been sent to seek out and destroy...she bears the mark of a crowned woman surrounded\n"
                  f"by skulls!'")
            pause()
            self.hud()
            print(f"Her face and mood again shift, and she removes her blade and begins to smile! It is then that you\n"
                  f"begin to notice the signs you missed earlier; Her teeth- black and smooth as raven's claws,\n"
                  f"tiny fangs, deep red eyes and her unusually petite, yet athletic build. But how could a Dark "
                  f"Elf have\n"
                  f"such a pale complexion, you wonder silently...Are they not grey-skinned?")
            pause()
            cls()
            print_txt_file('sikira.txt')
            pause()
            self.hud()
            print(f"'Well. {self.name} of Tinbar, well met!', she says with an evil chuckle. 'I am Si'Kira,\n"
                  f"Child of the Waning Moon. My people too, have all been slain. I also seek to destroy the\n"
                  f"wicked Queen Jannbrielle.'. She sheathes her blade, and her long silver hair glistens gorgeously\n"
                  f"in the darkness, as does her wondrous weaponry and armor.")
            pause()
            self.hud()
            print(f"'Queen Jannbrielle..', you repeat thoughtfully. Si'Kira looks at you as you say the name.\n"
                  f"'I have met allies above who dare not even utter that word, and at last I learn it...'\n"
                  f"'Thank you for finally revealing the name of our common enemy, my good Elf-of-the-darkness!' "
                  f"you say with\n"
                  f"a hint of humor.")
            pause()
            self.hud()
            print(f"Si'Kira laughs gleefully again. 'This is most interesting!', she says, with sincere intrigue\n"
                  f"in her voice, and visible excitement in her eyes. 'How odd that our paths cross in such a "
                  f"way..and in such a place! I shall\n"
                  f"'be accompanying you, {self.name} of Tinbar! For good or ill, we are bound in purpose and\n"
                  f"outcome.'")
            pause()
            self.hud()
            print(f"'I suppose..that settles it..?', you say somewhat ironically.\n"
                  f"'Aye. It does.', says Si'Kira, plainly.")
            pause()
            self.hud()
            print(f"You cannot help but wish that you had a voice in the matter; Dark Elves are notoriously "
                  f"duplicitous, and\nvery clever, but you trust your instincts and move on, together.")
            self.sikira_ally = True
            pause()
        else:
            return

    def deaf_one_forced_portal_conditionals(self):
        # called from self.deaf_one_portal_dungeon_levelX_event() methods below
        # sets conditions checked elsewhere
        self.forced_portal = True  # checked in town_navigation()
        cls()
        teletype(f"A portal opens before you; Strange, erratic, and "
                 f"pulsating with incredible power\nthat you feel in your bones. Within the Weird "
                 f"opening, you see Deaf One, silently standing in front\nof the Slumbering Bear Inn! "
                 f"He beckons you with a gesture to join him. Instinctively, you step through to find\n"
                 f"him vanished in an instant..\n")
        pause()
        town_theme()
        self.in_town = True  # checked in main loop, to break out of dungeon loops and remain in town loop
        self.in_dungeon = False  # checked in main loop to break out of dungeon loops
        self.town_portal_exists = True  # checked to ensure proper prompt to enter or re-enter dungeon

    def deaf_one_portal_dungeon_level2_event(self):
        # called from self.event_logic()
        # on dungeon level 2, force player to tavern to trigger boss_hint_1_event if not done so already
        # to move story along.
        if not self.boss_hint_1_event:
            self.deaf_one_forced_portal_conditionals()
            return "DeafOnePortal"

    def deaf_one_portal_dungeon_level3_event(self):
        # called from self.event_logic()
        # on dungeon level 3, force player to tavern to trigger boss_hint_2_event if not done so already
        # to move story along
        if not self.boss_hint_2_event:
            self.deaf_one_forced_portal_conditionals()
            return "DeafOnePortal"

    def deaf_one_portal_dungeon_level4_event(self):
        # called from self.event_logic()
        # on dungeon level 4, force player to tavern to trigger boss_hint_3_event if not done so already
        # because, otherwise the party members will just show up without explanation
        if not self.boss_hint_3_event:
            self.deaf_one_forced_portal_conditionals()
            return "DeafOnePortal"

    def event_logic(self):
        # interactive events, items etc.
        # the event dictionary *key* is a tuple trigger corresponding to
        # dungeon x y coordinates of an event or item e.g. (2, 3)
        # the event dictionary *value* is the corresponding player function/event.
        # if the player's coordinates exist as a key in event_dict,
        # the dictionary value is given the variable 'event_function'
        # finally, the proper function (method) is called and any
        # function values are returned to the main program
        # using 'return event_function()'
        # monster_encounter = dice_roll(1, 20)
        self.coordinates = (self.x, self.y)
        event_dict = {self.dungeon.quantum_treasure_chest: self.quantum_treasure_chest_event,
                      self.dungeon.encounter_sikira: self.encounter_sikira_event,
                      self.dungeon.encounter_deaf_one_1: self.encounter_deaf_one_event1,
                      self.dungeon.encounter_deaf_one_2: self.encounter_deaf_one_event2,
                      self.dungeon.deaf_one_portal_dungeon_level2: self.deaf_one_portal_dungeon_level2_event,
                      self.dungeon.deaf_one_portal_dungeon_level3: self.deaf_one_portal_dungeon_level3_event,
                      self.dungeon.deaf_one_portal_dungeon_level4: self.deaf_one_portal_dungeon_level4_event,
                      self.dungeon.encounter_the_party: self.encounter_the_party_event,
                      self.dungeon.treasure_chest: self.treasure_chest_event,
                      self.dungeon.altar: self.altar_event,
                      self.dungeon.throne: self.throne_event,
                      self.dungeon.fountain: self.fountain_event,
                      self.dungeon.teleporter: self.teleporter_event,
                      self.dungeon.elevator: self.elevator_event,
                      self.dungeon.pit: self.pit_event,
                      self.dungeon.elite_monster: self.elite_monster_event,
                      self.dungeon.legendary_monster: self.legendary_monster_event,
                      self.dungeon.wicked_queen: self.wicked_queen_event,
                      self.dungeon.exit: self.dungeon_exit_event
                      }
        if self.coordinates in event_dict.keys():
            event_function = (event_dict[self.coordinates])  # (event_dict[self.coordinates])
            return event_function()
        else:
            return

        # NAVIGATION

    def town_navigation(self):
        # called from main loop
        if self.forced_portal:
            # if self.boss_hint_3 and not self.boss_hint_3_event:  # if player defeats level 3 exit boss and has not yet
            self.forced_portal = False  # reset forced portal condition
            tavern_theme()  # visited tavern, then player automatically placed at tavern
            self.tavern()
            town_theme()
        if self.town_portal_exists:  # or self.loaded_game:
            town_functions = input("(The Town of Fieldenberg)\n(Quit) to desktop, (R)estart game (I)nventory, "
                                   "(B)lacksmith, (C)hemist , (T)avern, or re-(E)nter dungeon --> ").lower()
        else:
            town_functions = input("(The Town of Fieldenberg)\n(Quit) to desktop, (R)estart game (I)nventory, "
                                   "(B)lacksmith, (C)hemist , (T)avern, or (E)nter dungeon --> ").lower()
        if town_functions == 'r':
            return self.restart()

        elif town_functions == 'quit':
            quit_game()

        #  elif town_functions == 's':
        #    self.save_character()

        elif town_functions == 'i':
            self.inventory()

        elif town_functions == 'b':
            print("You visit the blacksmith..")
            sleep(1.5)
            blacksmith_theme()
            self.blacksmith_main()
            town_theme()

        elif town_functions == 'c':
            print("You make your way to the chemist manipulator..")
            sleep(1.5)
            chemist_theme()
            self.chemist_main()
            town_theme()

        elif town_functions == 't':
            print(f"You make your way to the tavern..")
            sleep(1.25)
            tavern_theme()
            self.tavern()
            town_theme()

        elif town_functions == 'e':

            if self.town_portal_exists:  # or self.loaded_game:
                same_line_print(f"You re-enter the portal.")

            else:
                sad_cello_theme()
                teletype_txt_file('first_descent.txt')
                pause()
            random_floppy_rw_sound()
            loading_screen()
            dot_dot_dot(15)
            return 'e'

        else:
            unknown_command()

    def dungeon_navigation(self, dungeon_command):
        if dungeon_command == 'w':
            self.hud()
            print("North")
            self.y -= 1
            sleep(.5)
            return
        elif dungeon_command == 'a':
            self.hud()
            print("West")
            self.x -= 1
            sleep(.5)
            return
        elif dungeon_command == 's':
            self.hud()
            print("South")
            self.y += 1
            sleep(.5)
            return
        elif dungeon_command == 'd':
            self.hud()
            print("East")
            self.x += 1
            sleep(.5)
            return
        elif dungeon_command == 'nw':
            self.hud()
            print("Northwest")
            self.y -= 1  # north
            self.x -= 1  # west
            sleep(.5)
            return
        elif dungeon_command == 'ne':
            self.hud()
            print("Northeast")
            self.y -= 1  # north
            self.x += 1  # east
            sleep(.5)
            return
        elif dungeon_command == 'se':
            self.hud()
            print("Southeast")
            self.y += 1  # south
            self.x += 1  # east
            sleep(.5)
            return
        elif dungeon_command == 'sw':
            self.hud()
            print("Southwest")
            self.y += 1  # south
            self.x -= 1  # west
            sleep(.5)
            return
        elif dungeon_command == 'l':
            # this will call dungeon_description().
            self.dungeon_description()
            self.coordinates = (self.x, self.y)
            self.position = self.dungeon.grid[self.y][self.x]
            return
        elif dungeon_command == 'map':
            self.display_map(self.dungeon.player_grid)  #
            pause()
            self.dungeon_description()
            return
        elif dungeon_command == 'm':
            self.item_management_sub_menu()
            return
        elif dungeon_command == 'i':
            self.inventory()
            return
        elif dungeon_command == 'stay':
            print(f"Stay.")
            sleep(1)
            return
        else:  # remove after testing
            print(f"This should be unreachable.")
            return

    def boss_clue_1(self):
        # player finds first clue about wicked queen boss
        self.hud()
        rndm_hint_list = ["a piece of parchment", "a torn piece of fabric", "a broken necklace", "a broken ring"]
        clue_item = random.choice(rndm_hint_list)
        print(f"On the ground before you lays {clue_item}. You carefully pick it up.")
        sleep(1)
        print(f"You see a symbol on it; A woman with a crown, surrounded by many skulls.")
        sleep(1)
        print(f"Without warning, it begins to deteriorate in your hands until it is nothing but ashes!")
        sleep(1)
        print(f"You ponder this, and commit the image to memory. You wonder if there is someone in town who can shed\n"
              f"light on the strange symbol.")
        pause()
        self.hud()
        self.boss_hint_1 = True
        return

    def boss_clue_2(self):
        self.hud()
        print("You see a nasty-looking knife in a hand-etched sheath of gold!")
        sleep(1)
        print("Turning it over in your hands reveals runes that are foreign to you, which cover its entire surface.")
        sleep(1)
        print(f"You carefully place the dagger on your belt.")
        pause()
        self.hud()
        self.boss_hint_2 = True
        return

    def boss_clue_3(self):
        self.hud()
        print("You hear the flapping of wings nearby...")
        sleep(1)
        print(f"You catch a glimpse of a flying creature overhead, just before it disappears into the darkness.")
        pause()
        self.hud()
        self.boss_hint_3 = True
        return

    # def boss_clue_4(self):
    #    self.hud()
    #    print("You find a clue about the boss4")
    #    pause()
    #    self.hud()
    #    self.boss_hint_4 = True
    #    return

    def boss_hint_logic(self):
        # called from victory_over_boss_logic (if self.encounter ==99),
        # which is called from main loop, after exit bosses are defeated
        if not self.boss_hint_1:
            self.boss_clue_1()
            return
        if not self.boss_hint_2:
            self.boss_clue_2()
            return
        if not self.boss_hint_3:
            self.boss_clue_3()
            return
        # if not self.boss_hint_4:
        #    self.boss_clue_4()
        #   return
        # if not self.boss_hint_5:
        # return self.boss_clue_5()
        # if not self.boss_hint_6:
        # return self.boss_clue_6()
        return

    def wide_open_space_logic(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        level_7_openness_phrase = f"This is a rather wide-open area of {self.dungeon.name}."
        level_8_openness_phrase = f"This is a wide open area of {self.dungeon.name}."
        if self.in_a_pit:
            level_7_openness_phrase = f"The pit seems rather wide open here."
            level_8_openness_phrase = f"The pit is wide open here."
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        perimeter = []
        if north_of_you != "*":
            perimeter.append("North")
        if south_of_you != "*":
            perimeter.append("South")
        if east_of_you != "*":
            perimeter.append("East")
        if west_of_you != "*":
            perimeter.append("West")
        if northeast_of_you != "*":
            perimeter.append("Northeast")
        if northwest_of_you != "*":
            perimeter.append("Northwest")
        if southeast_of_you != "*":
            perimeter.append("Southeast")
        if southwest_of_you != "*":
            perimeter.append("Southwest")
        openness = len(perimeter)
        if openness == 7:
            return level_7_openness_phrase
        if openness == 8:
            return level_8_openness_phrase
        else:
            return f"This is a non-descript area of {self.dungeon.name}."

    def atrium_check(self):
        # an atrium connects a corridor to a wide-open chamber.
        # called from automatic_dungeon_description_and_room_exit_finder() *after* intersection_check
        # this only works if intersection check is called first, and is False
        directions = []
        corridor_found = False
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        if northeast_of_you == "*" and northwest_of_you == "*" and north_of_you != "*":
            directions.append("Northern")
            corridor_found = True
            # return "Northern"
        if southeast_of_you == "*" and southwest_of_you == "*" and south_of_you != "*":
            directions.append("Southern")
            corridor_found = True
            # return "Southern"
        if northeast_of_you == "*" and southeast_of_you == "*" and east_of_you != "*":
            directions.append("Eastern")
            corridor_found = True
            # return "Eastern"
        if northwest_of_you == "*" and southwest_of_you == "*" and west_of_you != "*":
            directions.append("Western")
            corridor_found = True
            # return "Western"
        if corridor_found:
            return directions
        else:
            return False

    def intersection_check(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        if northeast_of_you == "*" and northwest_of_you == "*" and southeast_of_you == "*" and southwest_of_you == "*":
            return True
        else:
            return False

    def auto_intersection_description(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        intersection_name = self.dungeon.intersection_name
        if self.in_a_pit:
            intersection_name = self.dungeon.pit_intersection_name
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        if north_of_you != "*":
            exits_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        number_of_ways = len(exits_list)
        if number_of_ways > 1:
            # exits = convert_list_to_string_with_and(exits_list)
            description = f"You are in {intersection_name} which " \
                          f"forms a {number_of_ways}-way intersection."
            return description
        else:
            # this code is ostensibly unreachable
            exits = convert_list_to_string(exits_list)
            print(f"There appears to have been an intersection here at one time, but all except one corridor has "
                  f"collapsed. The only exit is to the {exits}")

    def automatic_dungeon_description_and_room_exit_finder(self):
        # I am very proud of this code. I wrote it all from scratch,
        # which is quite an accomplishment for me.
        # called from dungeon_description()
        multiple_corridors = False
        barrier_name = self.dungeon.barrier_name
        barrier_name_plural = self.dungeon.barrier_name_plural
        corridor_phrase = self.dungeon.corridor_phrase
        corridor_name = self.dungeon.corridor_name
        large_atrium_phrase = self.dungeon.large_atrium_phrase
        one_walled_atrium_phrase = self.dungeon.one_walled_atrium_phrase
        if self.in_a_pit:
            barrier_name = self.dungeon.pit_barrier_name
            barrier_name_plural = self.dungeon.pit_barrier_name_plural
            corridor_phrase = self.dungeon.pit_corridor_phrase
            corridor_name = self.dungeon.pit_corridor_name
            large_atrium_phrase = self.dungeon.pit_large_atrium_phrase
            one_walled_atrium_phrase = self.dungeon.pit_one_walled_atrium_phrase

        corridor_direction = ""
        auto_description_phrase = ""
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        walls_list = []

        if north_of_you != "*":
            exits_list.append("North")
        else:
            walls_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        else:
            walls_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        else:
            walls_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        else:
            walls_list.append("West")
        number_of_exits = len(exits_list)
        number_of_walls = len(walls_list)

        if number_of_walls == 0:  # 4-way intersection, large atrium, or wide-open area

            if not self.intersection_check():  # if you are not at an intersection

                if not self.atrium_check():  # and you are not in an atrium
                    auto_description_phrase = self.wide_open_space_logic()  # you must be in a wide open space

                else:  # you must be in a large atrium with 0 walls
                    auto_description_phrase = large_atrium_phrase
                    corridor_direction = self.atrium_check()

                    if len(corridor_direction) > 1:  # beta if more than 1 corridor
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)
                        multiple_corridors = True

                    else:  # only one corridor
                        corridor_direction = convert_list_to_string(corridor_direction)

            else:  # you must be at a 4-way intersection; intersections do not need to detect corridor_direction
                auto_description_phrase = self.auto_intersection_description()

        if number_of_walls == 1:  # 3-way intersection, wall-lined atrium, or against a wall

            if not self.intersection_check():  # if you are not at an intersection

                if not self.atrium_check():  # and you are not in an atrium lined with one wall
                    # you must be against a wall
                    direction = convert_list_to_string(walls_list)
                    auto_description_phrase = f"You are against {barrier_name} to the {direction}."

                else:  # you must be in an atrium lined with one wall
                    direction = convert_list_to_string(walls_list)
                    auto_description_phrase = f"{one_walled_atrium_phrase} The {direction} " \
                                              f"side is lined with {barrier_name}."
                    corridor_direction = self.atrium_check()

                    if len(corridor_direction) > 1:
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)
                        multiple_corridors = True

                    else:  # beta
                        corridor_direction = convert_list_to_string(corridor_direction)

            else:  # you must be at a 3-way intersection; intersections do not need to detect corridor_direction
                auto_description_phrase = self.auto_intersection_description()

        if number_of_walls == 2:  # corridor, corner, or corner-atrium
            e_w_walls = ['East', 'West']
            n_s_walls = ['North', 'South']

            # if there are walls to your east and west *or* to your north and south:
            if set(e_w_walls) == set(walls_list) or set(n_s_walls) == set(walls_list):  # you must be in a corridor:
                directions = convert_list_to_string_with_and(walls_list)
                auto_description_phrase = f"{corridor_phrase} " \
                                          f"There are {barrier_name_plural} to the {directions}."

            else:  # otherwise, you must be in a corner:
                directions = convert_list_to_string_with_and(walls_list)
                auto_description_phrase = f"You are in a corner. " \
                                          f"There are {barrier_name_plural} to the {directions}."

                if self.atrium_check():
                    corridor_direction = self.atrium_check()
                    # you can sometimes be in a corner and also be in an atrium. i.e. there are 2 proximal corridors.
                    # in that case, the atrium description is ignored, because it is not really an atrium
                    # by human definition, but corridor directions are still calculated:
                    if len(corridor_direction) > 1:
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)  # beta
                        multiple_corridors = True

                    else:
                        corridor_direction = convert_list_to_string(corridor_direction)  # beta

        if number_of_walls == 3:  # 3 walls must be a dead end
            directions = convert_list_to_string_with_and(walls_list)
            auto_description_phrase = f"This is a dead end. " \
                                      f"There are {barrier_name_plural} to the {directions}."

        if number_of_walls == 4:  # this must never happen! :P
            directions = convert_list_to_string_with_and(walls_list)
            print(f"Ostensibly, you are in a cell. "
                  f"There are {barrier_name_plural} to the {directions}.\n"
                  f"You are completely trapped due to a programming error. The grid should never "
                  f"have been created\nwith coordinates that place you in such a predicament. "
                  f"Placing you back at staircase..")
            pause()
            (self.x, self.y) = self.dungeon.staircase
            self.coordinates = (self.x, self.y)
            return

        # finally, print auto_description_phrase and exits:
        if number_of_exits > 1:
            exits = convert_list_to_string_with_and(exits_list)
            print(f"{auto_description_phrase} Exits are to the {exits}.")

            # if there are corridors, calculate which exits lead to them and print out:
            if corridor_direction != "":  # you must be at an atrium, or corner-atrium

                if not self.dungeon_level_exit_check():  # if player is not proximal to dungeon_level exit

                    if multiple_corridors:
                        print(f"The {corridor_direction} exits each lead to {corridor_name}.")
                    else:
                        print(f"The {corridor_direction} exit leads to {corridor_name}.")

                else:  # player IS proximal to the dungeon_level exit
                    if multiple_corridors:
                        print(f"The {corridor_direction} exits each lead to corridors.")
                        dungeon_exit_direction = self.dungeon_level_exit_check()
                        print(f"The {dungeon_exit_direction} corridor leads to a staircase.."
                              f" ***** IT IS THE EXIT OF {self.dungeon.name}!!! *****")
                        #
                    else:
                        corridor_direction = self.dungeon_level_exit_check()
                        print(f"The {corridor_direction} corridor leads to a staircase.."
                              f" ***** IT IS THE EXIT OF {self.dungeon.name}!!! *****")
                        #
            else:  # you must be at an intersection. intersections are auto-described above.
                # just check to see if player is proximal to the dungeon_level_exit:
                if self.dungeon_level_exit_check():
                    corridor_direction = self.dungeon_level_exit_check()
                    print(f"The {corridor_direction} corridor leads to a staircase.."
                          f" ***** IT IS THE EXIT OF {self.dungeon.name}!!! *****")
                    #
        else:  # you must be at a dead end
            exits = convert_list_to_string(exits_list)
            print(f"{auto_description_phrase} The only exit is to the {exits}.")

    def you_cannot_go_that_way(self):
        # called from dungeon_description()
        barrier_name = self.dungeon.barrier_name
        if self.in_a_pit:
            barrier_name = self.dungeon.pit_barrier_name
        random_statement_list = [f"The {barrier_name} blocks your way...", "You cannot go that way...",
                                 f"The {barrier_name} prevents movement in that direction..."]
        random_statement = random.choice(random_statement_list)
        print(random_statement)
        self.x = self.previous_x
        self.y = self.previous_y
        self.coordinates = (self.x, self.y)
        self.position = self.dungeon.grid[self.y][self.x]

    def dungeon_level_exit_check(self):
        # called from dungeon_description()
        north_of_you = (self.x, (self.y - 1))
        west_of_you = ((self.x - 1), self.y)
        south_of_you = (self.x, (self.y + 1))
        east_of_you = ((self.x + 1), self.y)
        level_exit = self.dungeon.exit
        if north_of_you == level_exit:
            return "Northern"
        if west_of_you == level_exit:
            return "Western"
        if east_of_you == level_exit:
            return "Eastern"
        if south_of_you == level_exit:
            return "Southern"
        else:
            return False

    def navigation_position_coordinates(self):
        # called from end of each navigation turn in main loop
        self.position = self.dungeon.grid[self.y][self.x]
        self.coordinates = (self.x, self.y)

    def navigation_turn_initialize(self):
        # called from main loop at beginning of each navigation turn while in dungeon
        self.coordinates = (self.x, self.y)
        self.previous_x = self.x
        self.previous_y = self.y

    def dungeon_description(self):
        # meta-function called from navigation() and main loop.
        self.hud()
        north_south = ""
        east_west = ""
        if self.x > 9:
            east_west = "eastern"
        elif self.x < 10:
            east_west = "western"
        if self.y > 9:
            north_south = "South"
        elif self.y < 10:
            north_south = "North"

        # You cannot go that way; Player has hit a dungeon wall and is returned to previous position
        if self.position == "*":  # asterisk represents barrier
            self.you_cannot_go_that_way()

        # call the automatic description function
        self.automatic_dungeon_description_and_room_exit_finder()

        # Dungeon logical descriptions. They correspond to dungeon instance coordinates and events.
        # They are printed out after automatic description function
        if self.coordinates == self.dungeon.staircase:
            self.staircase_description()
        if self.coordinates == self.dungeon.elevator_landing:
            self.elevator_landing_description()
        if self.coordinates == self.dungeon.teleporter_landing:
            self.teleporter_landing_description()
        if self.coordinates == self.dungeon.pit_landing:
            self.pit_landing_description()
        if self.coordinates == self.dungeon.encounter_deaf_one_1:
            self.deaf_one_fog_remnant_description()
        if self.coordinates == self.dungeon.encounter_deaf_one_2:
            self.deaf_one_fog_remnant_description()
        # self.coordinates = (self.x, self.y)  # commented out. seems to be unnecessary at this point in program.

        # print out dungeon level and coordinates before returning
        if self.in_a_pit:
            # assuming pit landing coordinates are at 1, 14:
            print(f"(In a pit below {self.dungeon.name}) Coordinates: {self.x, (self.y - 13)}")
        else:
            if self.coordinates != self.dungeon.exit:
                print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}, "
                      f"{north_south}{east_west} region) Coordinates: {self.coordinates}")
        return

    def display_map(self, maps):
        if self.in_a_pit:
            print(f"You are in uncharted territory..")
            sleep(1)
            return
        else:
            cls()
            print("You look at the map..")
            # print(f"Position key: {self.position}")  # remove after testing

            self.coordinates = (self.x, self.y)
            print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}) Coordinates: {self.coordinates}")

            if self.coordinates != self.dungeon.staircase:
                self.dungeon.player_grid[self.y][self.x] = "X"
                for element in range(0, 20):
                    print(*maps[element])
                # replace the X with a dot after printing map so that it doesn't leave a trail of x's:
                self.dungeon.player_grid[self.y][self.x] = "."
                print(f"S = Staircase X = your position E = Exit")

            else:
                for element in range(0, 20):
                    print(*maps[element])
                print(f"S = Staircase E = Exit\nYou are currently at the staircase.")

            # place the next line in the main file to leave a trail of x's throughout the map to see where you've been.
            # player_1.dungeon.player_grid[player_1.y][player_1.x] = "x"
            return

    def dungeon_exit_event(self):
        # dungeon dictionary in dungeons.py file
        print(f"You approach the exit. With quiet resolve, you turn to briefly look\n"
              f"behind you, and then continue onward, toward your goal.")
        sleep(2)
        # the deepest dungeon level will have no exit, so there should be no chance of a KeyError by adding 1.
        # at end of game, transport player back to dungeon level 1 with:
        # self.dungeon_key = 1
        # self.dungeon = dungeon_dict[self.dungeon_key]
        self.dungeon_key += 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        (self.x, self.y) = self.dungeon.staircase  # simplified with tuple instead of self.x = and self.y =
        self.coordinates = (self.x, self.y)  # beta testing
        # for a while, self.coordinates would be set after first move. otherwise, the intro would be printed 1st,
        # followed by the staircase description, which was awkward. after migrating to automatic_description, this
        # seems to no longer be the case
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = 0
        pause()
        return "Exit Boss"
