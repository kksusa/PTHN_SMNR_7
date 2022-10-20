from os import system
from time import sleep
import UI

def Menu():
    system('clear')
    UI.Greetings()
    while True:
        try:
            menu = int(input())
            if menu >= 1 and menu <= 4: return menu
            else: UI.BadMenuChoice()
        except: UI.BadMenuChoice()