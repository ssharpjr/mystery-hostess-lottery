# -*- coding: utf-8 -*-
'''
 lottery.py
 Author: Stacey Sharp (github.com/ssharpjr)
 Version: 2016-01-24
 Description: Gathers and tallys scores for a lottery drawing.
'''

import sys

tickets = {}
ticket_holders = {}
counter = 1


def pressAnyKey():
    input("Press any key to continue...")


def notReady():
    print("\nThis function is not ready yet.")
    pressAnyKey()


def addPlayer(counter):
    while True:
        name = input("\nEnter the new player's name" +
                     " or 'Q' to return to the Main: "
                     )
        if name == 'q':
            main()
        name = name.title()
        entries = input("Enter %s's number of entries: " % name)
        ticket_holders[name] = int(entries)
        print(name + " has " + entries + " tickets.")
        entries = int(entries)
        cEntries = counter + entries

        for entry in range(counter, cEntries):
            tickets[entry] = name
            counter += 1

        # print(tickets)
        # print(ticket_holders)
        # print("\nTickets: " + str(entries))
        # print("Counter: %s" % counter)


def playerList():
    print("\n")
    print("Current ticket holders:")
    for key, value in sorted(ticket_holders.items()):
        print(key, ':', value)

    totalTickets = sum(ticket_holders.values())
    print("Total tickets: " + str(totalTickets))
    pressAnyKey()
    main()


def pullLottery():
    notReady()
    main()


def exitProgram():
    print("Goodbye")
    sys.exit()


# Begin main
def main():
    print("\nWelcome to the Mystery Hostess Lottery Maker!")
    print("\nWhat would you like to do?")
    print("1. Enter a new player")
    print("2. See the existing player list")
    print("3. Pull the lottery!")
    print("Q. Exit the program")
    choice = input("\nChoose a menu option: ")

    if choice == '1':
        addPlayer(counter)
    elif choice == '2':
        playerList()
    elif choice == '3':
        pullLottery()
    elif choice == 'q' or 'Q':
        exitProgram()
    else:
        print("Not a valid option")
        main()


# Run main
if __name__ == '__main__':
    main()
