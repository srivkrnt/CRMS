from Tkinter import *
from tkMessageBox import *
import dash


#LOGIN PAGE
dash.create()
dash.create_admin()


def index():
    index_ui = Tk()
    index_ui.geometry("900x600+300+100")
    index_ui.resizable(0,0)
    bg = PhotoImage(file="images/background.gif")
    Label(index_ui,image=bg).grid(row=0, column=0, rowspan=20, columnspan=20)

    Label(index_ui, text='Welcome', font='Helvetica 18 ', fg='white', bg='#34383C').place(x=50, y=230)
    Label(index_ui, text='Criminal Records Management System', font='Helvetica 12 ', fg='white', bg='#34383C').place(x=50, y=260)
    Label(index_ui, text='Add / Remove / update and view the records using this interactive application', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=290)
    Label(index_ui, text='Reduced function calls, improved speed', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=310)
    Label(index_ui, text='Code made readable for further developement', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=330)
    

    logo = PhotoImage(file="images/logo.gif")
    Label(index_ui, image=logo,borderwidth=0).place(x=695,y=120)


    username_logo = PhotoImage(file="images/username_logo.gif")
    Label(index_ui, image=username_logo).place(x=600, y=260)
    username = Entry(index_ui, font=(14),fg='#0B8FCC')
    username.place(x=635, y=260)

    pass_logo = PhotoImage(file="images/password_logo.gif")
    Label(index_ui, image=pass_logo).place(x=600, y=290)
    password = Entry(index_ui, font=(14), show='*',fg='#0B8FCC')
    password.place(x=635, y=290)

    login_button = Button(index_ui, borderwidth=0,bg='#1A2E39',command=lambda:dash.sign_in(index_ui,username.get(), password.get()))
    login_button_bg = PhotoImage(file="images/login_button.GIF")
    login_button.config(image=login_button_bg)
    login_button.place(x=640 , y=350)

    help_button = Button(index_ui, borderwidth=0, command=show_help,bg='#00BC90')
    help_bg = PhotoImage(file="images/help.gif")
    help_button.config(image=help_bg)
    help_button.place(x=870, y=570)
                      
    index_ui.mainloop()

def show_help():
    help_win = Toplevel()
    help_win.geometry("900x600+300+100")
    help_win.resizable(0,0)

    help_win_bg = PhotoImage(file="images/other_bg.gif")
    Label(help_win, image=help_win_bg).place(x=0, y=0)

    Label(help_win , text="Administrator's account", font="Helvetica 15 bold", fg='white', bg='#34383C').place(x=331, y=60)

    Label(help_win, text='Username:', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=160)
    Label(help_win , text='admin', fg = '#34383C', bg='white', font='Helvetica 11 ').place(x=300, y=200)
    Label(help_win, text='Password:', fg = '#34383C', bg='white',font='Helvetica 11 bold').place(x=300, y=260)
    Label(help_win , text='admin', fg = '#34383C', bg='white', font='Helvetica 11 ').place(x=300, y=300)

    Label(help_win , text='Use this password ', font = 'Helvetica 16 bold',bg='white', fg='#028CCA' ).place(x=300, y=400)
    help_win.mainloop()


    
root=Tk()
root.geometry("450x600+510+130")
root.resizable(0,0)
root.overrideredirect(1)
splash_image = PhotoImage(file="images/splash.gif")

def to_index():
    root.destroy()
    index()
    
Label(root, image = splash_image).place(x=0,y=0)
root.after(3000,to_index)
root.mainloop()

