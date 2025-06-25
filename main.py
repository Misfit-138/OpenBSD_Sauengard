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

from player_module import cls, town_theme, gong, sleep, pause, teletype, \
    dungeon_command_choices, quit_game, game_start, loading_screen, os_check, unknown_command

os_check()


while True:

    player_1 = game_start()
    loading_screen()
    print(f"You enter the town of Fieldenberg.")
    sleep(1.5)
    player_1.in_town = True
    player_1.in_dungeon = False  # defined as False after portal use
    town_theme()

    # in_town loop:
    while player_1.in_town:
        player_1.hud()
        command = player_1.town_navigation()
        if command == "Restart":
            break
        if command == 'e':
            player_1.in_town = False
            player_1.town_portal_exists = False
            player_1.in_dungeon = True
            player_1.hud()
            player_1.dungeon_description()
            # random_floppy_loading_sound()
            # sleep(2)
            player_1.dungeon_theme()
            navigation_list = ['w', 'a', 's', 'd', 'ne', 'nw', 'se', 'sw', 'l', 'map', 'm', 'i', 'stay']

            # DUNGEON NAVIGATION LOOP:
            game_over = False
            while player_1.in_dungeon:

                if game_over:

                    if player_1.choose_to_play_again():
                        break

                if not player_1.in_dungeon:
                    break

                player_1.navigation_turn_initialize()
                # player_1.loot()  # for testing
                # player_1.asi()  # for testing

                if player_1.position == 0:  # 0 is the game/level start position
                    # player_1.hud()
                    cls()
                    teletype(player_1.dungeon.intro)
                    pause()

                    # set player position, which also removes intro condition
                    player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]
                    player_1.dungeon_description()

                dungeon_command = dungeon_command_choices()

                if dungeon_command == 'p':
                    if player_1.use_scroll_of_town_portal():
                        town_theme()
                        player_1.in_town = True
                        player_1.in_dungeon = False
                        player_1.town_portal_exists = True
                        break
                    else:
                        continue  # if you have no scrolls, don't waste a turn

                elif dungeon_command == 'r':
                    if player_1.restart():
                        break
                    else:
                        player_1.dungeon_description()
                        continue

                elif dungeon_command == 'quit':
                    if not quit_game():
                        player_1.dungeon_description()
                        continue

                elif dungeon_command == "q":
                    player_1.hud()
                    monster = None  # quantum_effects needs monster parameter, but player is not in battle at this point
                    player_1.quantum_effects(monster)

                elif dungeon_command == 'g':
                    if not player_1.drink_potion_of_strength():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'v':
                    if not player_1.drink_antidote():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'h':
                    if not player_1.drink_healing_potion():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'c':
                    if not player_1.drink_elixir():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command in navigation_list:
                    player_1.dungeon_navigation(dungeon_command)

                else:
                    unknown_command()
                    player_1.dungeon_description()
                    continue  # continue means you do not waste a turn

                # ***** END OF NAVIGATION choice *************************************************************
                # NAVIGATION position and coordinate CALCULATIONS:
                player_1.navigation_position_coordinates()
                # ENCOUNTER LOGIC IS DETERMINED *BEFORE* event_logic(), BUT CAN BE RE-ASSIGNED BASED ON
                # RETURNED VALUES FROM event_logic()
                player_1.encounter_logic()

                # EVENT LOGIC IS DETERMINED BEFORE end_of_turn_calculation() AND player_1.check_dead(),
                # IN CASE PLAYER SUFFERS DAMAGE, ETC.
                event = player_1.event_logic()  # trigger any events corresponding to self.coordinates
                player_1.check_for_boss(event)  # check if event should trigger a boss encounter
                if event == "DeafOnePortal":  # by conditionals, player will be forced to tavern for hint event
                    break
                # META CALCULATION FUNCTION FOR REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                # this is also called after monster melee, necro, poison and quantum attack
                # as well as after turning/banishing, and player victory, etc.,
                player_1.end_of_turn_calculation()
                if player_1.check_dead():  # player can die of necrosis/poison/event damage after calculations
                    game_over = True
                    continue
                # LASTLY, dungeon_description()
                player_1.dungeon_description()  # this seems to work best when put LAST

                if player_1.encounter < 11 or player_1.encounter > 20:  # < 11 = normal monster. > 20 = boss
                    player_1.in_proximity_to_monster = True
                    game_over = False

                    # IN PROXIMITY TO MONSTER LOOP *contains battle loop within it*
                    while player_1.in_proximity_to_monster:

                        if game_over:
                            break

                        if not player_1.in_proximity_to_monster:
                            break

                        # create a monster based on player_1.encounter: < 11 = normal monster. > 20 = boss
                        monster = player_1.meta_monster_generator()
                        player_1.monster_introduction(monster)

                        if player_1.monster_likes_you_or_steals_from_you(monster):
                            break

                        # PLAYER INITIATIVE, MONSTER INITIATIVE
                        human_goes_first = player_1.initiative(monster)

                        # IF MONSTER GOES FIRST:
                        if not human_goes_first:
                            player_1.hud()
                            monster.meta_monster_function(player_1)

                            if not player_1.check_dead():  # if player not dead

                                if monster.can_paralyze and monster.paralyze(player_1):
                                    if not player_1.check_dead():  # if player not dead
                                        print(f"You regain your faculties.")
                                        pause()

                                    else:
                                        print("You are dead and paralyzed!")
                                        game_over = True
                                        break

                            else:  # you died
                                player_1.random_death_statement()
                                pause()
                                game_over = True
                                break

                            # at this point, monster still has initiative
                            # therefore, if player has npc allies and monster has multi_attack or lesser_multi_attack,
                            # monster attacks npc allies:
                            player_1.monster_attacks_npc_meta(monster)

                        # OTHERWISE, PLAYER PROMPT and enter BATTLE LOOP
                        # ********************************* BATTLE LOOP ***********************************************
                        while True:
                            if not player_1.in_proximity_to_monster:
                                break
                            battle_choice = player_1.battle_menu_choices(monster)

                            # these choices count as turns, and are therefore followed by monster's turn:
                            battle_choice_turn_list = ['e', 'h', 'g', 'v', 'c', 'q']
                            if battle_choice in battle_choice_turn_list:

                                if battle_choice == "e":
                                    if player_1.evade(monster):
                                        player_1.in_proximity_to_monster = False  # get out of battle loop and prox loop
                                        player_1.dungeon_description()  # beta works so far
                                        break

                                elif battle_choice == 'h':
                                    if not player_1.drink_healing_potion():
                                        continue  # if you have no potions, don't waste a turn!

                                elif battle_choice == 'g':
                                    if not player_1.drink_potion_of_strength():
                                        continue  # if you have no potions, don't waste a turn!

                                elif battle_choice == 'v':
                                    if not player_1.drink_antidote():
                                        continue  # if you have no potions, don't waste a turn!

                                elif battle_choice == 'c':
                                    if not player_1.drink_elixir():
                                        continue  # if you have no potions, don't waste a turn!

                                # PLAYER QUANTUM ATTACK
                                elif battle_choice == "q":
                                    player_1.hud()
                                    damage_to_monster = player_1.quantum_effects(monster)

                                    # if invalid input during quantum effect, None is returned:
                                    if damage_to_monster is None:  # invalid input
                                        continue  # should not waste a turn

                                    # If monster is successfully turned, stone-petrified, fearful,
                                    # disentangled, lost to gravity well or banished, etc., experience is gained,
                                    # but player gets no gold or loot:
                                    if not player_1.in_proximity_to_monster:
                                        # CALCULATE REGENERATION/POTION OF STR/POISON/NECROSIS/PROT EFFECT:
                                        player_1.end_of_turn_calculation()
                                        if player_1.check_dead():  # you can die from poison or necrosis,
                                            game_over = True  # right after victory, following calculations
                                            break

                                        # allies heal and no longer retreat:
                                        player_1.npc_calculation()

                                        if player_1.encounter > 20:  # if victory over a boss by quantum 'turning':
                                            gong()
                                            sleep(4)
                                            player_1.dungeon_theme()
                                            player_1.victory_over_boss_logic()

                                        player_1.level_up(monster.experience_award, monster.gold)
                                        player_1.dungeon_description()
                                        break

                                    # otherwise, calculate damage:
                                    # if total monster hit points is returned from quantum_effects(),
                                    # then monster will die instantly and player gets loot
                                    monster.reduce_health(damage_to_monster)
                                    if monster.check_dead():  # if human player defeats monster with quantum attack
                                        # CALCULATE REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                                        # player_1.end_of_turn_calculation()
                                        if not player_1.end_game_check(monster):  # player lives if game completed
                                            player_1.end_of_turn_calculation()  # beta
                                            # player can die of poison/necrosis after monster hp are reduced to 0:
                                            if player_1.check_dead():
                                                game_over = True
                                                player_1.in_proximity_to_monster = False
                                                break

                                        player_1.hud()
                                        player_1.victory_statements(monster)
                                        pause()

                                        # npc allies heal and no longer retreat:
                                        player_1.npc_calculation()
                                        player_1.level_up(monster.experience_award, monster.gold)
                                        player_1.in_proximity_to_monster = False
                                        player_1.loot()
                                        player_1.victory_over_boss_logic()

                                        if player_1.end_game_check(monster):  # beta
                                            player_1.end_game_character_condition_resets()
                                            game_over = True
                                            player_1.in_proximity_to_monster = False
                                            break

                                        player_1.dungeon_description()
                                        break

                                # if monster is still alive after quantum attack, and player has allies,
                                # npc allies attack monster:
                                if player_1.npc_attack_logic(monster):  # if npc ally defeats monster
                                    # player_1.end_of_turn_calculation()  # restore if beta below does not work
                                    pause()
                                    if not player_1.end_game_check(monster):  # player lives if game completed
                                        # player can die of poison/necrosis after monster hit points are reduced to 0:
                                        player_1.end_of_turn_calculation()  # beta

                                        if player_1.check_dead():
                                            game_over = True
                                            player_1.in_proximity_to_monster = False
                                            break

                                    player_1.npc_calculation()  # allies heal and no longer retreat
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()
                                    if player_1.end_game_check(monster):  # beta
                                        player_1.end_game_character_condition_resets()
                                        game_over = True
                                        player_1.in_proximity_to_monster = False
                                        break
                                    player_1.dungeon_description()
                                    break

                                # ****MONSTER TURN AFTER YOU SWIG POTION, fail to evade, or cast quantum attack******
                                #
                                player_1.hud()
                                monster.meta_monster_function(player_1)
                                if not player_1.check_dead():  # if player not dead

                                    if monster.can_paralyze and monster.paralyze(player_1):

                                        if not player_1.check_dead():
                                            print(f"You regain your faculties.")
                                            pause()
                                            # if monster has multi_attack, then attack npc
                                            player_1.monster_attacks_npc_meta(monster)
                                            continue

                                        else:
                                            print("You are dead and paralyzed!")
                                            game_over = True
                                            break

                                else:
                                    print(f"You died!")
                                    sleep(3)
                                    game_over = True
                                    break

                                # if player has npc allies, monster attacks them
                                player_1.monster_attacks_npc_meta(monster)

                            # FIGHT: player chooses melee:
                            elif battle_choice == "f":
                                print(f"Fight.")
                                damage_to_monster = player_1.melee(monster)
                                monster.reduce_health(damage_to_monster)

                                if monster.check_dead():  # if human player defeats monster with melee attack
                                    # CALCULATE REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                                    # player_1.end_of_turn_calculation()  # restore if beta below does not work
                                    if not player_1.end_game_check(monster):  # player lives if game completed
                                        player_1.end_of_turn_calculation()  # beta
                                        # player can die of poison/necrosis after monster hit points are reduced to 0:
                                        if player_1.check_dead():
                                            game_over = True
                                            player_1.in_proximity_to_monster = False
                                            break

                                    player_1.hud()
                                    player_1.victory_statements(monster)
                                    pause()
                                    # npc allies heal and no longer retreat:
                                    player_1.npc_calculation()
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()

                                    if player_1.end_game_check(monster):  # beta
                                        player_1.end_game_character_condition_resets()
                                        game_over = True
                                        player_1.in_proximity_to_monster = False
                                        break

                                    player_1.dungeon_description()
                                    break

                                # if monster still alive after player melee attack and player has allies
                                # npc allies attack monster
                                if player_1.npc_attack_logic(monster):  # if npc ally defeats monster
                                    # player_1.end_of_turn_calculation()  # restore if beta below does not work
                                    pause()
                                    if not player_1.end_game_check(monster):  # allow player to live if game completed
                                        player_1.end_of_turn_calculation()  # beta
                                        if player_1.check_dead():
                                            game_over = True
                                            player_1.in_proximity_to_monster = False
                                            break

                                    player_1.npc_calculation()  # allies heal and no longer retreat
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()

                                    if player_1.end_game_check(monster):  # beta
                                        player_1.end_game_character_condition_resets()
                                        game_over = True
                                        player_1.in_proximity_to_monster = False
                                        break

                                    player_1.dungeon_description()
                                    break

                                # monster turn if still alive after player melee attack:
                                else:
                                    monster.meta_monster_function(player_1)

                                    # I tried to offload this code, but the breaks and continues are pretty tangled
                                    if not player_1.check_dead():  # if player not dead

                                        if monster.can_paralyze and monster.paralyze(player_1):

                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You regain your faculties.")
                                                pause()
                                                # if monster has multi_attack, then attack npc
                                                player_1.monster_attacks_npc_meta(monster)
                                                continue

                                            else:
                                                print("You are dead and paralyzed!")
                                                game_over = True
                                                break

                                    else:  # you died
                                        player_1.random_death_statement()
                                        sleep(3)
                                        game_over = True
                                        break

                                    player_1.hud()

                                # if player has npc allies, monster attacks them:
                                player_1.monster_attacks_npc_meta(monster)

                            else:  # invalid inputs. this should be unreachable, since creating battle_menu_choices()
                                print(f"Invalid input.")
                                sleep(1)
                                player_1.hud()
                                continue

                else:  # encounter condition False; no monster, continue
                    continue

        else:  # player is in town and does NOT (E)nter dungeon; continue
            continue
