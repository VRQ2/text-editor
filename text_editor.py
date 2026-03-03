from tkextrafont import Font
from tkinter import filedialog
from tkinter import *

filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0,END)

def saveFile():
	global filename
	if filename is None:
		saveAs()
		return
	try:
		t = text.get(0.0,END)
		with open(filename, 'w') as f:
			f.write(t)
	except Exception as e:
		print(f"ERROR SAVING {e}")
	
	f.close()

def saveAs():
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="ERROR", message = "Unabnle to save file...")

def openFile():
	f = filedialog.askopenfile(mode='r')
	if f is not None:
		try:
			t = f.read()
			text.delete(0.0, END)
			text.insert(0.0, t)
		finally:
			f.close()

root = Tk()
root.title("My Text Editor")
root.minsize(width=800,height=600)
root.maxsize(width=400,height=400)
root.configure(bg="#343567")

fira_font = Font(file="FiraCode-Light.ttf", family="Fira Code")
text = Text(root, width=400, height=400, bg="#1f1f3d", fg="#ffffff",spacing1=4, 
               spacing2=2, insertbackground="white")
text.pack(padx=2, pady=2, expand=True, fill="both")
text.configure(font=(fira_font, 8))


menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as", command=saveAs)
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
filemenu = Menu(menubar)
filemenu.add_command(label="T.B.D", command=newFile)
menubar.add_cascade(label="Settings", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
