Letter = '''Dear <name>!
You are selected
Date : <date>'''

name=input(Enter any  name : )
date=input(Enter the date : )

Letter = Letter.replace(name)
Letter = Letter.replace(date)

print("Letter = Dear <name>!")
print("You are selected")            
print("Date : date") 

