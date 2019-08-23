import os
from tkinter import *
searching_dir = "D:\\Programming\\Python" # Default Location

class Main(Tk): # Creates Parent window and handels switching between Frames
	def __init__(self):
		Tk.__init__(self)
		Parent = Frame(self)
		self.geometry("500x500")
		Parent.pack(side="top", fill="both", expand=True)
		Parent.grid_rowconfigure(0, weight=1)
		Parent.grid_columnconfigure(0, weight=1)
		self.Frames = {}
		for f in (MainFrame, Screen2):
			frame = f(Parent, self)
			self.Frames[f] = frame
			frame.grid(row=0, column=0, sticky="snew")
		self.show_frame(MainFrame)

	def show_frame(self, page):
		self.Frames[page].tkraise()

def Get_dir(string, swapper): # Checks if he given dir is functional
	try:
		os.path.exists(string)
	except:
		print("error")
	else: # if it is it switches to the second screen
		searching_dir = string
		swapper.show_frame(Screen2)


class MainFrame(Frame):  # first frame 
	def __init__(self, parent, swapper):
		Frame.__init__(self, parent)
		path_entry = Entry(self)
		path_entry.bind("<Return>", lambda x: Get_dir(path_entry.get(), swapper))
		path_entry.pack()
		

class Screen2(Frame): # second frame
	def __init__(self, parent, swapper):
		Frame.__init__(self, parent)
		x = []
		for i in range(len(os.listdir(searching_dir))):
			if os.path.splitext((os.listdir(searching_dir))[i])[1] in (".py", ".pyw", ".exe", ".txt"):
				x.append((os.listdir(searching_dir))[i])	

		label = Listbox(self, width=75, height=25, yscrollcommand=True)
		for i in x:
			label.insert(0, i)
		label.bind("<Double-1>", lambda x:os.startfile(searching_dir+"\\"+label.get(label.curselection())))
		label.pack(side="top", anchor="w")
		button1 = Button(self, text="back",command=lambda:swapper.show_frame(MainFrame))
		button1.pack(side="top", anchor="w")


if __name__ == "__main__": # If the file is run on it's own it will well... run
	app = Main()
	app.title("File Explorer")
	app.mainloop()
