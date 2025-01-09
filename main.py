from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# import pyperclip
# pyperclip to auto copy password to clipboard
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = "".join(password_list)

    password_input.insert(0 , password)

    # password = ""
    # for char in password_list:
    #   password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:
                    {
                        "email": email,
                        "password": password,
                    }
                }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS" , message="Please make sure you haven't left any fields empty.")

    else:
        # is_ok = messagebox.askokcancel(title=website , message=f"These are details entered: \nEmail: {email}"
        #                                                f" \nPassword: {password}"
        #                                                f"\nIs it okay to save? ")
        #
        # if is_ok:
        try:
            with open("password.json" , "r") as  data_file:
                # read old passwords
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password.json" , "w") as data_file:
                json.dump(new_data , data_file , indent=4)

        else:
            # update the data along with old one
            data.update(new_data)

            with open("password.json", "w") as data_file:
                # saving the updated data
                json.dump(data , data_file , indent=4)

                # data_file.write(f"{website} | {email} | {password} \n ")

        finally:
                website_input.delete(0,END)
                password_input.delete(0,END)

# ---------------------------- PASSWORD SEARCH ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open("password.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="ERROR" , message="Bhai tu File hi nahi banya heh")

    else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website , message=f"Email:{email} \n"
                                                            f" Password:{password}")
        else:
            messagebox.showinfo(title="ERROR" , message="Bhai tu password hi nahi save kiya heh")


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=100 , pady=100)


# image

canvas = Canvas(width = 200 , height=200 )
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1 , row = 0)


# Website label
website_text = Label(text = "Website:", font=("Arial" , 24 , "bold") )
website_text.grid(column = 0 , row = 1)



# Email label
email_text = Label(text = "Email/Username:" , font=("Arial" , 24 , "bold"))
email_text.grid(column = 0 , row = 2)
# email_text.config(padx=2 , pady = 2)



# password label
password_text = Label(text = "Password:" , font=("Arial" , 24 , "bold"))
password_text.grid(column = 0 , row = 3)


# Search button
search_button = Button(text="Search",width=13 , command=search , bg="lightgreen")
search_button.grid(column = 2 , row = 1 )



# Add button
add_button = Button(text="Add" ,width=36, command=save_to_file)
add_button.grid(column = 1 , row = 4 , columnspan = 2)


# Generate Password button
generate_password_button = Button(text="Generate Password" , command=generate_password)
generate_password_button.grid(column = 2 , row = 3)


# Entry / input from user for WEBSITE
website_input = Entry(width=21)
website_input.grid(column = 1 , row = 1 )
website_input.focus( )
print(website_input.get())

# Entry / input from user for Email/username
email_input = Entry(width=35)
email_input.grid(column = 1 , row = 2, columnspan = 2)
email_input.insert(0 , "HETPatel@gmail.com")
print(email_input.get())

# Entry / input from user for Password Input
password_input = Entry(width=21)
password_input.grid(column = 1 , row = 3)

print(password_input.get())








window.mainloop()

