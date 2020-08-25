from src.ra2 import *
from colorama import init, Fore
from os import system
init(convert=True)

#note: this version was programed for windows os, but can be used in termux or in linux.
#note2: Future versions will have compatibility with both os.
#Hi catsploit! I see you. 7w7

class ConsoleUI:
	def __init__(self):
		self.cipher = RandomEncryptor2()

	def main(self):
		system('cls')
		self.title()

		while True:
			print(Fore.GREEN+" [>]"+Fore.WHITE+" #: ", end="")
			op = input()

			if op == "help":
				self.help()

			elif op.split(" ")[0] == "encrypt":
				try:
					test = op.split(" ")[1]

					val = self.cipher.encrypt(op.replace("encrypt ", ""))
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Result: "+val)
					print(Fore.GREEN+" [>]"+Fore.WHITE+" Save this to a file? [y/n] #: ", end='')
					valop = input()
					if valop == "y":
						print(Fore.GREEN+" [*]"+Fore.WHITE+" Saving...")
						f = open("encrypted_text.txt", "w")
						f.write(val)
						f.close()
						print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: no arguments.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.split(" ")[0] == "decrypt":
				try:
					val = self.cipher.decrypt(op.split(" ")[1])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Result: "+val)
					print(Fore.GREEN+" [>]"+Fore.WHITE+" Save this to a file? [y/n] #: ", end='')
					valop = input()
					if valop == "y":
						print(Fore.GREEN+" [*]"+Fore.WHITE+" Saving...")
						f = open("decrypted_text.txt", "w")
						f.write(val)
						f.close()
						print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: no arguments.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.startswith("encryptFile"):
				try:
					vals = op.split(" ")
					self.cipher.encryptFile(vals[1], vals[2])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: missing arguments.")

				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.startswith("decryptFile"):
				try:
					vals = op.split(" ")
					self.cipher.decryptFile(vals[1], vals[2])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: missing arguments.")

				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.startswith("saveKey"):
				try:
					self.cipher.saveKey(op.split(" ")[1])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.startswith("loadKey"):
				try:
					self.cipher.loadKey(op.split(" ")[1])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op=="generateKey":
				self.cipher.generateKey()
				print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")

			elif op == "exit":
				print(Fore.GREEN+" [#]"+Fore.WHITE+" Goodbye!")
				break

			else:
				print(Fore.RED+" [!]"+Fore.WHITE+" Command not recognized.")


	def title(self):
		print(Fore.CYAN+"##            # "+Fore.GREEN+"           ###                      #           "+Fore.YELLOW+" ### \n"
				+Fore.CYAN+"# #  ## ##  ### ### ### "+Fore.GREEN+"   #   ##  ### ### # # ### ### ### ###"+Fore.YELLOW+"     # \n"
				+Fore.CYAN+"##  # # # # # # # # ###  "+Fore.GREEN+"  ##  # # #   #   ### # #  #  # # #   "+Fore.YELLOW+"  ### \n"
				+Fore.CYAN+"# # ### # # ### ### # #   "+Fore.GREEN+" #   # # ### #     # ###  ## ### #    "+Fore.YELLOW+" #   \n"
				+Fore.CYAN+"# #                        "+Fore.GREEN+"###             ### #                 "+Fore.YELLOW+"### "+Fore.RED+"\n by: Katrioska\n"
				)
		print(Fore.GREEN+" [#]"+Fore.WHITE+" Welcome to Random Encryptor 2 Pre-Alpha 1.0.0")
		print(Fore.GREEN+" [*]"+Fore.WHITE+" Note: This version can have bugs. Don't use for professional porposes.")
		print(Fore.GREEN+" [#]"+Fore.WHITE+" Use 'help' to show commands.")

	def help(self):
		print(Fore.GREEN+" [#]"+Fore.CYAN+" Commands: \n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\thelp					   	: Show this. \n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tencrypt [text]			: Encrypt the entered text.\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tdecrypt [text]			: Decrypt the entered encrypted text\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tencryptFile [path] [save path]  : Encrypt the file at path and save it on save path.\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tdecryptFile [path] [save path]  : Decrypt the encrypted file at path and save it on save path.\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tsaveKey [path]			: Save the key in the entered path.\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tloadKey [path]			: Load the key in the entered path.\n\n")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tgenerateKey			: Generate a new key.\n\n")

if __name__ == "__main__":
	ui = ConsoleUI()
	ui.main()