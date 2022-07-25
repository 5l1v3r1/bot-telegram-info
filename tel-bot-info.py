import requests
import time, os, platform
from colorama import init, Fore, Back
init()




if platform.uname()[0] == "Linux":
	os.system("clear")
else:
	os.system("cls")




print(Fore.CYAN+"""
             o                                           o                               .oOo       
            O                                           O                      o         O          
  O         o                                           O            O                   o          
 oOo        O                                           o           oOo                  OoO        
  o   .oOo. o  .oOo. .oOoO `OoOo. .oOoO' `oOOoOO.       OoOo. .oOo.  o         O  'OoOo. o    .oOo. 
  O   OooO' O  OooO' o   O  o     O   o   O  o  o       O   o O   o  O         o   o   O O    O   o 
  o   O     o  O     O   o  O     o   O   o  O  O       o   O o   O  o         O   O   o o    o   O 
  `oO `OoO' Oo `OoO' `OoOo  o     `OoO'o  O  o  o       `OoO' `OoO'  `oO       o'  o   O O'   `OoO' 
                         O                                                                          
                      OoO'

created by r4my""")





def start():
	
	print()
	token = input(Fore.BLUE+"enter telegram bot token : ")


	url = "https://api.telegram.org/bot{0}/getMe".format(token)
	req = requests.get(url).json()



	print(Fore.GREEN+"[+] bot id => "+Fore.WHITE+str(req["result"]["id"]))
	time.sleep(0.1)
	print(Fore.GREEN+"[+] bot first name => "+Fore.WHITE+req["result"]["first_name"])
	time.sleep(0.2)
	print(Fore.GREEN+"[+] bot username => "+Fore.WHITE+"@"+req["result"]["username"])
	time.sleep(0.3)
	print(Fore.GREEN+"[+] bot can join groups => "+Fore.WHITE+str(req["result"]["can_join_groups"]))
	time.sleep(0.4)
	print(Fore.GREEN+"[+] bot can read all group messages => "+Fore.WHITE+str(req["result"]["can_read_all_group_messages"]))




	urll = "https://api.telegram.org/bot{0}/Getupdates".format(token)
	reqq = requests.get(urll).json()


	inf = reqq["result"][0]["message"]["from"]
	time.sleep(0.2)
	print(Fore.GREEN+"[+] user id => "+Fore.WHITE+str(inf["id"]))
	time.sleep(0.3)
	print(Fore.GREEN+"[+] user first name => "+Fore.WHITE+inf["first_name"])
	time.sleep(0.4)
	print(Fore.GREEN+"[+] USERNAME => "+Fore.WHITE+"@"+reqq["result"][1]["message"]["from"]["username"])





if __name__ == "__main__":
	start()
