import time
import webbrowser
from random import randint
from colorama import Fore
import os
from bs4 import BeautifulSoup
import requests


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

nonourl = "link"

print(Fore.WHITE + "Wheel of death (r34 edition)")
print("Not proudly made by dirui")
print("") #seperator

input(Fore.GREEN + 'Press ENTER to begin')

cls()

a = input(Fore.WHITE + "How many tabs?: ")
cona = int(a)
print("") #seperator

t = input("How much time between tabs? (s): ")
cont = int(t)
print("") #seperator

cls()

print("0 - Custom (sometimes will bring you back to the main page)")
print("1 - Websites random function")
ver = input("What version do you want to use? 0/1: ")
print("") #seperator

cls()

if ver == "0":
    for x in range(cona):
        num = randint(1000000, 9999999)
        connum = str(num)
        webbrowser.open_new_tab("https://rule34.xxx/index.php?page=post&s=view&id=" + connum)

        source = requests.get("https://rule34.xxx/index.php?page=post&s=view&id=" + connum).text
        soup = BeautifulSoup(source, "lxml")
        fsoup = soup.find("link", {"href":"https://rule34.xxx/index.php?page=post&s=list&tags=all"})

        fsoupcon = str(fsoup)

        print(Fore.WHITE + "ID = " + connum)

        if nonourl in fsoupcon:
            print(Fore.RED + "^ ID invalid ^")
            #cona = cona + 1
            #idk what to do when invalid, maybe someone could fork and fix it lol
            #is it even posible to extend range() or for loop?????

        time.sleep(cont)

if ver == "1":
    for x in range(cona):
        webbrowser.open_new_tab("https://rule34.xxx/index.php?page=post&s=random")
        countx = int(x)
        countxp1 = countx + 1
        conx = str(countxp1)
        print("Started " + conx + " tabs")
        time.sleep(cont)

print("") #seperator
print(Fore.GREEN + "Done!")
print("") #seperator
input(Fore.RED + 'Press ENTER to exit')

cls()
