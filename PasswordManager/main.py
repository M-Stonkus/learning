from tkinter import *
from tkinter import messagebox
import generator
import json

#Saves website, email or username and password for that website in a local txt file

def save_info():
    new_data={website_entry.get():{
        "email":email_entry.get(),
        "password":password_entry.get()
    }}
    if len(website_entry.get()) ==0 or len(email_entry.get())==0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"You entered:\nEmail:{email_entry.get()}\nPassword: {password_entry.get()}\nIs it okay to save?")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            except json.JSONDecodeError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

def generate():
    password_entry.delete(0,END)
    password_entry.insert(0, generator.generate_pass())

def search():
    try:
        with open("passwords.json", "r") as file:
            search_data = json.load(file)
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email: {search_data[website_entry.get()]["email"]}\nPassword: {search_data[website_entry.get()]["password"]}")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No Passwords Saved.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    #better to use if/else when possible
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website_entry.get()} exists.")

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=100)
window.minsize(width=500, height=350)

website_label = Label(text="Website:", anchor="e", width=15, height=3)
website_label.grid(column=0, row=1)

website_entry = Entry(width=24)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email_label = Label(text="Email/Username:", anchor="e", width=15, height=3)
email_label.grid(column=0, row=2)

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "name.surname@gmail.com")

password_label = Label(text="Password:", anchor="e", width=15, height=3)
password_label.grid(column=0, row=3)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, columnspan=1)

generate_button = Button(text="Generate", width=25, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=47, height=1, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=25, command=search)
search_button.grid(column=2, row=1, columnspan=1)



window.mainloop()