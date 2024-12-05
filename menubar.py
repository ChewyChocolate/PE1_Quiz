import tkinter as tk
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.geometry("400x400+500+100")
window.title("MENU SAMPLE")

# Secondary Window
window2 = tk.Tk()
window2.geometry("300x300")
window2.title("Win 2")
window2.withdraw()
window.deiconify()

# Functions
def fnQuit():
    window.destroy()

def fnpopup(event):
    mnuFile.tk_popup(event.x_root, event.y_root, 0)

def fntest(event):
    messagebox.showinfo("Testing", "This is a test action!")

def fnNew():
    window.withdraw()
    window2.deiconify()

def fnBack():
    window2.withdraw()
    window.deiconify()

def fnSave():
    messagebox.showinfo("Save", "Save functionality is not yet implemented!")

def fnAbout():
    about_window = tk.Toplevel(window)
    about_window.geometry("300x200")
    about_window.title("About")
    lbl_about = tk.Label(about_window, text="This is a sample menu-driven application.\nVersion 1.0", font=("Arial", 12))
    lbl_about.pack(pady=20)
    btn_close = tk.Button(about_window, text="Close", command=about_window.destroy)
    btn_close.pack(pady=10)

def fnHelp():
    messagebox.showinfo("Help", "Use the menu bar to navigate and interact with the application.")

def fnToggleTheme():
    pass

# Back Button in Window 2
btnBack = tk.Button(window2, text="Back", command=fnBack)
btnBack.pack()

# Menu Bar
menubar = tk.Menu(window) 
window.config(menu=menubar)

# File Menu
mnuFile = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=mnuFile)
mnuFile.add_command(label="New", command=fnNew, accelerator="Ctrl+N")
mnuFile.add_command(label="Save", command=fnSave, accelerator="Ctrl+S")
mnuFile.add_separator()
mnuFile.add_command(label="Theme", command=fnToggleTheme)
mnuFile.add_separator()
mnuFile.add_command(label="Quit", command=fnQuit, accelerator="Ctrl+Q")

# About Menu
mnuAbout = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=mnuAbout)
mnuAbout.add_command(label="About", command=fnAbout)

# Help Menu
mnuHelp = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=mnuHelp)
mnuHelp.add_command(label="Help", command=fnHelp)

# Status Bar
lbl_status = tk.Label(window, text="Ready", bg="white", fg="black", anchor="w", relief="sunken")
lbl_status.pack(side="bottom", fill="x")

# Bindings for Shortcuts
window.bind("<Control-n>", lambda event: fnNew())
window.bind("<Control-s>", lambda event: fnSave())
window.bind("<Control-q>", lambda event: fnQuit())

# Context Menu and Test Action
window.bind("<Button-3>", fnpopup)
window.bind("<Button-2>", fntest)

window.mainloop()
