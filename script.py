import tkinter as tk
import random as rand



letters = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
numbers = [i for i in range(0,10)]
letters_n_numbers = letters + numbers
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
letters_n_specialC = letters + special_characters
special_charactersnnumbers = special_characters + numbers
allallowed = letters + numbers + special_characters




lenghtpw = int(input("How many characters do you want?: "))
passwordlenght = int(lenghtpw)

contains_numbers = False
contains_symbols = False
contains_letters = False

contains_numbnlet = False
contains_numbnsym = False
contains_symnlet = False

only_letters = False
only_numbers = False
only_symbols = False

allallowed1 = False

letterspw = input("Do you want it to have letters?: ")
numberspw = input("Do you want it to have numbers?: ")
symbolspw = input("Do you want it to have symbols?: ")


if numberspw.lower() == "y":
    contains_numbers = True

if symbolspw.lower() == "y":
    contains_symbols = True

if letterspw.lower() == "y":
    contains_letters = True

if contains_numbers and contains_letters:
    contains_numbnlet = True

if contains_numbers and contains_symbols:
    contains_numbnsym = True

if contains_letters and contains_symbols:
    contains_symnlet = True

if contains_letters and contains_numbers == False and contains_symbols == False:
    only_letters = True

if contains_numbers and contains_letters == False and contains_symbols == False:
    only_numbers = True

if contains_symbols and contains_numbers == False and contains_letters == False:
    only_symbols = True

if contains_letters and contains_numbers and contains_symbols:
    allallowed1 = True



def password_generator():   
    lenght = lenghtpw
    password = ""
    while lenght != 0:  
        if only_letters:
            new_letter = rand.choice(letters)
            lenght -= 1
            password += new_letter
        if only_numbers:
            new_letter = str(rand.choice(numbers))
            lenght -= 1
            password += new_letter
        if only_symbols:
            new_letter = rand.choice(special_characters)
            lenght -= 1
            password += new_letter
        if contains_numbnlet:
            new_letter = str(rand.choice(letters_n_numbers))
            lenght -= 1
            password += new_letter
        if contains_symnlet:
            new_letter = rand.choice(letters_n_specialC)
            lenght -= 1
            password += new_letter
        if contains_numbnsym:
            new_letter = str(rand.choice(special_charactersnnumbers))
            lenght -= 1
            password += new_letter
        if allallowed1:
            new_letter = str(rand.choice(allallowed))
            lenght -= 1
            password += new_letter

        
    return password


print(password_generator())

""" 
root1 = tk.Tk()

def click_generator():
    output = tk.Label(root1,text="oi")
    output.pack()

main_button = tk.Button(root1, text="Generate password")
main_button.pack()

#password generator function is done, now i need to assign commands on tkinter buttons and create the GUI

root1.mainloop()
 """



