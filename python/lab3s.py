# -*- coding: latin-1 -*-

#
#  IS-105 LAB3
#
#  lab2.py - kildekode som inneholder studentenes løsning.
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

#
#  Oppgave 1
#    Skrive test1.sh, test1.pl og test1.py
#    Kalle disse opp fra en funksjon lab3_scripts()
#    vha. Python modulen subprocess
#    Funksjonen kalles opp på slutten av denne filen
#    Eksempel:
#      subprocess.call(["../scripts/test.sh"])
#      som skal returnere
#      1 a
#      1 b
#      1 c
#      ....
#      3 c
#
# Din funksjonsimplementering skrives her ...


#
#  Oppgave 2
#    Funksjonen min_sys_info() skriver ut systeminformasjon
#    til det miljøet (maskinen) den blir utført på.
#
#    Kopier resultatet som kjøring av denne funksjonen gir og 
#    lim inn her som kommentar.
#
def min_sys_info():
	"""
	Her er mitt resultat av kjøringen av denne funksjonen:
    
	"""
	print "byteorder: " + sys.byteorder
	print "os data: "
	print os.uname()
	print "os bruker: " + os.getlogin()


#
#  Oppgave 3
#    Jobbe med symboler (bokstaver og tall)
#	 Utforske str.find funksjon fra Python Standard Library
#    
#    Ved hjelp av str.find funksjonen implementer funksjon
#    initialer(navn), som gjør et personnavn med både
#	 fornavn og etternavn til initialer.
#    
#    Eksempel:
#    initialer("Alf Bogen") returnerer "A.B."
#    initialer("Von Neuman") returnerer "V.N."
#    
#    Anta at inn-data er korrekt (ingen testing nødvendig)
#
def initialer(navn):
	i_fornavn = navn[0]
	ws_p = navn.find(" ")
	i_etternavn = navn[ws_p + 1]
	init = i_fornavn + "." + i_etternavn + "."
	return init


#
#  Oppgave 4
#    Ditt første møte med regulære uttrykk i Python (Perl stil)
#    Utførsk re.findall funksjonen fra Python modulen re
#    
#    Gitt to regulære uttrykk r"[0-9]+" og r"[+*\-\/] gjør 
#    om en infix-notasjon på et enkelt regnestykke 
#    (kun to operander og en operator) til en prefix-notasjon)
#    
#    Eksempel:
#    infix_to_prefix("2+3") skal gi "+ 2 3"
#    infix_to_prefix("234+6125") skal gi "+ 234 6125"
#    infix_to_prefix("3/4") skal gi "/ 3 4"
#
#    Anta at inn-data er korrekt.
#
def infix_to_prefix():
	pass

#
#  Oppgave 4
#    Ditt første møte med regulære uttrykk i Python (Perl stil)
def min_reg_exp_test2():
	# Disjunction / OR (konstruksjon av enten eller)
	# Skriv et regulært uttrykk som enten passer for 
	# Assign to the variable regexp a regular expression that matches either the
	# exact string ab or one or more digits.
	regexp = r"ab|[0-9]+"

	# regexp matches:
	print re.findall(regexp,"ab") == ["ab"]
	#>>> True
	print re.findall(regexp,"1") == ["1"]
	#>>> True
	print re.findall(regexp,"123") == ["123"]
	#>>> True

	# regexp does not match:
	print re.findall(regexp,"a") != ["a"]
	#>>> True
	print re.findall(regexp,"abc") != ["abc"]
	#>>> True
	print re.findall(regexp,"abc123") != ["abc123"]
	#>>> True 

#
#  Oppgave X
#    Ta inn data fra utdata til en skript og analysere disse dataene
#    Kanskje for komplisert?
def cmd_parsing():
#list = subprocess.call(["ls","-l","/tmp/"])
# Trying this, but the return value named list is not list :( ...
#for line in list:
#	re.findall(r"[0-9]", line)

# What about this? This is present from Python 2.7 only ...
	result = subprocess.check_output(["ls","-l","../shell"])
#print result
#for line in result:
#	print line
	for item in result.splitlines():
		print item
		print re.findall(r"[r][w][x]", item)



# Kaller opp implementerte funksjoner (pseudo-testing)
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
	if s is not "-":
		print s

print 5*"-" + " mysysinfo() " + 5*"-"
print min_sys_info.__doc__
#min_sys_info()

print 5*"-" + " min_reg_exp_test() " + 5*"-"
min_reg_exp_test()

print 5*"-" + " initialer() " + 5*"-"
print initialer("Wolfgang Goethe")


print 5*"-" + " lab3_scripts() " + 5*"-"




