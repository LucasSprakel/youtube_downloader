from urllib.parse import urlparse
from pytube import YouTube
from colorama import init, Fore
import os
import sys


init()

var_key = ""
url = ""

def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def insert_link():
    global video
    global url
    url = str(input('Link from youtube video: '))
    try:
        video = YouTube(url)
    except:
        print(Fore.RED + 'Youtube Downloader Error: Invalid Link\n')
        global var_key 
        var_key = str(input(Fore.MAGENTA + 'Press ENTER to continue'))

def download_video():
    if url == "":
        print(Fore.YELLOW + 'Youtube Downloader Warning: Insert Youtube Link First\n')
        global var_key 
        var_key = str(input(Fore.MAGENTA + 'Press ENTER to continue'))
    else:
        video.streams.get_highest_resolution().download('Videos')
        print(Fore.MAGENTA + f'Downloading {video.title}...')


def download_audio():
    if url == "":
        print(Fore.YELLOW + 'Youtube Downloader Warning: Insert Youtube Link First\n')
        global var_key 
        var_key = str(input(Fore.MAGENTA + 'Press ENTER to continue'))
    else:
        video.streams.get_audio_only().download('Audios')
        print(Fore.MAGENTA + f'Downloading {video.title}...')


def credits():
    print(Fore.MAGENTA +
            """       
                         ____        
                        | __ ) _   _ 
                        |  _ \| | | |
                        | |_) | |_| |
                        |____/ \__, |
                               |___/ 
 _                          ____                  _        _ 
| |   _   _  ___ __ _ ___  / ___| _ __  _ __ __ _| | _____| |
| |  | | | |/ __/ _` / __| \___ \| '_ \| '__/ _` | |/ / _ \ |
| |__| |_| | (_| (_| \__ \  ___) | |_) | | | (_| |   <  __/ |
|_____\__,_|\___\__,_|___/ |____/| .__/|_|  \__,_|_|\_\___|_|
                                 |_|      
        
        
        """)
    global var_key 
    var_key = str(input('Press ENTER to continue'))


def help():
    print(Fore.MAGENTA +
        """
Before Download, insert youtube link
    """)
    global var_key 
    var_key = str(input('Press ENTER to continue'))


def menu():
    while True:
        print(Fore.BLUE + """ 

        __   __          _         _          
        \ \ / /__  _   _| |_ _   _| |__   ___ 
         \ V / _ \| | | | __| | | | '_ \ / _ \
          | | (_) | |_| | |_| |_| | |_) |  __/
          |_|\___/ \__,_|\__|\__,_|_.__/ \___|
                          
 ____                      _                 _           
|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                      
                                                                      """)
        print('                                                      ')
        print('                                                      ')
        print(Fore.GREEN + 
              '    (1) Insert Youtube Link     |     (4) Credits ')
        print('    (2) Download Video          |     (5) Help    ')
        print('    (3) Download Audio          |     (6) Leave   ')
        print('                                                      ')
        action = str(input(Fore.CYAN + '        Which action do you want to do: '))
        if action == '1':
            clear()
            insert_link()
            clear()
        elif action == '2':
            clear()
            download_video()
            clear()
        elif action == '3':
            clear()
            download_audio()
            clear()
        elif action == '4':
            clear()
            credits()
            clear()
        elif action == '5':
            clear()
            help()
            clear()
        elif action == '6':
            exit(1)
        else:
            print(Fore.RED + '\nMessage_bot Error: Invalid Action')



    
