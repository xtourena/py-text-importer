from sys import argv
from termcolor import colored

script, filename = argv

print "----------------------------------"
print colored ("Welcom to text(.txt) importer.", "red")
print "----------------------------------"

txt = open(filename)

print "--------------------------------------------"
print "Here's text from your file %r:" % filename
print colored (txt.read(),"green")
print "-------------------------------------------"

print "--------------------------------------------------"
print "Thanks for using "
print "--------------------------------------------------"
