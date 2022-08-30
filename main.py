from playsound import playsound
import os
import getpass
from pystyle import *
import requests
import pyautogui as pag
from time import sleep
from elevate import elevate
import keyboard as kb
import shutil
import wget
import threading
import pygame
from pygame.locals import *
import itertools
import threading
import time
import sys
from colorama import * 
from rich.console import Console
import urllib.request
import random

elevate()

def loopSound():
    while True:
        playsound('moosiq.mp3', block=True)

# providing a name for the thread improves usefulness of error messages.
loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True # shut down music thread when the rest of the program exits
loopThread.start()



os.system('cls & title Windows Installer ~ unofficialdxnny')

banner = '''


    (   /'  _/      _  /   __/_ //_ _ 
    |/|///)(/()((/_)  (/)_) /(/(((-/  
            by unofficialdxnny


'''

menu = '''

    [1] Windows XP        [4] Windows 8   
    [2] Windows Vista     [5] Windows 10   
    [3] Windows 7         [6] Windows 11
          

'''
opt = ['1', '2', '3', '4', '5', '6']

while True:
    try:
        os.system('cls')
        print(Colorate.Horizontal(Colors.red_to_blue, f"{banner}", 1))
        print(Colorate.Horizontal(Colors.red_to_blue, f"{menu}", 1))
        print('')
        choice = Write.Input("Select an option : ", Colors.red_to_blue, interval=0.0025)

        if choice == '1':
            ## print(Colorate.Color(Colors.green, f'Installing Windows XP...', True))

            console = Console()
            tasks = [f"Loading Contents", "Retrieving URL", "Checking URL MetaData", "Loading URL", "Checking Internet Connection"]
            for n in range(1, 11):
                with console.status("[bold green]Working on tasks...") as status:
                    while tasks:
                        tim = random.randint(1,6)
                        task = tasks.pop(0)
                        sleep(tim)
                        console.log(f"{task}")
            
            def connect(host='http://google.com'):#
                try:
                    urllib.request.urlopen(host) #Python 3.x
                    return True
                except:
                    return False
                    # test
            
            if connect():
                done = False
                #here is the animation
                def animate():
                    for c in itertools.cycle(['|', '/', '-', '\\']):
                        if done:
                            break
                        sys.stdout.write(Fore.GREEN + '\rInstalling Windows XP ' + c)
                        sys.stdout.flush()
                        time.sleep(1)
                    ## sys.stdout.write(Fore.GREEN + '\rWindows XP Installed')

                t = threading.Thread(target=animate)
                t.start()
                ## playsound.playsound('./assets/sounds/startup7.mp3', True)
    
                response = requests.get("https://bit.ly/WinXPPXniW1002")

                file = open("WindowsXP.iso", "wb")
                file.write(response.content)
                file.close()
                print(Colorate.Color(Colors.green, f'Windows XP ISO Installed', True))  

                #long process here
                time.sleep(10)
                done = True

                sleep(1)
                os.system('cls')
            else:
                pag.keyDown('alt')
                pag.keyDown('F4')
                pag.keyUp('alt')
                pag.keyUp('F4')


                    

            


        elif choice == '2':
            ## print(Colorate.Color(Colors.green, f'Installing Windows Vista', True))  

            console = Console()
            tasks = [f"Loading Contents", "Retrieving URL", "Checking URL MetaData", "Loading URL", "Checking Internet Connection"]
            for n in range(1, 11):
                with console.status("[bold green]Working on tasks...") as status:
                    while tasks:
                        tim = random.randint(1,6)
                        task = tasks.pop(0)
                        sleep(tim)
                        console.log(f"{task}")
            
            def connect(host='http://google.com'):#
                try:
                    urllib.request.urlopen(host) #Python 3.x
                    return True
                except:
                    return False
                    # test
            
            if connect():
                done = False
                #here is the animation
                def animate():
                    for c in itertools.cycle(['|', '/', '-', '\\']):
                        if done:
                            break
                        sys.stdout.write(Fore.GREEN + '\rInstalling Windows Vista ' + c)
                        sys.stdout.flush()
                        time.sleep(1)
                    ## sys.stdout.write(Fore.GREEN + '\rWindows XP Installed')

                t = threading.Thread(target=animate)
                t.start()
                ## playsound.playsound('./assets/sounds/startup7.mp3', True)
    
                response = requests.get("https://bit.ly/WinVistaatsiVniW7002")

                file = open("WindowsXP.iso", "wb")
                file.write(response.content)
                file.close()
                print(Colorate.Color(Colors.green, f'Windows Vista ISO Installed', True))  

                #long process here
                time.sleep(10)
                done = True

                sleep(1)
                os.system('cls')
            else:
                pag.keyDown('alt')
                pag.keyDown('F4')
                pag.keyUp('alt')
                pag.keyUp('F4')

            sleep(1)
            os.system('cls')



        elif choice == '3':
            print(Colorate.Color(Colors.green, f'Installing Windows 7...', True))
      
            sleep(1)
            os.system('cls')


        elif choice == '4':
            print(Colorate.Color(Colors.green, f'Installing Windows 8', True))  
            sleep(1)
            os.system('cls')


        elif choice == '5':
            print(Colorate.Color(Colors.green, f'Installing Windows 10', True)) 
            sleep(1)
            os.system('cls')


        elif choice == '6':
            print(Colorate.Color(Colors.green, f'Installing Windows 11', True)) 
            sleep(1)
            os.system('cls')
        


        elif choice == '':
            print(Colorate.Color(Colors.red, f'Field Cant Be Empty', True))
            sleep(1)
            os.system('cls')



        elif choice != opt:
            print(Colorate.Color(Colors.red, f'Invalid Option, READ!', True))
            sleep(1)
            os.system('cls')

    except KeyboardInterrupt:
        print('')
        print(Colorate.Color(Colors.red, f'Use the cross (X) if you really want to exit.', True))
        sleep(1)
        os.system('cls')
    
    
    except:
        print('')
        print(Colorate.Color(Colors.red, f'You cant do that!', True))
        sleep(1)
        os.system('cls')