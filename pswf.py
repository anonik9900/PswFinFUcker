#!/usr/bin/env python3
import random
import pyautogui
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
	
	
		


print MenuFont() #ASCII LOGO
print SceltaMenu()
print CreaPassword()

	
	







name = raw_input("Please enter your name:  ")
age = raw_input("Enter your age: ")
bday = raw_input ("Enter your Birthday: ")



def FinalData():
	print "Ti chiami "+name+ " Hai " +age+ " anni e sei nato il " +bday 
print FinalData()
