dot_speed = 0.1
from time import sleep
from os import system
no = ["you are an idiot","You are an idiot","Gabe itches","gabe itches","Mike Oxmall","Mike oxmall","mike Oxmall","mike oxmall","cunt","fuck","dick","pussy","tits","tiddies"]
stop = ["cancel","quit","exit","stop"]
scrname = "notebot"
VER = "0.6.1"
def cancel(): 
    system("cls||clear")
    print("Okay, cancelled. Quitting in 3s...")
    sleep(1)
    system("cls||clear")
    print("Okay, cancelled. Quitting in 2s...")
    sleep(1)
    system("cls||clear")
    print("Okay, cancelled. Quitting in 1s...")
    sleep(1)
    system("cls||clear")
    print("Quitting...")
    sleep(0.5)
    
def err():
        system("clear||cls")
        print('e: inappropriate name or note input!')
        print("this script will end in four (4) seconds.")
        sleep(4)
print("The 'dot_speed' variable is configured to cycle the dots every",dot_speed,"seconds.")
print("")
print("To change it, simply open this script in your favourite text editor and change the number.\nmake sure not to enclose it in quotes though!")
print("")
print("")
print("notebot v"+VER)
print("(C) 2019 Brendan J. Webb. All rights reserved.")
sleep(10)
system("cls||clear")
print("Hi there! I'm",scrname+".")
print("What's your name? type it out, then hit [enter]...")
name = input()
if name.lower() in no:
    err()
else:
    if name.lower() in stop:
        cancel()
    else:
        print("What do you want me to say,",name+"? again, type it out, then hit [enter]...")
        inf = input()

        if inf.lower() in no:
            err()
        else:
            if inf.lower() in stop:
                cancel()
            else:
                if name.lower() in inf:
                    system("cls||clear")
                    print("you can't print your name,",name+"!")
                    sleep(2)
                else:
                    system("cls||clear")
                    print("Okay, initializing.\nStarting in:")
                    print("5.")
                    sleep(1)
                    print("4.")
                    sleep(1)
                    print("3.")
                    sleep(1)
                    print("2.")
                    sleep(1)
                    print("1.")
                    sleep(1)
                    while True:
                        system("cls||clear")
                        print("hi there! I'm",scrname+". I was told by",name+" to tell you the following:\n\n"+inf+"\n\nThe dots below are designed to confirm that the script is still running.")
                        print("They're also designed to make sure that",name+"'s computer isn't frozen.")
                        print(".")
                        sleep(dot_speed)
                        print(".")
                        sleep(dot_speed)
                        print(".")
                        sleep(dot_speed)