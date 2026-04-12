import os
import re
import tkinter as tk
from tkextrafont import Font
from tkinter import filedialog
from tkinter import *
from tkinter import font
from pathlib import Path

class LineNumbers(tk.Canvas):
	def __init__(self, *args, **kwargs):
		tk.Canvas.__init__(self, *args, **kwargs)
		self.textwidget = None

	def redraw(self, *args):
		"""Redraw the line numbers gutter"""
		if not self.textwidget: return
		self.delete("all")
		i = self.textwidget.index("@0,0")
		while True:
			dline = self.textwidget.dlineinfo(i)
			if dline is None: break
			y = dline[1]
			linenum = str(i).split(".")[0]
			self.create_text(5, y+8, anchor="nw", text=linenum,
							 fill="#888888", font=self.textwidget.cget("font"))
			i = self.textwidget.index("%s+1line" % i)

class CustomText(tk.Text):
	def __init__(self, *args, **kwargs):
		tk.Text.__init__(self, *args, **kwargs)
		self._orig = self._w + "_orig"
		self.tk.call("rename", self._w, self._orig)
		self.tk.createcommand(self._w, self._proxy)

	def _proxy(self, *args):
		cmd = (self._orig,) + args
		try:
			result = self.tk.call(cmd)
		except Exception:
			return None
			
		if (args[0] in ("insert", "replace", "delete") or 
			args[0:3] == ("mark", "set", "insert") or
			args[0:2] == ("xview", "moveto") or args[0:2] == ("xview", "scroll") or
			args[0:2] == ("yview", "moveto") or args[0:2] == ("yview", "scroll")):
			self.event_generate("<<Change>>", when="tail")
		return result

filename = "My Text Editor"

def newFile(event=None):
	global filename
	text.delete(1.0,END)
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	filename = Path(f.name).name
	root.title(f"My Text Editor - {filename}")


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
	global filename
	filename = Path(f.name).name
	root.title(f"My Text Editor - {filename}")
	try:
		f.write(t.rstrip())
	except:
		showerror(title="ERROR", message = "Unabnle to save file...")

def openFile(event=None):
	f = filedialog.askopenfile(mode='r')
	if f is not None:
		global filename
		filename = Path(f.name).name
		root.title(f"My Text Editor - {filename}")
		try:
			t = f.read()
			text.delete(1.0, END)
			text.insert(1.0, t)
		finally:
			f.close()

def zoom_in(event):
	zoom_var = custom_font.cget("size")
	custom_font.configure(size=zoom_var+1)
	ln.redraw()

def zoom_out(event):
	zoom_var = custom_font.cget("size")
	custom_font.configure(size=zoom_var-1)
	ln.redraw()

def zoom_mouse(event):
	if event.num == 4 or event.delta > 0:
		zoom_in(event)
	elif event.num == 5 or event.delta < 0:
		zoom_out(event)

def handle_return(event):
	line_content = text.get("insert linestart", "insert")
	indentation_length = len(line_content) - len(line_content.lstrip())
	indentation = line_content[:indentation_length]
	if line_content.strip().endswith(':'):
		indentation += '\t'
		
	text.insert("insert", "\n" + indentation)
	
	return "break"

root = Tk()
root.title(filename)
root.minsize(root.winfo_width(), root.winfo_height())
root.geometry("600x600+400+150")
root.configure(bg="#343567")

custom_font = font.Font(family="Courier", size=11)

container = Frame(root, bg="#343567")
container.pack(expand=True, fill="both")

ln = LineNumbers(container, width=35, bg="#1f1f3d", highlightthickness=0, bd=0)
ln.pack(side="left", fill="y")

text = CustomText(container, font=custom_font, bg="#1f1f3d", fg="#ffffff",spacing1=3, 
               spacing3=3, insertbackground="white", highlightthickness=0, borderwidth=0)
text.pack(side="right", padx=5, pady=5, expand=True, fill="both")

ln.textwidget = text

text.bind("<<Change>>", lambda e: ln.redraw())
text.bind("<Configure>", lambda e: ln.redraw())

root.bind('<Control-MouseWheel>', zoom_mouse)
root.bind('<Control-Button-4>', zoom_mouse)
root.bind('<Control-Button-5>', zoom_mouse)
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
text.bind('<Return>', handle_return)

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
