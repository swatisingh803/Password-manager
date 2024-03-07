from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

# ----------------------------------------PASSWORD GENERATOR-----------------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    
    pyperclip.copy(password)
# ------------------------------------SAVE PASSWORD--------------------------------------------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty.")
    else:
        is_ok =  messagebox.askokcancel(title="website",message=f"These are details entered.\n Email:{email}\n password:{password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0 ,END)
        
# -----------------------------------UI SETUP-----------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)



canvas = Canvas(width=200,height=200)
logo_img = ImageTk.PhotoImage(file="images/logo.jpg")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=0)


website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=24)
website_entry.grid(column=1,row=1)
website_entry.focus()

search_button = Button(text="Search",width=15)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=44)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"name@example.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=24)
password_entry.grid(column=1,row=3)

password_button = Button(text="Generate password",command=generate_password)
password_button.grid(column=2,row=3)

Add_button = Button(text="Add",width=36,command=save)
Add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()