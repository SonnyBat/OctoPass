import random
from tkinter import *
import pyperclip
# list storing letters numbers and symbols used for password
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#", "$", "%", "&", "(", ")", "*", "+"]
combined = []
password = ""







# functions
def generate_password():
    global combined # access global variable
    global password # access global variable
    password_input.delete(0,len(password)) # deletes password if generating new one
    combined = [] # makes combined list empty
    password = "" # makes password string empty
    for x in range (0, random.randint(6,10)): # creates random password looping through lists adding to combine then shuffle
        combined += random.choice(letters)
        combined += random.choice(numbers)
        combined += random.choice(symbols)
        random.shuffle(combined)
    for x in range (0, len(combined)): # puts each str of combine into password string
        password += combined[x]
    password_input.insert(END, password) # inserts password variable
    pyperclip.copy(password) # copies password

def add_details():
    with open("password.txt", "a") as file: # creates file called password.txt or adds to file if you already have it and adds user details you typed in
        file.write( "\n" + "Website:" + website_input.get() + "\n" + "Email/User: " + email_input.get() + "\n" + "Password: " + password_input.get() + "\n")
    website_input.delete(0, len(website_input.get())) # deletes inputs after details are saved
    email_input.delete(0, len(email_input.get())) # deletes inputs after details are saved
    password_input.delete(0, len(password_input.get())) # deletes inputs after details are saved








# window creation UI
window = Tk()
window.title("OctoPass")
window.minsize(300, 300)
canvas = Canvas(width=290, height=290, bg="#00B7CD", highlightthickness=0)
octopass_img = PhotoImage(file="octopass.png")
canvas.create_image(150, 150, image=octopass_img)
canvas.grid(column=1, row=0)
window.configure(bg="#00B7CD")
window.configure(padx=10, pady=10)
window.iconbitmap("octoicon.ico")



# Label
website_label = Label(window, text=f"Website:",bg="#00B7CD", fg="#FFF1D1", font="Arial 12 bold")
website_label.grid(column=1, row=1)
email_label = Label(window, text=f"Email/User:",bg="#00B7CD", fg="#FFF1D1", font="Arial 12 bold" )
password_label = Label(window, text=f"Password:",bg="#00B7CD", fg="#FFF1D1", font="Arial 12 bold" )
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)




# Inputs
website_input = Entry(bg="#00B7CD", fg="#FFF1D1", width=30, font="Arial 8 bold")
website_input.grid(column=1, row=1)

email_input = Entry(bg="#00B7CD", fg="#FFF1D1", width=30, font="Arial 8 bold")
email_input.grid(column=1, row=2)

password_input = Entry(bg="#00B7CD", fg="#FFF1D1",width=30, font="Arial 8 bold")
password_input.grid(column=1, row=3)




# Button
generate_password = Button(window, text="Generate Password", command=generate_password, bg="#DF301C", fg="#FFF1D1", font="Arial 8 bold")
generate_password.grid(column=2, row=3)

add_details = Button(window, text="Add Password", command=add_details, bg="#DF301C", fg="#FFF1D1", font="Arial 8 bold", width=11, height=2)
add_details.grid(column=1, row=4)











window.mainloop()
