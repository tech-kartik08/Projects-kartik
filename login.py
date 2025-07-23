from tkinter import *
from tkinter import messagebox

bg_color = "beige"
text_color = "black"
btn_color = "#6074FF"

credentials = {
    "user_1": "Radhey",
    "user_2": "Krishna",
    "Kartikay": "Radhey",  
    "coder": "220010130125"
}

def check_password():
    username = e_name.get().strip()
    password = e_pass.get().strip()

    if username in credentials and credentials[username] == password:
        messagebox.showinfo('Login Success', f'Welcome, {username}!')
        load_welcome_screen(username)
    else:
        messagebox.showerror('Login Failed', 'Invalid username or password')

def load_welcome_screen(username):
    for widget in frame_down.winfo_children():
        widget.destroy()

    Label(frame_down, text=f"Welcome, {username}!", bg=bg_color, fg=text_color, font=('Ivy 16 bold')).place(relx=0.5, rely=0.4, anchor=CENTER)

    Button(frame_down, text="Log Out", bg=btn_color, fg=bg_color, font=('Ivy 10 bold'), command=reset_login_screen).place(relx=0.5, rely=0.6, anchor=CENTER)

def reset_login_screen():
    for widget in frame_down.winfo_children():
        widget.destroy()
    create_login_widgets()

def create_login_widgets():
    Label(frame_down, text="Username", bg=bg_color, fg=text_color, font=('Ivy 12')).place(x=10, y=10)
    global e_name
    e_name = Entry(frame_down, width=25, font=("", 15))
    e_name.place(x=14, y=40)

    Label(frame_down, text="Password", bg=bg_color, fg=text_color, font=('Ivy 12')).place(x=10, y=75)
    global e_pass
    e_pass = Entry(frame_down, width=25, show="*", font=("", 15))
    e_pass.place(x=14, y=110)

    Button(frame_down, text="Log In", bg=btn_color, fg=bg_color, width=39, height=2,
           font=("Ivy 9 bold"), command=check_password).place(x=15, y=180)

window = Tk()
window.title("Login System")
window.geometry('310x300')
window.configure(background=bg_color)

frame_up = Frame(window, width=310, height=50, bg=bg_color)
frame_up.grid(row=0, column=0)

frame_down = Frame(window, width=310, height=250, bg=bg_color)
frame_down.grid(row=1, column=0)

Label(frame_up, text="LOGIN", bg=bg_color, font=('Ivy 23 bold')).place(x=5, y=5)
Label(frame_up, width=40, height=1, bg=btn_color).place(x=10, y=45)

create_login_widgets()

window.mainloop()
