#!/usr/bin/env python3
import random
import string
import subprocess #Process commands
import socket #Process socket data
import pyfiglet
import sys
import os
from subprocess import call

def SplashScreen():
	print("         .            )        )")
	print("                  (  (|              .")
	print("              )   )\/ ( ( (")
	print("      *  (   ((  /     ))\))  (  )    )")
	print("    (     \   )\(          |  ))( )  (|")
	print("    >)     ))/   |          )/  \((  ) \ ")
	print("    (     (      .        -.     V )/   )(    ( ")
	print("    \   /     .   \            .       \))   ))")
	print("       )(      (  | |   )            .    (  /")
	print("      )(    ,'))     \ /          \( `.    )")
	print("      (\>  ,'/__      ))            __`.  /")
	print("     ( \   | /  ___   ( \/     ___   \ | ( (")
	print("      \.)  |/  /   \__      __/   \   \|  ))")
	print("     .  \. |>  \      | __ |      /   <|  /")
	print("          )/    \____/ :..: \____/     \ <")
	print("   )   \ (|__  .      / ;: \          __| )  (")
	print("  ((    )\)  ~--_     --  --      _--~    /  ))")
	print("   \    (    |  ||               ||  |   (  /")
	print("         \.  |  ||_             _||  |  /")
	print("           > :  |  ~V+-I_I_I-+V~  |  : (.")
	print("          (  \:  T\   _     _   /T  : ./")
	print("           \  :    T^T T-+-T T^T    ;<")
	print("            \..`_       -+-       _'  )")
	print("  )            . `--=.._____..=--'. ./         (")
	print(" ((     ) (          )             (     ) (   )> ")
	print("  > \/^/) )) (   ( /(.      ))     ))._/(__))./ (_.")
	print(" (  _../ ( \))    )   \ (  / \.  ./ ||  ..__:|  _. \ ")
	print(" |  \__.  ) |   (/  /: :)) |   \/   |(  <.._  )|  ) )")
	print("))  _./   |  )  ))  __  <  | :(     :))   .//( :  : |")
	print("(: <     ):  --:   ^  \  )(   )\/:   /   /_/ ) :._) :")
	print(" \..)   (_..  ..  :    :  : .(   \..:..    ./__.  ./")
	print("            ^    ^      \^ ^           ^\/^     ^ JaL")




def MenuFont():
		ascii_banner = pyfiglet.figlet_format("PSW-FINFUCK")
		print(ascii_banner)
		return "+++By Anonik V1.0+++"
	


def CreditsMenu():
	print("")
	print("")
	print("()==========================================()")
	print("()                                          ()")
	print("()               CREDITS BY:                ()")
	print("()                                          ()")
	print("()       *)General Scripting: Anonik        ()")
	print("()                                          ()")
	print("()      *)crucnh.py Scripting By derv82     ()")
	print("()                                          ()")
	print("()==========================================()")
	
	print("")
	print("")
	
	print("()==========================================()")
	print("()             SOCIAL - GITHUB              ()")
	print("()==========================================()")
	print("")
	print("()=Github Anonik: https://github.com/anonik9900")
	print("()=Github derv: https://github.com/derv82")
	print("")
	print("()==========================================()")
	print("()           END CREDITS AND SOCIAL         ()")
	print("()==========================================()")
	
	print("")
	print("")
	creditChoice = input("Type 1) to go home or 2) to exit: ")
	
	if creditChoice == str("1"):
		os.system('clear')
		return SceltaMenu()
	
	if creditChoice == str("2"):
		sys.exit()
	
	else:
		print("Error... Invalid command. Closing program")
		sys.exit()
	


