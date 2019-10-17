from time import sleep
from os import system
no = ["you are an idiot","You are an idiot","Gabe itches","gabe itches","Mike Oxmall","Mike oxmall","mike Oxmall","mike oxmall","cunt","fuck","dick","pussy","tits","tiddies"]
stop = ["cancel","quit","exit","stop"]
scrname = "notebot"
VER = "0.5.0"
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
        print('e: inappropriate name or repeater input!')
        print("this script will end in four (4) seconds.")
        sleep(4)
print("notebot v"+VER)
print("(C) 2019 Brendan J. Webb. All rights reserved.")
sleep(2)
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
                    print("Okay! Let's do this!\nstarting in:")
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
                        print("hi there! I'm",scrname+". I was told by",name+" to tell you the following:\n\n"+inf+"\n\nI'll just have these dots show up below to prove that this script\n(and",name+"'s computer) are both still running.")
                        print("By the way, don't shoot the messenger. please. Us messengers don't like getting shot.\nI DON'T WANNA DIIIEEEEEE!!!!")
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
