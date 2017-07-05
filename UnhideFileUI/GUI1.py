from tkinter import *
import os
class Application(Frame):
    ''' A GUI application with two button'''

    def __init__(self,master):
        '''Initialize the Frame'''
        Frame.__init__(self,master)
        self.grid()
    def create_button(self,text="Quit",command=quit):
        self.button = Button(self,text=text,command = command,fg="red")
        return self.button

def logout_win():
    command = "sudo pkill loginwindow"
    sudoPassword = show_event()
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))


def hide_win():
    os.system("defaults write com.apple.finder AppleShowAllFiles False")
    logout_win()

def Unhide_win():
    os.system("defaults write com.apple.finder AppleShowAllFiles True")
    logout_win()

def show_event():
    print("Password is %s"%(e1.get()))
    password = e1.get()
    return password

root = Tk()
background_image=PhotoImage('hide.jpeg')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.title("First Script ")
root.geometry("400x200")

Label(root, text="Enter Password").grid(row=2,padx=20)

e1 = Entry(root)
e2 = Entry(root)

e1.pack()
e1.grid(row=2, column=1)

app = Application(root)
buttHide = app.create_button("Hide",hide_win)
buttUnhide  = app.create_button("Unhide",Unhide_win)
buttQuit = app.create_button()
buttEnter = app.create_button("Enter",show_event)

buttHide.pack()
buttUnhide.pack()
buttQuit.pack()
buttEnter.pack()


buttHide.grid(row = 2,column = 4,sticky=W,padx=46,pady=4)
buttUnhide.grid(row = 3,column = 4,sticky=W,padx=46,pady=4)
buttQuit.grid(row = 4 ,column = 4,sticky=W,padx=46,pady=4)
buttEnter.grid(row = 1 ,column = 4,sticky=W,padx=46,pady=4)

print(e1.get())

root.mainloop()
root.destroy()
