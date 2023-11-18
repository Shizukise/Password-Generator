import tkinter as tk
import random as rand



letters = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
numbers = [i for i in range(0,10)]
letters_n_numbers = letters + numbers
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
letters_n_specialC = letters + special_characters
allallowed = letters + numbers + special_characters
12


lenghtpw = input("How many characters do you want?")
passwordlenght = int(lenghtpw)

contain_numbers = False
contain_symbols = False

numberspw = input("Do you want it to have numbers?")
symbolspw = input("Do you want it to have symbols?")


if numberspw.lower() == "y":
    contain_numbers = True

if symbolspw.lower() == "y":
    contain_symbols = True




def password_generator():   
    lenght = int(lenghtpw)
    password = ""
    while lenght != 0:  
        if contain_numbers is False and contain_symbols is False:
            new_letter = rand.choice(letters)
            lenght -= 1
            password += new_letter
        if contain_numbers is True and contain_symbols is False:
            new_character = str(rand.choice(letters_n_numbers))
            lenghtt -= 1
            password += new_character
        if contain_numbers is False and contain_symbols is True:
            new_character = rand.choice(letters_n_specialC)
            lenght -= 1
            password += new_character
        if contain_numbers is True and contain_symbols is True:
            new_character = str(rand.choice(allallowed))
            lenght -= 1
            password += new_character
    return password





root1 = tk.Tk()

def click_generator():
    output = tk.Label(root1,text="oi")
    output.pack()

main_button = tk.Button(root1, text="Generate password")
main_button.pack()

#password generator function is done, now i need to assign commands on tkinter buttons and create the GUI

root1.mainloop()




