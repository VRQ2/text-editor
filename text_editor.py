import os
import tkinter as tk
from tkextrafont import Font
from tkinter import filedialog
from tkinter import *
from tkinter import font

filename = None

def newFile(event=None):
	global filename
	filename = "Untitled.txt"
	text.delete(1.0,END)

def saveFile(event=None):
	global filename
	if filename is None:
		saveAs()
		return
	try:
		t = text.get(1.0,END)
		with open(filename, 'w') as f:
			f.write(t)
	except Exception as e:
		print(f"ERROR SAVING {e}")
	
	f.close()

def saveAs(event=None):
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(1.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="ERROR", message = "Unabnle to save file...")

def openFile(event=None):
	f = filedialog.askopenfile(mode='r')
	if f is not None:
		try:
			t = f.read()
			text.delete(1.0, END)
			text.insert(1.0, t)
		finally:
			f.close()

def zoom_in(event):
	zoom_var = custom_font.cget("size")
	custom_font.configure(size=zoom_var+1)

def zoom_out(event):
	zoom_var = custom_font.cget("size")
	custom_font.configure(size=zoom_var-1)

def zoom_mouse(event):
	if event.delta > 0:
		zoom_in(event)
	else:
		zoom_out(event)

root = Tk()
root.title("My Text Editor")
root.minsize(root.winfo_width(), root.winfo_height())
root.geometry("600x600+400+150")
root.configure(bg="#343567")

custom_font = font.Font(family="Courier", size=11)
text = Text(root, font=custom_font, width=400, height=400, bg="#1f1f3d", fg="#ffffff",spacing1=3, 
               spacing3=3, insertbackground="white", highlightthickness=0, borderwidth=0)
text.pack(padx=5, pady=5, expand=True, fill="both")

root.bind('<Control-MouseWheel>', zoom_mouse)
root.bind('<Control-minus>', zoom_out)
root.bind('<Control-plus>', zoom_in)
root.bind('<Control-equal>', zoom_in)
# dodac jakiś wskaznik ze plik został zapisany
root.bind('<Control-s>', saveFile)
# gdy tworzy plik zapytac o zapisanie poprzedniego
root.bind('<Control-n>', newFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-S>', saveFile)
root.bind('<Control-N>', newFile)
root.bind('<Control-O>', openFile)

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as", command=saveAs)
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
filemenu = Menu(menubar)
filemenu.add_command(label="T.B.D", command=None)
menubar.add_cascade(label="Settings", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
