from tkinter import *
from tkinter import filedialog, messagebox, font

version = "Pre-Alpha 1.2.0"

class GUI:
	def __init__(self):
		self.root = Tk()
		self.root.title("Random Encryptor 2")
		self.root.resizable(0,0)
		self.root.config(bg="Black")

		self.bgColor = "#505050"
		self.fgColor = "#ffffff"
		self.strMode = "Encrypt"

		self.frame = Frame(self.root)
		self.frame.config(bg=self.bgColor)
		self.frame.pack()

		self.TopMenu = Menu(self.root)
		self.root.config(menu=self.TopMenu)

		self.MainMenu = Menu(self.TopMenu, tearoff=0)
		self.MainMenu.add_command(label="Save output")
		self.MainMenu.add_command(label="Load output")
		self.MainMenu.add_separator()
		self.MainMenu.add_command(label="Save key")
		self.MainMenu.add_command(label="Load key")
		self.MainMenu.add_separator()
		self.MainMenu.add_command(label="About")
		self.MainMenu.add_command(label="Exit")
		self.TopMenu.add_cascade(label="Menu", menu=self.MainMenu)

		self.TextMenu = Menu(self.TopMenu, tearoff=0)
		self.TextMenu.add_command(label="Text Encrypt Mode")
		self.TextMenu.add_command(label="Text Decrypt Mode")
		self.TopMenu.add_cascade(label="Text", menu=self.TextMenu)

		self.FileMenu = Menu(self.TopMenu, tearoff=0)
		self.FileMenu.add_command(label="File Encrypt Mode")
		self.FileMenu.add_command(label="File Decrypt Mode")
		self.TopMenu.add_cascade(label="File", menu=self.FileMenu)

		self.Title = Label(self.frame, text="Random Encryptor 2", font=("Console", 20), bg=self.bgColor, fg="#ff0000")
		self.TitleFont = font.Font(self.Title, self.Title.cget("font"))
		self.TitleFont.config(underline=True)
		self.Title.config(font=self.TitleFont)
		self.Title.grid(row=0, column=0, columnspan=3)

		self.TextMode = Label(self.frame, text=f"Mode: {self.strMode}", font=("Console", 15), bg=self.bgColor, fg=self.fgColor)
		self.TextMode.grid(row=1, column=1)

		self.InputLabel = Label(self.frame, text="input:", font=("Console", 8), bg=self.bgColor, fg=self.fgColor)
		self.InputLabel.grid(row=1, column=1, sticky="ws")

		self.InputText = Text(self.frame, height=10, width=40, bg="#606060", fg="#DBDBDB")
		self.InputText.grid(row=2, column=1)

		self.InputScroll = Scrollbar(self.frame, command=self.InputText.yview)
		self.InputScroll.grid(row=2, column=2, sticky="nsew")
		self.InputText.config(yscrollcommand=self.InputScroll.set)

		self.ConvertButton = Button(self.frame, text=self.strMode, fg="#DEDEDE", bg="#505050", activebackground="#303030")
		self.ConvertButton.grid(row=3, column=1)

		self.OutputLabel = Label(self.frame, text="output:", font=("Console", 8), bg=self.bgColor, fg=self.fgColor)
		self.OutputLabel.grid(row=3, column=1, sticky="ws")

		self.OutputText = Text(self.frame, height=10, width=40, bg="#606060", fg="#DBDBDB")
		self.OutputText.grid(row=4, column=1)

		self.OutputScroll = Scrollbar(self.frame, command=self.OutputText.yview)
		self.OutputScroll.grid(row=4, column=2, sticky="nsew")
		self.OutputText.config(yscrollcommand=self.OutputScroll.set)

		self.keyLabel = Label(self.frame, text=f"Key: {None}", font=("Console", 12), bg=self.bgColor, fg=self.fgColor)
		self.keyLabel.grid(row=5, column=1)

		self.versionLabel = Label(self.frame, text=version, font=("Console", 10), bg=self.bgColor, fg=self.fgColor)
		self.versionLabel.grid(row=6, column=1)

	def main(self):
		self.root.mainloop()

if __name__ == "__main__":
	gui = GUI()
	gui.main()