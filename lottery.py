# lottery.py
# Author: Stacey Sharp (github.com/ssharpjr)
# Version: 2016-01-24
# Description: Gathers and tallys scores for a lottery drawing

import sys

tickets = {}
counter = 1

print("\nWelcome to the Lottery Maker 9000!")
print("\nWhat would you like to do?")
print("1. Enter a new player")
print("2. See the existing player list")
print("3. Pull the lottery!")
print("Q. Exit the program")
choice = input("\nChoose a menu option: ")

if choice != '1':
    print("\nNot ready yet, Goodbye :)")
    sys.exit()

name = input("\nEnter the new player's name: ")
name = name.title()
entries = input("Enter %s's number of entries: " % name)

print(name + " has " + entries + " tickets.\n")
entries = int(entries)

for entry in range(counter, entries + 1):
    tickets[entry] = name
    counter = counter + 1

print(tickets)
print("\nTickets: " + str(entries))
print("Counter: %s" % counter)