def MenuCHoice():
	print(")-------------------------------------------(")
	print(")-                                         -(")
	print(")---------Build YOur ExPlOiT PsW------------(")
	print(")-----                                 -----(")
	print(")--------------By Anonik&Others-------------(")
	print(")-----                                 -----(")
	print(")-------------------------------------------(")
	
	print("")
	
	print("        -----          Menu         -----")
	print("         ()--------------------------()")
	print("         ()---1*Create Psw with comb-()")
	print("")
	
	




def Menucrunch():
	print("")
	print("()---------------------------------()")
	print("()-----------/Crunch Tool\---------()")
	print("()----------|             |--------()")
	print("()----------\_____________/--------()")
	print("()---------------------------------()")
	
	
	print(SplashScreen())
	
	vic = input ("Please enter a value for create new wordlist: ")
	minChar = input("Enter the minimum word lenght: ")
	maxChar = input("Enter the maximum word lenght: ")
	print("")
	
	saveFile = input("Did you save all words inside a file ?: [Y]or[N] ")
	
	if saveFile == str("Y") or saveFile == str("y"):
		nameSfile = input("Enter the name of your wordlist is saved ex: (word.txt) : ")
		print("")
		print("Success")
		os.system('python3 crunch.py -m '+minChar+' -M '+maxChar +' -c '+vic+ ' -o '+nameSfile)
		#call(['python3', 'crunch.py -m '+minChar+' -M '+maxChar +' -c '+vic+ ' -o '+nameSfile])	
		#call(['python3 crunch.py -m '+minChar+' -M '+maxChar +' -c '+vic+ ' -o '+nameSfile])
		print("")
		print("()================================()")
		print("()            COMPLETED           ()")
		print("()================================()")
		print("")
		print("The wordlist called "+nameSfile+" is saved inside the pswf.py folder !")
		print("")
		sys.exit()
	
	if saveFile == str("N") or saveFile == str("n"):
		print("Go to the next step \../ ")
		print("")
		call(["python3", "crunch.py -m "+minChar+" -M "+maxChar +" -c "+vic])
		#os.system('python crunch.py -m '+minChar+' -M '+maxChar +' -c '+vic)
		print("")
		print("()================================()")
		print("()            COMPLETED           ()")
		print("()================================()")
		print("")
		sys.exit()
		
	else:
		print("Error.... :(")
		sys.exit()
    

	
	#os.system('cowsay ' + vic)
	
	#os.system('python crunch.py -m 1 -M 3'+' -c '+vic)
	
	#os.system(mark)
	#os.system('%s %s' % ('ls', '-l'))
	sys.exit()

def SceltaMenu():
	scelta = input("Type (1) to enter, (2) To Exit, (3) to use the crunch Tool \nor (4) to see the credits ")

	if scelta == str("1"):
		return MenuCHoice() #MEnu
	
	if scelta == str("2"):
		sys.exit()
		
	if scelta == str("3"):
		return Menucrunch() #MenuCrunch
	
	if scelta == str("4"):
		return CreditsMenu() #Menu Credits
	
	else:
		print("Invalid input - try again")
		print("")
		return SceltaMenu()
		
		
		

