from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for n in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Add Website name using get
    web = website_entry.get()
    # Add Email using get
    email = email_user_entry.get()
    # Add password using get
    password_data = password_entry.get()
    new_data = {
        web: {
            'Email': email,
            'Password': password_data,
        }
    }
    if len(web) == 0 or len(email) == 0 or len(password_data) == 0:
        messagebox.showwarning(title='Oops!', message="Please don't leave any fields blank!")
    else:
        # Open the file
        try:
            with open('passwords.json', 'r') as data:
                # Reading old data
                data_file = json.load(data)

        except FileNotFoundError:
            with open('passwords.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data with new
            data_file.update(new_data)
            with open('passwords.json', 'w') as data:
                json.dump(data_file, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ----------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open('passwords.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        if website in data:
            email = data[website]['Email']
            password = data[website]['Password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title='Error', message='No details for the website exist')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='C:/Users/kevs9/PycharmProjects/password-manager/logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text='Website:')
website.grid(column=0, row=1)
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, sticky=W)
website_entry.focus()

email_user = Label(text='Email/Username:')
email_user.grid(column=0, row=2)
email_user_entry = Entry(width=52)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_user_entry.insert(0, 'kevs9487@gmail.com')

password = Label(text='Password:')
password.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky=W)

gen_pass = Button(text='Generate Password', command=gen_password)
gen_pass.grid(column=2, row=3)

add_button = Button(text='Add', width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

search = Button(text='Search', width=15, command=find_password)
search.grid(column=2, row=1, sticky=W)
window.mainloop()