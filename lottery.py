#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 lottery.py
 Author: Stacey Sharp (github.com/ssharpjr)
 Version: 2016-01-24
 Description: Gathers and tallys scores for a lottery drawing.
'''

import sys
import os
import random

tickets = {}
ticket_holders = {}
counter = 1


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pressAnyKey():
    input("Press any key to continue...")
    clearScreen()


def notReady():
    print("\nThis function is not ready yet.")
    pressAnyKey()


def savePlayers():
    saveFile = open('players.txt', 'w')
    saveFile.write(str(ticket_holders))
    saveFile.close()


def loadPlayers():
    pass


def deletePlayers():
    print("\nDelete all player tickets")
    choice = input("Are you sure you want to delete all player tickets" +
                   " (y/n)? ")
    if choice == 'y':
        try:
            if os.stat('players.txt').st_size > 0:
                os.remove('players.txt')
                print("\nDone.")
                pressAnyKey()
                main()
        except Exception:
            print("\nNo tickets to delete.")
            pressAnyKey()
            main()
    elif choice == 'n':
        print("\n")
        clearScreen()
        main()
    else:
        clearScreen()
        main()


def addPlayer(counter):
    while True:
        name = input("\nEnter the new player's name" +
                     " or 'Q' to return to the Main: "
                     )
        if name == 'q':
            clearScreen()
            main()
        name = name.title()
        entries = input("Enter %s's number of entries: " % name)
        ticket_holders[name] = int(entries)
        savePlayers()
        print(name + " has " + entries + " tickets.")
        entries = int(entries)
        cEntries = counter + entries

        for entry in range(counter, cEntries):
            tickets[entry] = name
            counter += 1

        totalTickets = sum(ticket_holders.values())
        print("\nTotal tickets: " + str(totalTickets))
        print("Next ticket number: %s" % counter)


def playerList():
    try:
        if os.stat('players.txt').st_size < 0:
            print("\nThere are no existing players!\n")
            pressAnyKey()
            main()
        else:
            playerFile = open('players.txt', 'r')
            ticket_holders = eval(playerFile.read())
            playerFile.close()
    except Exception:
        print("\nThere are no existing players.\n")
        pressAnyKey()
        main()

    print("----------------------------------------")
    print("\nCurrent ticket holders:\n")
    for key, value in sorted(ticket_holders.items()):
        print(key, '\t\t:', value)

    totalTickets = sum(ticket_holders.values())
    print("\nTotal tickets: " + str(totalTickets) + "\n")
    print("----------------------------------------")
    pressAnyKey()
    main()


def pullLottery():
    totalTickets = sum(ticket_holders.values())
    winningTicket = random.randrange(1, totalTickets + 1)
    winner = tickets[winningTicket]

    print("----------------------------------------")
    print("\nLottery Drawing\n")
    print("The winning ticket number is: " + str(winningTicket))
    print("\nThe winner is: " + winner.upper() + "!\n")
    print(winner + " had " + str(ticket_holders[winner]) +
          " tickets in this drawing."
          )
    print("Lottery pulled from " + str(totalTickets) + " tickets.\n")
    print("----------------------------------------")
    pressAnyKey()
    main()


def exitProgram():
    print("\nGoodbye!\n")
    sys.exit()


# Begin main
def main():
    print("--------------------------------------------------")
    print("\nWelcome to the Mystery Hostess Lottery Maker!")
    print("\nWhat would you like to do?")
    print("1. Enter a new player")
    print("2. View current ticket holders")
    print("3. Pull the lottery!")
    print("D. Delete all ticket holders")
    print("Q. Exit the program\n")
    print("--------------------------------------------------")
    choice = input("\nChoose a menu option: ")

    if choice == '1':
        addPlayer(counter)
    elif choice == '2':
        playerList()
    elif choice == '3':
        pullLottery()
    elif choice == 'd':
        deletePlayers()
    elif choice == 'q':
        exitProgram()
    else:
        print("Not a valid option")
        pressAnyKey()
        main()


# Run main
if __name__ == '__main__':
    clearScreen()
    main()
