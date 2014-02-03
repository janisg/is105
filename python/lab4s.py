# -*- coding: latin-1 -*-

#
#  IS-105 LAB4
#
#  lab4.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys
import os
import subprocess
import re

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': '-', \
			'student2': '-', \
            'student3': '-', \
}

# Ikke endre denne funksjonen
# Denne informasjonen skal vises i resultate av din kjøring
def min_sys_info():
	"""
	Viser byteorder (litte eller big endian)
   
	"""
	print "byteorder: " + sys.byteorder
	print "os data: "
	print os.uname()
	print "os bruker: " + os.getlogin()

#
#  Oppgave 1
#    



#
#  Oppgave 2
#    Funksjonen ... 
#
#    
#



#
#  Oppgave 3
#  	Formål:
#   	Jobbe med symboler (bokstaver og tall)
#	 	Utforske str.find funksjon fra Python Standard Library
#		Aktuelt på eksamen:
#    
#	Beskrivelse:
#
#	Eksempler:

def funksjon(argument):
	return 2

#
#  Oppgave 4 
#    Formål:
#    Ditt første møte med regulære uttrykk i Python (Perl stil)
#    Utførsk re.findall funksjonen fra Python modulen re
#    list = re.findall(regexp, str) (funksjon returnere en 
#	 liste av det som matcher regexp)
#    
#    Beskrivelse:
#    Gitt to regulære uttrykk r"[0-9]+" og r"[+*\-\/] gjør 
#    om en infix-notasjon på et enkelt regnestykke 
#    (kun to operander og en operator) til en prefix-notasjon)
#    
#    Eksempel:
#    infix_to_prefix("2+3") skal gi "+ 2 3"
#    infix_to_prefix("234+6125") skal gi "+ 234 6125"
#    infix_to_prefix("3/4") skal gi "/ 3 4"
#
#    Anta at inn-data er korrekt, dvs. inneholder to 
#    operander (to tall) og en operatør (+, for eksempel).
#
def infix_to_prefix(infix):
	return 2

# Eksperimenter
# ex10.py
def escape():
	tabby_cat = "\tI'm tabbed in."
	persian_cat = "I'm split\non a line."
	backslash_cat = "I'm \\ a \\ cat." 
	fat_cat = """
	I'll do a list:
	\t* Cat food
	\t* Fishies
	\t Catnip\n\t* Grass
	"""
	print tabby_cat
	print persian_cat
	print backslash_cat
	print fat_cat

#escape()

def list_comprehension():
	ath_data = [('Marit', 'Norway', 'cross-country skiing'), ('Martin', 'France', 'biathlon')]
	ath_country = [name + ' is from ' + country for name, country, sport in ath_data]
	for row in ath_country:
		print row

list_comprehension()

c1 = "CS373"
c2 = "CS253"
print c1.find("CS3")
print c2.find("CS3")

# Kaller opp implementerte funksjoner (pseudo-testing)
# For å teste innleveringen
#print 5*"-" + " Studenter: " + 5*"-"
#for s in gruppe.values():
#	if s is not "-":
#		print s

#print 5*"-" + " mysysinfo() " + 5*"-"
#min_sys_info()

#print 5*"-" + " funksjon() " + 5*"-"
#print initialer("Wolfgang Goethe")





