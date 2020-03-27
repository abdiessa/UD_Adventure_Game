import time
import random


def stop(messege):
    print(messege)
    time.sleep(2)


def intro(list, selection):
    stop("Make yourself in your mind")
    stop("Dargon " + selection + " is good game")


def beat(list, selection):
    if "short grass" in list:
        stop("\nYou make fly into the cave.")
    else:
        stop("\nYou are flying out the place.\n")
        list.append("short grass")
    place(list, selection)


def palace(list, selection):
    stop("\nYou are about to " + selection)
    stop("\nOn to " + selection + "'s palace!")
    stop("\nThe " + selection + " FIGHT!\n")
    if "short grass" not in list:
        stop("Keep-up Make Over it.\n")
    while True:
        input2 = input("Select to (1) or (2) to run?")
        if input2 == "1":
            if "short grass" in list:
                stop("\For that " + selection +
                     " moves to attack and rise the sword.")
                stop("\nAlso " + selection + " runs away!")
                stop("\nYou have rid the town of the " +
                     selection + " and that passed!\n")
            else:
                stop("You are" + selection + ".")
                stop("\nGAME OVER!\n")
            never_giveup()
            break
        if input2 == "2":
            stop("\nYou run back into the place. "
                 "\nLuckily, you don't seem to have been "
                 "followed.\n")
            place(list, selection)
            break


def place(list, selection):
    stop("Number 1 to knock on the door of the palace.")
    stop("Number 2 to peer into the cave.")
    stop("What are you doing now, please select?")
    while True:
        input1 = input("(Please Number 1 or 2.)\n")
        if input1 == "1":
            palace(list, selection)
            break
        elif input1 == "2":
            beat(list, selection)
            break


def never_giveup():
    again = input("One more time? (y/n)").lower()
    if again == "y":
        stop("\n\n\OK! Restarting the game ...\n\n\n")
        lets_play()
    elif again == "n":
        stop("\n\n\nThank You 4 Playing!\n\n\n")
    else:
        never_giveup()


def lets_play():
    list = []
    selection = random.choice(
        ["Megaman", "Spyro", "Dragon Fly", "IRON MAN", "HE-MAN"])
    intro(list, selection)
    place(list, selection)


lets_play()
