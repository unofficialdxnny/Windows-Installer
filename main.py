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


elevate()

playsound('moosiq.mp3', False)


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
            print(Colorate.Color(Colors.green, f'Installing Windows XP', True))
            sleep(1)
            os.system('cls')


        elif choice == '2':
            print(Colorate.Color(Colors.green, f'Installing Windows Vista', True))  
            sleep(1)
            os.system('cls')



        elif choice == '3':
            print(Colorate.Color(Colors.green, f'Installing Windows 7', True))
            ## playsound.playsound('./assets/sounds/startup7.mp3', True)
  
            ## url = 'https://bit.ly/3318e1R'
            ## data = requests.get(url).content
            ## with open('./Windows 7/7.iso', 'wb') as handler:
            ##     handler.write(data)
            
            wget.download('https://bit.ly/3318e1R')
            
            print(Colorate.Color(Colors.green, f'Windows 7 ISO Installed', True))  
            print(Colorate.Color(Colors.green, f'Making Bootable USB...', True))
            print(Colorate.Color(Colors.red_to_blue, f'Inserted USB? Press "Enter"', True))
            if kb.read_key('enter'):
                os.system('diskpart')
                os.system('list disk')
                print(Colorate.Color(Colors.red_to_blue, f'Type "Disk #" of your disk', True))
                disk = Write.Input("type 'Disk #' : ", Colors.red_to_blue, interval=0.0025)
                os.system(disk)
                print(Colorate.Color(Colors.red_to_blue, f'To make a pendrive bootable, there is a need to format it to clean the existing data. Make sure you made a backup.', True))
                print(Colorate.Color(Colors.red_to_blue, f'Press "Enter" once done.', True))
                if kb.read_key('enter'):
                    print(Colorate.Color(Colors.red_to_blue, f'Cleaning the disk.', True))
                    os.system('clean')
                    print(Colorate.Color(Colors.green, f'Successful...', True))
                    print(Colorate.Color(Colors.red_to_blue, f'Making the disk bootable.', True))
                    os.system('create partition primary')
                    print(Colorate.Color(Colors.green, f'Successful...', True))
                    print(Colorate.Color(Colors.red_to_blue, f'Selecting correct partition.', True))
                    os.system('select partition 1')
                    print(Colorate.Color(Colors.green, f'Successful...', True))
                    print(Colorate.Color(Colors.red_to_blue, f'Formatting Drive', True))
                    os.system('format=fs NTFS')
                    print(Colorate.Color(Colors.green, f'Successful...', True))
                    print(Colorate.Color(Colors.red_to_blue, f'Activating Bootable Drive', True))
                    os.system('active')
                    print(Colorate.Color(Colors.green, f'Successful...', True))
                    print(Colorate.Color(Colors.red_to_blue, f'Exiting DISKPART', True))
                    os.system('exit')
                    print(Colorate.Color(Colors.green, f'Finished', True))
                    source_dir = Write.Input("path/to/source/directory :  ", Colors.red_to_blue, interval=0.0025)
                    target_dir = Write.Input("path/to/destination/directory : ", Colors.red_to_blue, interval=0.0025)
                    
                    file_names = os.listdir(source_dir)
                        
                    for file_name in file_names:
                        shutil.move(os.path.join(source_dir, file_name), target_dir)
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