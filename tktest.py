from tkinter import *
from tkinter import filedialog, ttk
import emailing_html_2 as email
from Authenticator import Authenticate

def Send(path, list):
    email.Send_HTML(username.get(), password.get(), path, list, 'smtp.gmail.com', 587)

def Update(a,l):
    a["values"] = l

def Login():
    if Authenticate(username.get(), password.get(), 'smtp.gmail.com', 587):
        root.destroy()
        root1 = Tk()
        local_path = StringVar()
        canva_paras = {'height': 500, 'width': 600}
        canva1 = Canvas(root1, height = canva_paras['height'], width = canva_paras['width'], bg = '#f0ddcc')
        canva1.pack()

        main_label1 = Label(canva1, text = "Welcome", bg = '#7bc7a2' )
        main_label1.place(relx = 0.45, rely = 0.1, anchor = 'center')
        main_label1.config(font = ("Courier", 25))

        lab1 = Label(canva1, text = "Enter senders' email addresses")
        lab1.place(relx = 0.1, rely = 0.3, anchor = 'w')
        lab1.config(font = ("Courier", 14))
        emails = StringVar()
        entry1 = Entry(canva1, textvariable = emails, width = 20)
        entry1.place(relx = 0.1, rely = 0.36, anchor = 'w')
        entry1.config(font = ("Courier", 14))
        email_list = []
        button1 = Button(canva1, text = "Enter", width = 10,bg = '#f0ddcc', command = lambda: [email_list.append(entry1.get()), Update(combob1, email_list)])
        button1.place(relx = 0.475, rely = 0.36, anchor = 'w')
        button1.config(font = ("Courier", 12))
        combob1 = ttk.Combobox(canva1, text = "No Addresses", width = 30, values = email_list)
        combob1.place(relx = 0.1, rely = 0.42, anchor = 'w')

        select_label = Label(canva1, text = "Select HTML folder" )
        select_label.place(relx = 0.1, rely = 0.5, anchor = 'w')
        select_label.config(font = ("Courier", 15))

        path_entry = Entry(canva1, textvariable = local_path)
        path_entry.place(relx = 0.1, rely = 0.55, anchor = 'w')
        path_button = Button(canva1, text = "Select Folder", bg = '#f0ddcc', command = lambda: [local_path.set(filedialog.askdirectory())])
        path_button.place(relx = 0.35, rely = 0.55, anchor = 'w')

        send_button = Button(canva1, text = "Send", bg = '#f0ddcc', command = lambda: Send(local_path.get(), email_list) )
        send_button.place(relx = 0.1, rely = 0.65, anchor = 'w', width = 100)
        send_button.config(font = ("Courier", 15))

        root1.mainloop()
        print(set(email_list))
        print(local_path.get())

    else:
        error_var = "Conditions not Met!!"
        print("Conditions not Met!!")

    root.update_idletasks()

if __name__ == '__main__':

    root = Tk()

    canva_paras = {'height': 500, 'width': 600}
    canva = Canvas(root, height = canva_paras['height'], width = canva_paras['width'], bg = '#f0ddcc')
    canva.pack()

    main_label = Label(canva, text = "Send HTML through emails", bg = '#7bc7a2' )
    main_label.place(relx = 0.45, rely = 0.1, anchor = 'center')
    main_label.config(font = ("Courier", 25))

    username_label = Label(canva, text = "Username", bg = '#f0ddcc' )
    username_label.place(relx = 0.08, rely = 0.45, anchor = 'w')
    username_label.config(font = ("Courier", 15))
    username = StringVar()
    username_entry = Entry(canva, textvariable = username, width = 30)
    username_entry.place(relx = 0.3, rely = 0.45, anchor = 'w')

    password_label = Label(canva, text = "Password", bg = '#f0ddcc' )
    password_label.place(relx = 0.08, rely = 0.55, anchor = 'w')
    password_label.config(font = ("Courier", 15))
    password = StringVar()
    password_entry = Entry(canva, textvariable = password, width = 30)
    password_entry.place(relx = 0.3, rely = 0.55, anchor = 'w')

    login_button = Button(canva, text = "Login", bg = '#f0ddcc', width = 45, command = lambda: [ Login(), print(username.get()+" "+password.get()), root.update_idletasks()])
    login_button.place(relx = 0.08, rely = 0.63, anchor = 'w')

    error_var = StringVar()
    error_var = ""
    error_label = Label(canva, text = error_var, bg = '#f0ddcc' )
    error_label.place(relx = 0.08, rely = 0.7, anchor = 'w')
    error_label.config(font = ("Courier", 20))

    root.mainloop()
