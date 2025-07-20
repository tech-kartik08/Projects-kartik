# from tkinter import *
# from tkinter import Tk, ttk
# from tkinter import messagebox
# co1 ="beige"
# co2="black"
# co3= "#6074FF"

# window = Tk()
# window.title("") 
# window.geometry('310x300')
# window.configure(background=co1)

# credentails = ['coder','220010130125']

# def check_password():
#     name=e_name.get()
#     password=str(e_pass.get())

#     if name == 'Kartikay' and password=='Radhey':
#         messagebox.showinfo('login','Welcome Krishna!')
        
#     elif name==credentails[0] and password==credentails[1]:
#         messagebox.showinfo('login','Welcome back ' + credentails[0])

#         for widget in frame_down.winfo_children():
#             widget.destroy()
        
#         for widget in frame_down.winfo_children():
#             widget.destroy()
        
#         new_window()
#     else:
#         messagebox.showwarning('Error', 'invalid username and password')

# def new_window():
#     username= Label(frame_down, text="username",height=1,anchor=NW,bg=co1, fg=co2, font=('Ivy 12'))
#     username.place(x=10,y=10)

#     username= Label(frame_down, text="Welcome " + credentails[0],height=1,anchor=NW,bg=co1, fg=co2, font=('Ivy 12'))
#     username.place(x=10,y=10)
    

    
# frame_up = Frame(window, width=310, height=50, bg=co1)
# frame_up.grid(row=0,column=0)

# frame_down = Frame(window, width=310, height=300, bg=co1)
# frame_down.grid(row=1,column=0)

# heading = Label(frame_up, text="LOGIN", bg=co1, font=('Ivy 23 bold'))
# heading.place(x=5,y=5)

# line = Label(frame_up, width=40, text="",height=1,bg=co3,anchor=NW)
# line.place(x=10, y=45)

# username= Label(frame_down, text="username",height=1,anchor=NW,bg=co1, fg=co2, font=('Ivy 12'))
# username.place(x=10,y=10)

# e_name= Entry(frame_down,width=25,justify="left",font=("", 15))
# e_name.place(x=14,y=40)

# password= Label(frame_down, text="Password",height=1,anchor=NW,bg=co1, fg=co2, font=('Ivy 12'))
# password.place(x=10,y=75)

# e_pass= Entry(frame_down,width=25,justify="left",show='*',font=("", 15))
# e_pass.place(x=14,y=110)

# button_confirm = Button(frame_down,text="logIn",bg=co3,fg=co1,width=39,height=2,font=("Ivy 9 bold"),command=check_password)
# button_confirm.place(x=15,y=180)

# window.mainloop()
from tkinter import *
from tkinter import messagebox
# hi my self kartik
# --------- UI Colors ---------
bg_color = "beige"
text_color = "black"
btn_color = "#6074FF"

# --------- Sample Credentials (username: password) ---------
credentials = {
    "user_1": "Radhey",
    "user_2": "Krishna",
    "admin": "admin123"
}

# --------- Login Validation Function ---------
def check_password():
    username = e_name.get().strip()
    password = e_pass.get().strip()

    if username in credentials and credentials[username] == password:
        messagebox.showinfo('Login Success', f'Welcome, {username}!')
        load_welcome_screen(username)
    else:
        messagebox.showerror('Login Failed', 'Invalid username or password')

# --------- Load Welcome Screen ---------
def load_welcome_screen(username):
    for widget in frame_down.winfo_children():
        widget.destroy()

    welcome_label = Label(frame_down, text=f"Welcome, {username}!", bg=bg_color, fg=text_color, font=('Ivy 16 bold'))
    welcome_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    logout_btn = Button(frame_down, text="Log Out", bg=btn_color, fg=bg_color, font=('Ivy 10 bold'), command=reset_login_screen)
    logout_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

# --------- Reset Login Screen ---------
def reset_login_screen():
    for widget in frame_down.winfo_children():
        widget.destroy()
    create_login_widgets()

# --------- Build Login UI ---------
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

# --------- Main Window Setup ---------
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