import os
from tkinter import *


class Main(Tk): # Creates Parent window and handels switching between Frames
	def __init__(self):
		self.searching_dir = None

	def main(self):
		Tk.__init__(self)
		Parent = Frame(self)
		self.geometry("400x400")
		Parent.pack(side="top", fill="both", expand=True)
		Parent.grid_rowconfigure(0, weight=1)
		Parent.grid_columnconfigure(0, weight=1)
		self.Frames = {}
		frame = MainFrame(Parent, self, self.searching_dir)
		self.Frames[MainFrame] = frame
		frame.grid(row=0, column=0, sticky="snew")
		self.show_frame(MainFrame)

	def show_frame(self, page):
		self.Frames[page].tkraise()

def Get_dir(string): # Checks if he given dir is functional
	try:
		os.path.exists(string)
	except:
		print("error")
	else: # if it is it switches to the second screen
		searching_dir = string


class MainFrame(Frame):  # first frame 
	def __init__(self, parent, swapper, searching_dir):
		Frame.__init__(self, parent)
		x = []
		for i in range(len(os.listdir(searching_dir))):
			if os.path.splitext((os.listdir(searching_dir))[i])[1] in (".py", ".pyw", ".txt", ".json"):
				x.append((os.listdir(searching_dir))[i])	

		label = Listbox(self, width=75, height=25, yscrollcommand=True)
		for i in x:
			label.insert(0, i)
		label.bind("<Double-1>", lambda x:os.startfile(searching_dir+"\\"+label.get(label.curselection())))
		label.pack(side="top", anchor="w")
		


if __name__ == "__main__": # If the file is run on it's own it will well... runs
	app = Main()
	Dir = "D:\\Programming\\Python"
	app.searching_dir = Dir
	app.main()
	app.title("File Explorer")
	app.mainloop()
