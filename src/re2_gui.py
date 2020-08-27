from tkinter import *
from tkinter import filedialog, messagebox, font

class GUI:
	def __init__(self):
		self.root = Tk()
		self.root.title("Random Encryptor 2 Alpha 1.0.0")
		self.root.resizable(0,0)
		self.root.config(bg="Black")

		self.bgColor = "#505050"
		self.strMode = "Encrypt"

		self.frame = Frame(self.root)
		self.frame.config(bg=self.bgColor)
		self.frame.pack()

		self.Title = Label(self.frame, text="Random Encyptor 2", font=("Console", 20), bg=self.bgColor, fg="#ff0000")
		self.TitleFont = font.Font(self.Title, self.Title.cget("font"))
		self.TitleFont.config(underline=True)
		self.Title.config(font=self.TitleFont)
		self.Title.grid(row=0, column=0, columnspan=3)

		self.TextMode = Label(self.frame, text=f"Mode: {self.strMode}", font=("Console", 15), bg=self.bgColor, fg="#ffffff")
		self.TextMode.grid(row=1, column=1)

	def main(self):
		self.root.mainloop()

if __name__ == "__main__":
	gui = GUI()
	gui.main()