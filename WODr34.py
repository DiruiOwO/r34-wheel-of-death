from lib2to3.pytree import convert
from operator import concat
import time
from unittest import skip
import webbrowser
from random import randint, randrange

print("Wheel of death (r34 edition)")
print("Not proudly made by dirui")
print("") #seperator

a = input("How many tabs?: ")
cona = int(a)
print("") #seperator

t = input("How much time between tabs? (s): ")
cont = int(t)
print("") #seperator

print("0 - Custom (sometimes will bring you back to the main page)")
print("1 - Websites random function")
ver = input("What version do you want to use? 0/1: ")
print("") #seperator

if ver == "0":
    for x in range(cona):
        num = randint(1000000, 9999999)
        connum = str(num)
        webbrowser.open_new_tab("https://rule34.xxx/index.php?page=post&s=view&id=" + connum)
        print("ID = " + connum)
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
print("Done!")
print("") #seperator
input('Press ENTER to exit')
    
