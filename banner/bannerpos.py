#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import time
from subprocess import check_call
from colorama import Fore, Style

#Colores
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

os.system("clear")

############################################################

def banner():
	print("""
 \033[1;37m❰----------------------------------------------------------------------------------❱\033[0m

\033[0;34m      ██╗    ██╗██╗███████╗██╗    ██╗  ██╗ █████╗ ████████╗███████╗██████╗ 
\033[0;34m      ██║    ██║██║██╔════╝██║    ██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
\033[0;34m      ██║ █╗ ██║██║█████╗  ██║    ███████║╚█████╔╝   ██║   █████╗  ██████╔╝
\033[0;34m      ██║███╗██║██║██╔══╝  ██║    ██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
\033[0;34m      ╚███╔███╔╝██║██║     ██║    ██║  ██║╚█████╔╝   ██║   ███████╗██║  ██║
 \033[0;34m      ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝                 
  \033[0;34m                                                   parrot edtion !!!!!!
 
  \033[1;34m---< \033[1;39mCREATED BY: \033[1;39mZOD-THE-IMMORTAL   follow at https://github.com/rottingratto \033[1;34m>---\033[0m 
  \033[0;34m                                        CTRL+C TO EXIT TOOL

 \033[1;37m❰----------------------------------------------------------------------------------❱\033[0m
""")

def menu():
	print(""" \033[0;31m[\033[1;37m1\033[0;31m] \033[0;39mstart monitor mode 
 \033[0;31m[\033[1;37m2\033[0;31m] \033[0;39mstop monitor mode
 \033[0;31m[\033[1;37m3\033[0;31m] \033[0;39mcheck wifi interfaces
 \033[0;31m[\033[1;37m4\033[0;31m] \033[0;39mreboot network
 \033[0;31m[\033[1;37m5\033[0;31m] \033[0;39mscan nearby networks 
 \033[0;31m[\033[1;37m6\033[0;31m] \033[0;39mcapture Handshake
 \033[0;31m[\033[1;37m7\033[0;31m] \033[0;39mdecrypt keys
 \033[0;31m[\033[1;37m8\033[0;31m] \033[0;39mattack WPS networks \033[0;39mBully \033[0;32m\033[0m
 \033[0;31m[\033[1;37m9\033[0;31m] \033[0;39mAP flood 
 \033[0;31m[\033[1;37m0\033[0;31m] \033[0;39mEXIT\033[0m\n
""")

banner()
menu()



def goodbye():
  print("""
 \033[1;37m------------------------------------------------------\033[0m   
\033[1;34m    _____  ____   ____  _____  ______     ________ _ 
   / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____| |
  | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__  | |
  | | |_ | |  | | |  | | |  | |  _ < \   / |  __| | |
  | |__| | |__| | |__| | |__| | |_) | | |  | |____|_|
   \_____|\____/ \____/|_____/|____/  |_|  |______(_)\033[0m

     \033[1;31m<\033[1;37mbecome blackhat  - zod-the-immortal \033[1;31m>\033[0m 

 \033[1;37m------------------------------------------------------\033[0m 
                                                   
"""+ WHITE + Style.NORMAL)
