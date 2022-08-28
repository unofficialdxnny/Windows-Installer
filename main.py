import os
import getpass
from pystyle import *
import playsound 
import requests


playsound.playsound('moosiq.mp3', False)

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
opt = [1, 2, 3, 4, 5, 6]
print(Colorate.Horizontal(Colors.red_to_blue, f"{banner}", 1))
print(Colorate.Horizontal(Colors.red_to_blue, f"{menu}", 1))
print('')
while True:
    choice = Write.Input("Select an option : ", Colors.red_to_blue, interval=0.0025)

    if choice == 1:
        print(Colorate.Color(Colors.green, f'Installing Windows XP', True))
        url = 'https://bit.ly/3318e1R'
        data = requests.get(url).content
        with open('./Windows 7/7.iso', 'wb') as handler:
            handler.write(data)
            print(Colorate.Color(Colors.blue, f'Windows 7 ISO Installed', True))    
    elif choice == 2:
        print(Colorate.Color(Colors.green, f'Installing Windows Vista', True))  
    elif choice == 3:
        print(Colorate.Color(Colors.green, f'Installing Windows 7', True))  
    elif choice == 4:
        print(Colorate.Color(Colors.green, f'Installing Windows 8', True))  
    elif choice == 5:
        print(Colorate.Color(Colors.green, f'Installing Windows 10', True)) 
    elif choice == 6:
        print(Colorate.Color(Colors.green, f'Installing Windows 11', True)) 
    elif choice == '':
        print(Colorate.Color(Colors.red, f'Field Cant Be Empty', True))


