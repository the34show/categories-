##importing random shit
import random

def opends():
    #opens the ds
    name_to_first={}
    f=open("name.csv","r")
    header=f.readline()
    for line in f:
        name=line.strip("\n")
        first_char=name[0]
        name_to_first[name]=first_char
    f.close()
    return name_to_first

def letter(inital_letter):
    
    while len(inital_letter)!= 1:
        inital_letter=input("What letter would you like to start with? ")  
    return inital_letter.capitalize()
            


def game():
    alive=True
    pokemon="1"
    inital_letter=""
    global name_to_first
    name_to_first=opends()
    
    while alive== True:
        inital_letter=letter(inital_letter)        
        while pokemon[0]!= inital_letter:
            pokemon= input("What pokemon stats with "+ inital_letter + "? ")
            pokemon=pokemon.capitalize()
        inital_letter=pokemon[-1]
        #sets next variable
        if pokemon in name_to_first:
            print ("good job")
            pokemon="1"
        else:
            return ("Dead")
    

def opends2():
    #opens the ds
    first_to_name={}
    f=open("name.csv","r")
    header=f.readline()
    for line in f:
        name=line.strip("\n")
        first_char=name[0]
        if first_char in first_to_name:
            first_to_name[first_char].append(name)
        else:
            first_to_name[first_char]=[name]
    f.close()
    return first_to_name

def categories():
    alive=True
    pokemon="1"
    inital_letter=""
    global first_to_name
    first_to_name=opends2()
    while alive== True:
        inital_letter=letter(inital_letter)        
        while pokemon[0]!= inital_letter:
            pokemon= input("What pokemon stats with "+ inital_letter + "? ")
            pokemon=pokemon.capitalize()
        inital_letter=pokemon[-1]
        inital_letter=inital_letter.capitalize()
        alive=False
        


