import time
import random

# from where one item gets randomized once at beginning of game:
villain_list = ['dragon', 'romulan', 'pirate']
weapon_list = ['sword', 'phaser']
active_weapon = []
# empty list to add weapon once player picked it up
# to avoid the villain_choice getting changed mid game


def print_pause(message_to_print, print_wait):
    print(message_to_print)
    time.sleep(print_wait)


def replace_substring(string_output, substring):

    string_output = string_output.replace('villain', substring)
    return string_output
# replace the substring 'villain' in prints(print_pause) with the current
# randomized villain_choice(item)


def intro():  # preview of game
    print_pause("You find yourself standing in an open field, \n"
                "filled with grass and yellow wildflowers.", 1)
    print_pause(replace_substring("Rumor has it that a grim villain is "
                                  "somewhere\n around and has been "
                                  "terrifying the nearby village.",
                villain_choice), 1)  # substring from villain_choice()
    print_pause("In front of you is a house.", 1)
    print_pause("To your right is a dark cave.", 1)
    print_pause("In your hand you hold your trusty - but not very effective "
                "dagger.", 1)


def cave():  # decisive place to take action for next step
    print_pause("Behind one rock you spot a new weapon.", 11)
    # print_pause(weapon_choice) # check for existing weapons in weapon_choice
    pick_up = input("Collect the weapon?\n")
    if pick_up == 'yes' or pick_up == "y":
        active_weapon.append(weapon_choice)  # user activates weapon
        print_pause("All set and armored", 1)
        # print(active_weapon)  # check only
        if "sword" in active_weapon:  # indicate this step is already done
            print_pause("You have already upgraded to a sword. "
                        "Nothing left to do here.", .5)
        elif "phaser" in active_weapon:
            print_pause("You have picked up the phaser already. "
                        "Continue your journey.", .5)
        print_pause("Go one step back", .5)
        field()
    elif pick_up == 'no' or pick_up == "n":
        field()


def house():  # potential battlefield
    print_pause(replace_substring("The villain has tormented the village!",
                villain_choice), 1)
    print_pause(replace_substring("You find yourself facing the villain.",
                villain_choice), .5)
    Join = input('Would you like to fight?\n')
    if Join.lower() == 'yes' or Join.lower() == 'y':
    # print(active_weapon)  # check only on this line
        print_pause("You brave the danger", .5)
        fight()
    elif Join.lower() == 'no' or Join.lower() == "n":
        print_pause("You head back to the field.", .5)
        field()


def fight():
    if "sword" in active_weapon:  # if active_weapon != 'dagger'
        print_pause("The Sword of Damocles has casted impending doom"
                    " over the village.", .5)
        print_pause("You have saved the village.", 1)  # win
    elif "phaser" in active_weapon:  # if active_weapon != 'dagger'
        print_pause(replace_substring("The villain could not fight "
                                      "the power of the phaser"
                                      "You win",
                    villain_choice), 1)  # win
    else:  # if user did not pick_up: active_weapon.append from cave
        print_pause("The dagger could not measure up to the task. "
                    "You have been defeated", 1)  # active_weapon != 'dagger'
    play_again()  # have the option to try again regardless of outcome


def field():  # neutral space
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?", 1)
    door = input("Please enter 1 or 2\n")
    if door == '1':
        print_pause("You open the front door", .5)
        house()  # go inside house
    elif door == '2':
        print_pause("You descend into the dark cave", 1)
        cave()  # go inside cave
    else:
        field()


def play_again():  # option to replay
    print_pause("Would you like to play again?\n", 1)
    answer = input("Yes/No\n").lower
    if answer == "yes" or answer == "y":
        intro()
        field()
    elif answer == "no" or answer == "n":
        print_pause("Thanks for playing", .5)



def main():  # start game function
    global villain_choice
    # global limit repetitive code when replacing substring
    global weapon_choice
    # global to be able to modify during game
    global active_weapon

    villain_choice = random.choice(villain_list)
    # print(villain)  # check only on this line
    weapon_choice = random.choice(weapon_list)
    # print(weapon_choice)
    active_weapon = []  # when activated by user: _ == weapon_choice
    # print(weapon_choice)  # check only on this line

    intro()  # start game with
    field()  # starting point
    # play_again()  # option to restart


main()  # start

''' References:
https://stackabuse.com/
https://stackoverflow.com/
https://stackoverflow.com/questions/27462866/python-replacing-characters-in-string-without-replace-function
https://www.w3schools.com/python/ref_string_replace.asp
https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
'''
