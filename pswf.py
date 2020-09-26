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
		dog_number = raw_input("Enter the number of animals: ")
		if dog_number == str(1):
			dog_name = raw_input("Enter the animal name: ")
		if dog_number ==str(2):
			dog_name = raw_input("Enter the 1st animal name: ")
			dog_name2 = raw_input("Enter the 2nd animal name: ")
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
	print "comb17: "+nome+cognome+anno_nascita+mese_nascita #name+surname+year of birth+month of birth
	print""
	print "comb18: "+nome+cognome+mese_nascita+anno_nascita #name+surname+month of birth+ year of birth
	print""
	print "comb19: "+cognome+nome+anno_nascita+mese_nascita #surname+name+yearofbith+monthofbirth
	print""
	print "comb20: "+cognome+nome+mese_nascita+anno_nascita #surname+name+monthofbirt+yearofbirth
	
	print""
	print "comb21: "+nome+cognome+anno_nascita+mese_nascita+giorno_nascita #name+surname+year+month+day
	print""
	print "comb22: "+nome+cognome+mese_nascita+anno_nascita+giorno_nascita #name+surname+month+year+day
	print""
	print "comb23: "+nome+cognome+giorno_nascita+mese_nascita+anno_nascita #name+surname+day+month+year
	print""
	print "comb24: "+nome+cognome+giorno_nascita+anno_nascita+mese_nascita #name+surname+day+year+month
	print""
	print "comb25: "+cognome+nome+anno_nascita+mese_nascita+giorno_nascita #surname+name+year+month+day
	print""
	print "comb26: "+cognome+nome+mese_nascita+anno_nascita+giorno_nascita #surname+name+month+year+day
	print""
	print "comb27: "+cognome+nome+giorno_nascita+mese_nascita+anno_nascita #surname+name+day+month+year
	print""
	print "comb28: "+cognome+nome+giorno_nascita+anno_nascita+mese_nascita #surname+name+day+year+month
	print""
	print "comb29: "+nome+giorno_nascita #name+day
	print""
	print "comb30: "+cognome+giorno_nascita #surname+day
	print""
	print "comb31: "+nome+cognome+giorno_nascita #name+surname+day
	print""
	print "comb32: "+nome+giorno_nascita+cognome #name+day+surname
	print""
	print "comb33: "+cognome+nome+giorno_nascita #surname+name+day
	print""
	print "comb34: "+cognome+giorno_nascita+nome #surname+day+name
	
	print""
	print "comb35: "+nome+anno_nascita+cognome #name+year+surname
	print""
	print "comb36: "+cognome+anno_nascita+nome #surname+year+name
	print""
	print "comb37: "+nome+anno_nascita+cognome+mese_nascita #name+year+surname+month
	print""
	print "comb38: "+cognome+anno_nascita+nome+mese_nascita #surname+year+name+month
	print""
	print "comb39: "+nome+mese_nascita+cognome+anno_nascita #name+month+surname+year
	print""
	print "comb40: "+cognome+mese_nascita+nome+anno_nascita #surname+month+name+year
	print""
	print "comb41: "+nome+anno_nascita+mese_nascita+cognome #name+year+month+surname
	print""
	print "comb42: "+nome+mese_nascita+anno_nascita+cognome #name+month+year+surname
	print""
	print "comb43: "+cognome+anno_nascita+mese_nascita+nome #surname+year+month+name
	print""
	print "comb44: "+cognome+mese_nascita+anno_nascita+nome #surname+month+year+name
	
	print""
	print "comb45: "+anno_nascita+mese_nascita+giorno_nascita #YY/MM/DD
	print""
	print "comb46: "+mese_nascita+giorno_nascita+anno_nascita #MM/DD/YY
	print""
	print "comb47: "+giorno_nascita+mese_nascita+anno_nascita #DD/MM/YY
	print""
	print "comb48: "+nome+anno_nascita+mese_nascita+giorno_nascita #name+YY/MM/DD
	print""
	print "comb49: "+nome+mese_nascita+giorno_nascita+anno_nascita #name+MM/DD/YY
	print""
	print "comb50: "+nome+giorno_nascita+mese_nascita+anno_nascita #name+DD/MM/YY
	print""
	print "comb51: "+cognome+anno_nascita+mese_nascita+giorno_nascita #surname+YY/MM/DD
	print""
	print "comb52: "+cognome+mese_nascita+giorno_nascita+anno_nascita #surname+MM/DD/YY
	print""
	print "comb53: "+cognome+giorno_nascita+mese_nascita+anno_nascita #surname+DD/MM/YY
	print""
	print "comb54: "+nome+anno_nascita+mese_nascita+giorno_nascita+cognome #name+YY/MM/DD+surname
	print""
	print "comb55: "+nome+mese_nascita+giorno_nascita+anno_nascita+cognome #name+MM/DD/YY+surname
	print""
	print "comb56: "+nome+giorno_nascita+mese_nascita+anno_nascita+cognome #name+DD/MM/YY+surname
	print""
	print "comb57: "+cognome+anno_nascita+mese_nascita+giorno_nascita+nome #surname+YY/MM/DD+name
	print""
	print "comb58: "+cognome+mese_nascita+giorno_nascita+anno_nascita+nome #surname+MM/DD/YY+name
	print""
	print "comb59: "+cognome+giorno_nascita+mese_nascita+anno_nascita+nome #surname+DD/MM/YY+name
	
	
	#Animale
	if dog_name_value ==1 and dog_number==str(1):		
		print""
		print "combAnimal: "+nome+cognome+dog_name
	if dog_name_value ==1 and dog_number==str(2):
		print""
		print "combAnimal1: "+nome+cognome+dog_name
		print "combAnimal2: "+nome+cognome+dog_name2
	elif dog_name_value ==2:
		print ""
	else:
		print""
	
	
	print""
	print""
	print"---------------------------------------------------------------------------"
	print"---------------------------------------------------------------------------"
	print""
	print "                             END PASSWORD"
	print""
	print"---------------------------------------------------------------------------"
	print"---------------------------------------------------------------------------"
	print""	


print MenuFont() #ASCII LOGO
print SceltaMenu()
print CreaPassword()

	
	
