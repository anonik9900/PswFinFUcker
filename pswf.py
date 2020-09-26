#!/usr/bin/env python3
import random
import string
import subprocess #Process commands
import socket #Process socket data
import pyfiglet
import sys






def MenuFont():
		ascii_banner = pyfiglet.figlet_format("PSW-FINFUCK")
		print(ascii_banner)
		return "+++By Anonik V1.0+++"
	




def MenuCHoice():
	print")-------------------------------------------("
	print")-                                         -("
	print")---------Build YOur ExPlOiT PsW------------("
	print")-----                                 -----("
	print")--------------By Anonik&Others-------------("
	print")-----                                 -----("
	print")-------------------------------------------("
	
	print""
	
	print"        -----          Menu         -----"
	print"         ()--------------------------()"
	print"         ()---1*Create Psw with comb-()"
	print""




def SceltaMenu():
	scelta = raw_input("Type 1 to enter Or 2 To Exit ")

	if scelta == str("1"):
		return MenuCHoice() #MEnu
	
	elif scelta == str("2"):
		sys.exit()
	
	else:
		print "Invalid input - try again"
		print""
		return SceltaMenu()
		
		
		

def CreaPassword():
	print ""
	print ")------- Password Creator for Exploit -------("
	print ""
	nome = raw_input("Please enter your Victim name:  ")
	print ""
	cognome = raw_input("Please enter your Victim Surname:  ")
	print ""
	anno_nascita = raw_input("Enter your victim year of birth:  ")
	print ""
	mese_nascita = raw_input("Enter your victim month of birth: ")
	print ""
	giorno_nascita = raw_input("Enter your victim day of birth: ")
	print ""
	
	#If se ha il cane
	has_dog = raw_input("Yor victim has an animal?: ")
	
	if has_dog == "yes":
		dog_name = raw_input("Enter the animal name: ")
		dog_name_value =1
		
	elif has_dog == "no":
		dog_name = ""
		dog_name_value =2
		
	else:
		print CreaPassword()
	

	

	#print "La password e':  "+nome+ " " +cognome
	
	#Combinazione Password
	print""
	print""
	print"---------------------------------------------------------------------------"
	print"---------------------------------------------------------------------------"
	print""
	print "                             Genero Password"
	print""
	print"---------------------------------------------------------------------------"
	print"---------------------------------------------------------------------------"
	print""
	print "comb1: "+nome+cognome #name + surname
	print""
	print "comb2: "+nome+ " "+cognome #name + surnamen + with space
	print""
	print "comb3: "+nome+cognome+anno_nascita #name+surname+year of birth
	print""
	print "comb4: "+cognome+nome #surname+name
	print""
	print "comb5: "+cognome+ " "+nome #surname + name with space
	print""
	print "comb6: "+cognome+nome+anno_nascita #surname + name + year of birth
	print""
	print "comb7: "+nome+anno_nascita #name+year of birth
	print""
	print "comb8: "+cognome+anno_nascita#surname+year of birth
	print""
	print "comb9: "+nome+cognome+mese_nascita #name+surname+month of birth
	print""
	print "comb10: "+cognome+nome+mese_nascita #surname+name+month of birth
	print""
	print "comb11: "+nome+mese_nascita+cognome #name+month of birth+surname
	print""
	print "comb12: "+cognome+mese_nascita+nome #surname+month of birth+name
	print""
	print "comb13: "+nome+anno_nascita+mese_nascita #name+year-of-birth+month-of-birth
	print""
	print "comb14: "+nome+mese_nascita+anno_nascita #name+month-of-birth-year-of-birth
	print""
	print "comb15: "+cognome+anno_nascita+mese_nascita #surname+year-of-birth+month-of-birth
	print""
	print "comb16: "+cognome+mese_nascita+anno_nascita #surname+month-of-birth-year-of-birth 
	print""
	
		


print MenuFont() #ASCII LOGO
print SceltaMenu()
print CreaPassword()

	
	