def CreaPassword():
	print("")
	print(")------- Password Creator for Exploit -------(")
	print("")
	nome = input("Please enter your Victim name:  ")
	print("")
	cognome = input("Please enter your Victim Surname:  ")
	print("")
	anno_nascita = input("Enter your victim year of birth:  ")
	print("")
	mese_nascita = input("Enter your victim month of birth: ")
	print("")
	giorno_nascita = input("Enter your victim day of birth: ")
	print("")
	
	#If se ha il cane
	has_dog = input("Yor victim has an animal?: ")
	if has_dog == "yes":
		dog_number = input("Enter the number of animals: ")
		if dog_number == str(1):
			dog_name = input("Enter the animal name: ")
		if dog_number ==str(2):
			dog_name = input("Enter the 1st animal name: ")
			dog_name2 = input("Enter the 2nd animal name: ")
		if dog_number ==str(3):
			dog_name = input("Enter the 1st animal name: ")
			dog_name2 = input("Enter the 2nd animal name: ")
			dog_name3 = input("Enter the 3td animal name: ")
		dog_name_value =1
		
	elif has_dog == "no":
		dog_name = ""
		dog_name_value =2
		
	else:
		print(CreaPassword())
	

	

	#print "La password e':  "+nome+ " " +cognome
	
	#Combinazione Password
	print("")
	print("")
	print("---------------------------------------------------------------------------")
	print("---------------------------------------------------------------------------")
	print("")
	print("                             Genero Password")
	print("")
	print("---------------------------------------------------------------------------")
	print("---------------------------------------------------------------------------")
	print("")
	print("comb1: "+nome+cognome) #name + surname
	print("comb2: "+nome+ " "+cognome) #name + surnamen + with space
	print("comb3: "+nome+cognome+anno_nascita) #name+surname+year of birth
	print("comb4: "+cognome+nome) #surname+name
	print("comb5: "+cognome+ " "+nome) #surname + name with space
	print("comb6: "+cognome+nome+anno_nascita) #surname + name + year of birth
	print("comb7: "+nome+anno_nascita) #name+year of birth
	print("comb8: "+cognome+anno_nascita)#surname+year of birth
	print("comb9: "+nome+cognome+mese_nascita) #name+surname+month of birth
	print("comb10: "+cognome+nome+mese_nascita) #surname+name+month of birth
	print("comb11: "+nome+mese_nascita+cognome) #name+month of birth+surname
	print("comb12: "+cognome+mese_nascita+nome) #surname+month of birth+name
	
	print("comb13: "+nome+anno_nascita+mese_nascita) #name+year-of-birth+month-of-birth
	print("comb14: "+nome+mese_nascita+anno_nascita) #name+month-of-birth-year-of-birth
	print("comb15: "+cognome+anno_nascita+mese_nascita) #surname+year-of-birth+month-of-birth
	print("comb16: "+cognome+mese_nascita+anno_nascita) #surname+month-of-birth-year-of-birth 
	

	print("comb17: "+nome+cognome+anno_nascita+mese_nascita) #name+surname+year of birth+month of birth
	print("comb18: "+nome+cognome+mese_nascita+anno_nascita) #name+surname+month of birth+ year of birth
	print("comb19: "+cognome+nome+anno_nascita+mese_nascita) #surname+name+yearofbith+monthofbirth
	print("comb20: "+cognome+nome+mese_nascita+anno_nascita) #surname+name+monthofbirt+yearofbirth
	
	print("comb21: "+nome+cognome+anno_nascita+mese_nascita+giorno_nascita) #name+surname+year+month+day
	print("comb22: "+nome+cognome+mese_nascita+anno_nascita+giorno_nascita) #name+surname+month+year+day
	print("comb23: "+nome+cognome+giorno_nascita+mese_nascita+anno_nascita) #name+surname+day+month+year
	print("comb24: "+nome+cognome+giorno_nascita+anno_nascita+mese_nascita) #name+surname+day+year+month
	print("comb25: "+cognome+nome+anno_nascita+mese_nascita+giorno_nascita) #surname+name+year+month+day
	print("comb26: "+cognome+nome+mese_nascita+anno_nascita+giorno_nascita) #surname+name+month+year+day
	print("comb27: "+cognome+nome+giorno_nascita+mese_nascita+anno_nascita) #surname+name+day+month+year
	print("comb28: "+cognome+nome+giorno_nascita+anno_nascita+mese_nascita) #surname+name+day+year+month
	print("comb29: "+nome+giorno_nascita) #name+day
	print("comb30: "+cognome+giorno_nascita) #surname+day
	print("comb31: "+nome+cognome+giorno_nascita) #name+surname+day
	print("comb32: "+nome+giorno_nascita+cognome) #name+day+surname
	print("comb33: "+cognome+nome+giorno_nascita) #surname+name+day
	print("comb34: "+cognome+giorno_nascita+nome) #surname+day+name
	
	print("comb35: "+nome+anno_nascita+cognome) #name+year+surname
	print("comb36: "+cognome+anno_nascita+nome) #surname+year+name
	print("comb37: "+nome+anno_nascita+cognome+mese_nascita) #name+year+surname+month
	print("comb38: "+cognome+anno_nascita+nome+mese_nascita) #surname+year+name+month
	print("comb39: "+nome+mese_nascita+cognome+anno_nascita) #name+month+surname+year
	print("comb40: "+cognome+mese_nascita+nome+anno_nascita) #surname+month+name+year
	print("comb41: "+nome+anno_nascita+mese_nascita+cognome) #name+year+month+surname
	print("comb42: "+nome+mese_nascita+anno_nascita+cognome) #name+month+year+surname
	print("comb43: "+cognome+anno_nascita+mese_nascita+nome) #surname+year+month+name
	print("comb44: "+cognome+mese_nascita+anno_nascita+nome) #surname+month+year+name
	print("comb45: "+anno_nascita+mese_nascita+giorno_nascita) #YY/MM/DD
	print("comb46: "+mese_nascita+giorno_nascita+anno_nascita) #MM/DD/YY
	print("comb47: "+giorno_nascita+mese_nascita+anno_nascita) #DD/MM/YY
	print("comb48: "+nome+anno_nascita+mese_nascita+giorno_nascita) #name+YY/MM/DD
	print("comb49: "+nome+mese_nascita+giorno_nascita+anno_nascita) #name+MM/DD/YY
	print("comb50: "+nome+giorno_nascita+mese_nascita+anno_nascita) #name+DD/MM/YY
	print("comb51: "+cognome+anno_nascita+mese_nascita+giorno_nascita) #surname+YY/MM/DD
	print("comb52: "+cognome+mese_nascita+giorno_nascita+anno_nascita) #surname+MM/DD/YY
	print("comb53: "+cognome+giorno_nascita+mese_nascita+anno_nascita) #surname+DD/MM/YY
	print("comb54: "+nome+anno_nascita+mese_nascita+giorno_nascita+cognome) #name+YY/MM/DD+surname
	print("comb55: "+nome+mese_nascita+giorno_nascita+anno_nascita+cognome) #name+MM/DD/YY+surname
	print("comb56: "+nome+giorno_nascita+mese_nascita+anno_nascita+cognome) #name+DD/MM/YY+surname
	print("comb57: "+cognome+anno_nascita+mese_nascita+giorno_nascita+nome) #surname+YY/MM/DD+name
	print("comb58: "+cognome+mese_nascita+giorno_nascita+anno_nascita+nome) #surname+MM/DD/YY+name
	print("comb59: "+cognome+giorno_nascita+mese_nascita+anno_nascita+nome) #surname+DD/MM/YY+name
	
	
	#Animale
	if dog_name_value ==1 and dog_number==str(1):		
		print("")
		print("combAnimal1: "+nome+cognome+dog_name) #name+surname+animal
		print("combAnimal2: "+cognome+nome+dog_name) #surname+name+animal
		print("combAnimal3: "+dog_name+nome+cognome) #animal+name+surname
		print("combAnimal4: "+dog_name+cognome+nome) #animal+surname+name
		print("combAnimal5: "+nome+cognome+dog_name+anno_nascita) #name+surname+animal+year
		print("combAnimal6: "+cognome+nome+dog_name+anno_nascita) #surname+name+animal+year
		
		print("combAnimal7: "+nome+dog_name) #name+animal
		print("combAnimal8: "+dog_name+nome) #animal+name
		print("combAnimal9: "+cognome+dog_name) #surname+animal
		print("combAnimal10: "+dog_name+cognome) #animal+surname
		
		print("combAnimal11: "+dog_name+anno_nascita) #animal+year
		print("combAnimal12: "+dog_name+giorno_nascita) #animal+day
		print("combAnimal13: "+dog_name+mese_nascita) #animal+month
		
		print("combAnimal14: "+anno_nascita+dog_name) #year+animal
		print("combAnimal15: "+mese_nascita+dog_name) #month+animal
		print("combAnimal16: "+giorno_nascita+dog_name) #day+animal
		
		print("combAnimal17: "+nome+anno_nascita+dog_name) #name+year+animal
		print("combAnimal18: "+nome+mese_nascita+dog_name) #name+month+animal
		print("combAnimal19: "+nome+giorno_nascita+dog_name) #name+day+animal
		
		print("combAnimal20: "+nome+dog_name+anno_nascita) #name+animal+year
		print("combAnimal21: "+nome+dog_name+mese_nascita) #name+animal+month
		print("combAnimal22: "+nome+dog_name+giorno_nascita) #name+animal+day
		
		print("combAnimal23: "+dog_name+nome+anno_nascita) #animal+name+year
		print("combAnimal24: "+dog_name+nome+mese_nascita) #animal+name+month
		print("combAnimal25: "+dog_name+nome+giorno_nascita) #animal+name+day
		print("combAnimal26: "+dog_name+anno_nascita+nome) #animal+year+name
		print("combAnimal27: "+dog_name+mese_nascita+nome) #animal+month+name
		print("combAnimal28: "+dog_name+giorno_nascita+nome) #animal+day+name
		
		print("combAnimal29: "+cognome+anno_nascita+dog_name) #surname+year+animal
		print("combAnimal30: "+cognome+mese_nascita+dog_name) #surname+month+animal
		print("combAnimal31: "+cognome+giorno_nascita+dog_name) #surname+day+animal
		
		print("combAnimal32: "+cognome+dog_name+anno_nascita) #surname+animal+year
		print("combAnimal33: "+cognome+dog_name+mese_nascita) #surname+animal+month
		print("combAnimal34: "+cognome+dog_name+giorno_nascita) #surname+animal+day
		
		print("combAnimal35: "+dog_name+cognome+anno_nascita) #animal+surname+year
		print("combAnimal36: "+dog_name+cognome+mese_nascita) #animal+surname+month
		print("combAnimal37: "+dog_name+cognome+giorno_nascita) #animal+surname+day
		print("combAnimal38: "+dog_name+anno_nascita+cognome) #animal+year+surname
		print("combAnimal39: "+dog_name+mese_nascita+cognome) #animal+month+surname
		print("combAnimal40: "+dog_name+giorno_nascita+cognome) #animal+day+surname
		
		print("combAnimal41: "+dog_name+nome+anno_nascita+cognome) #animal+name+year+surname
		print("combAnimal42: "+dog_name+nome+anno_nascita+mese_nascita+cognome) #animal+name+year+month+surname
		print("combAnimal43: "+dog_name+nome+anno_nascita+mese_nascita+giorno_nascita+cognome) #animal+name+year+month+day+surname
		print("combAnimal44: "+dog_name+nome+anno_nascita+mese_nascita+cognome+giorno_nascita) #animal+name+year+month+surname+day
		print("combAnimal45: "+dog_name+nome+anno_nascita+giorno_nascita+cognome+mese_nascita) #animal+name+year+day+surname+month
		print("combAnimal46: "+dog_name+nome+mese_nascita+giorno_nascita+cognome+anno_nascita) #animal+name+month+day+surname+year
		print("combAnimal47: "+nome+dog_name+anno_nascita+cognome+mese_nascita) #name+animal+year+surname+month
		print("combAnimal48: "+nome+dog_name+mese_nascita+cognome+giorno_nascita) #name+animal+month+surname+day
		print("combAnimal49: "+nome+dog_name+giorno_nascita+cognome+anno_nascita) #name+animal+day+surname+year
		print("combAnimal50: "+cognome+dog_name+anno_nascita+nome+mese_nascita) #surname+animal+year+name+month
		print("combAnimal51: "+cognome+dog_name+mese_nascita+nome+giorno_nascita) #surname+animal+month+name+day
		print("combAnimal52: "+cognome+dog_name+giorno_nascita+nome+anno_nascita) #surname+animal+day+name+year
		
	if dog_name_value ==1 and dog_number==str(2):
		print("")
		print("combAnimal1: "+nome+cognome+dog_name) #name+surname+animal1
		print("combAnimal2: "+cognome+nome+dog_name) #surname+name+animal
		print("combAnimal3: "+dog_name+nome+cognome) #animal+name+surname
		print("combAnimal4: "+dog_name+cognome+nome) #animal+surname+name
		print("combAnimal5: "+nome+cognome+dog_name+anno_nascita) #name+surname+animal+year
		print("combAnimal6: "+cognome+nome+dog_name+anno_nascita) #surname+name+animal+year
		
		print("combAnimal7: "+nome+dog_name) #name+animal
		print("combAnimal8: "+dog_name+nome) #animal+name
		print("combAnimal9: "+cognome+dog_name) #surname+animal
		print("combAnimal10: "+dog_name+cognome) #animal+surname
		
		print("combAnimal11: "+dog_name+anno_nascita) #animal+year
		print("combAnimal12: "+dog_name+giorno_nascita) #animal+day
		print("combAnimal13: "+dog_name+mese_nascita) #animal+month
		
		print("combAnimal14: "+anno_nascita+dog_name) #year+animal
		print("combAnimal15: "+mese_nascita+dog_name) #month+animal
		print("combAnimal16: "+giorno_nascita+dog_name) #day+animal
		
		print("combAnimal17: "+nome+anno_nascita+dog_name) #name+year+animal
		print("combAnimal18: "+nome+mese_nascita+dog_name) #name+month+animal
		print("combAnimal19: "+nome+giorno_nascita+dog_name) #name+day+animal
		
		print("combAnimal20: "+nome+dog_name+anno_nascita) #name+animal+year
		print("combAnimal21: "+nome+dog_name+mese_nascita) #name+animal+month
		print("combAnimal22: "+nome+dog_name+giorno_nascita) #name+animal+day
		
		print("combAnimal23: "+dog_name+nome+anno_nascita) #animal+name+year
		print("combAnimal24: "+dog_name+nome+mese_nascita) #animal+name+month
		print("combAnimal25: "+dog_name+nome+giorno_nascita) #animal+name+day
		print("combAnimal26: "+dog_name+anno_nascita+nome) #animal+year+name
		print("combAnimal27: "+dog_name+mese_nascita+nome) #animal+month+name
		print("combAnimal28: "+dog_name+giorno_nascita+nome) #animal+day+name
		
		print("combAnimal29: "+cognome+anno_nascita+dog_name) #surname+year+animal
		print("combAnimal30: "+cognome+mese_nascita+dog_name) #surname+month+animal
		print("combAnimal31: "+cognome+giorno_nascita+dog_name) #surname+day+animal
		
		print("combAnimal32: "+cognome+dog_name+anno_nascita) #surname+animal+year
		print("combAnimal33: "+cognome+dog_name+mese_nascita) #surname+animal+month
		print("combAnimal34: "+cognome+dog_name+giorno_nascita) #surname+animal+day
		
		print("combAnimal35: "+dog_name+cognome+anno_nascita) #animal+surname+year
		print("combAnimal36: "+dog_name+cognome+mese_nascita) #animal+surname+month
		print("combAnimal37: "+dog_name+cognome+giorno_nascita) #animal+surname+day
		print("combAnimal38: "+dog_name+anno_nascita+cognome) #animal+year+surname
		print("combAnimal39: "+dog_name+mese_nascita+cognome) #animal+month+surname
		print("combAnimal40: "+dog_name+giorno_nascita+cognome) #animal+day+surname
		
		print("combAnimal41: "+dog_name+nome+anno_nascita+cognome) #animal+name+year+surname
		print("combAnimal42: "+dog_name+nome+anno_nascita+mese_nascita+cognome) #animal+name+year+month+surname
		print("combAnimal43: "+dog_name+nome+anno_nascita+mese_nascita+giorno_nascita+cognome) #animal+name+year+month+day+surname
		print("combAnimal44: "+dog_name+nome+anno_nascita+mese_nascita+cognome+giorno_nascita) #animal+name+year+month+surname+day
		print("combAnimal45: "+dog_name+nome+anno_nascita+giorno_nascita+cognome+mese_nascita) #animal+name+year+day+surname+month
		print("combAnimal46: "+dog_name+nome+mese_nascita+giorno_nascita+cognome+anno_nascita) #animal+name+month+day+surname+year
		print("combAnimal47: "+nome+dog_name+anno_nascita+cognome+mese_nascita) #name+animal+year+surname+month
		print("combAnimal48: "+nome+dog_name+mese_nascita+cognome+giorno_nascita) #name+animal+month+surname+day
		print("combAnimal49: "+nome+dog_name+giorno_nascita+cognome+anno_nascita) #name+animal+day+surname+year
		print("combAnimal50: "+cognome+dog_name+anno_nascita+nome+mese_nascita) #surname+animal+year+name+month
		print("combAnimal51: "+cognome+dog_name+mese_nascita+nome+giorno_nascita) #surname+animal+month+name+day
		print("combAnimal52: "+cognome+dog_name+giorno_nascita+nome+anno_nascita) #surname+animal+day+name+year
		
		print("combAnimal Second: "+nome+cognome+dog_name2) #name+surname+animal2
		
		
	if dog_name_value ==1 and dog_number==str(3):
		print("")
		print("combAnimal1: "+nome+cognome+dog_name) #name+surname+animal1
		print("combAnimal2: "+cognome+nome+dog_name) #surname+name+animal
		print("combAnimal3: "+dog_name+nome+cognome) #animal+name+surname
		print("combAnimal4: "+dog_name+cognome+nome) #animal+surname+name
		print("combAnimal5: "+nome+cognome+dog_name+anno_nascita) #name+surname+animal+year
		print("combAnimal6: "+cognome+nome+dog_name+anno_nascita) #surname+name+animal+year
		
		print("combAnimal7: "+nome+dog_name) #name+animal
		print("combAnimal8: "+dog_name+nome) #animal+name
		print("combAnimal9: "+cognome+dog_name) #surname+animal
		print("combAnimal10: "+dog_name+cognome) #animal+surname
		
		print("combAnimal11: "+dog_name+anno_nascita) #animal+year
		print("combAnimal12: "+dog_name+giorno_nascita) #animal+day
		print("combAnimal13: "+dog_name+mese_nascita) #animal+month
		
		print("combAnimal14: "+anno_nascita+dog_name) #year+animal
		print("combAnimal15: "+mese_nascita+dog_name) #month+animal
		print("combAnimal16: "+giorno_nascita+dog_name) #day+animal
		
		print("combAnimal17: "+nome+anno_nascita+dog_name) #name+year+animal
		print("combAnimal18: "+nome+mese_nascita+dog_name) #name+month+animal
		print("combAnimal19: "+nome+giorno_nascita+dog_name) #name+day+animal
		
		print("combAnimal20: "+nome+dog_name+anno_nascita) #name+animal+year
		print("combAnimal21: "+nome+dog_name+mese_nascita) #name+animal+month
		print("combAnimal22: "+nome+dog_name+giorno_nascita) #name+animal+day
		
		print("combAnimal23: "+dog_name+nome+anno_nascita) #animal+name+year
		print("combAnimal24: "+dog_name+nome+mese_nascita) #animal+name+month
		print("combAnimal25: "+dog_name+nome+giorno_nascita) #animal+name+day
		print("combAnimal26: "+dog_name+anno_nascita+nome) #animal+year+name
		print("combAnimal27: "+dog_name+mese_nascita+nome) #animal+month+name
		print("combAnimal28: "+dog_name+giorno_nascita+nome) #animal+day+name
		
		print("combAnimal29: "+cognome+anno_nascita+dog_name) #surname+year+animal
		print("combAnimal30: "+cognome+mese_nascita+dog_name) #surname+month+animal
		print("combAnimal31: "+cognome+giorno_nascita+dog_name) #surname+day+animal
		
		print("combAnimal32: "+cognome+dog_name+anno_nascita) #surname+animal+year
		print("combAnimal33: "+cognome+dog_name+mese_nascita) #surname+animal+month
		print("combAnimal34: "+cognome+dog_name+giorno_nascita) #surname+animal+day
		
		print("combAnimal35: "+dog_name+cognome+anno_nascita) #animal+surname+year
		print("combAnimal36: "+dog_name+cognome+mese_nascita) #animal+surname+month
		print("combAnimal37: "+dog_name+cognome+giorno_nascita) #animal+surname+day
		print("combAnimal38: "+dog_name+anno_nascita+cognome) #animal+year+surname
		print("combAnimal39: "+dog_name+mese_nascita+cognome) #animal+month+surname
		print("combAnimal40: "+dog_name+giorno_nascita+cognome) #animal+day+surname
		
		print("combAnimal41: "+dog_name+nome+anno_nascita+cognome) #animal+name+year+surname
		print("combAnimal42: "+dog_name+nome+anno_nascita+mese_nascita+cognome) #animal+name+year+month+surname
		print("combAnimal43: "+dog_name+nome+anno_nascita+mese_nascita+giorno_nascita+cognome) #animal+name+year+month+day+surname
		print("combAnimal44: "+dog_name+nome+anno_nascita+mese_nascita+cognome+giorno_nascita) #animal+name+year+month+surname+day
		print("combAnimal45: "+dog_name+nome+anno_nascita+giorno_nascita+cognome+mese_nascita) #animal+name+year+day+surname+month
		print("combAnimal46: "+dog_name+nome+mese_nascita+giorno_nascita+cognome+anno_nascita) #animal+name+month+day+surname+year
		print("combAnimal47: "+nome+dog_name+anno_nascita+cognome+mese_nascita) #name+animal+year+surname+month
		print("combAnimal48: "+nome+dog_name+mese_nascita+cognome+giorno_nascita) #name+animal+month+surname+day
		print("combAnimal49: "+nome+dog_name+giorno_nascita+cognome+anno_nascita) #name+animal+day+surname+year
		print("combAnimal50: "+cognome+dog_name+anno_nascita+nome+mese_nascita) #surname+animal+year+name+month
		print("combAnimal51: "+cognome+dog_name+mese_nascita+nome+giorno_nascita) #surname+animal+month+name+day
		print("combAnimal52: "+cognome+dog_name+giorno_nascita+nome+anno_nascita) #surname+animal+day+name+year
		
		
		print("combAnimalSecond: "+nome+cognome+dog_name2) #name+surname+animal2
		print("combAniaml Thidrd: "+nome+cognome+dog_name3) #name+surname+animal3
	elif dog_name_value ==2:
		print("")
	else:
		print("")
	
	
	print("")
	print("")
	print("---------------------------------------------------------------------------")
	print("---------------------------------------------------------------------------")
	print("")
	print("                             END PASSWORD")
	print("")
	print("---------------------------------------------------------------------------")
	print("---------------------------------------------------------------------------")
	print("")	


print(MenuFont()) #ASCII LOGO
print(SceltaMenu())
print(CreaPassword())

	
	
