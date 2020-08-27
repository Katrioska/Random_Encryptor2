from src.ra2 import *
from colorama import init, Fore
from os import system
init(convert=True)

#note: this version was programed for windows os, but can be used in termux or in linux with minor modifications.
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

			elif op.split(" ")[0] == "encryptFile":
				try:
					vals = op.split(" ")
					self.cipher.encryptFile(vals[1], vals[2])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: missing arguments.")

				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.split(" ")[0] == "decryptFile":
				try:
					vals = op.split(" ")
					self.cipher.decryptFile(vals[1], vals[2])
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: missing arguments.")

				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.split(" ")[0] == "saveKey":
				try:
					try:
						if op.split(" ")[2] == "true":
							save = True
						else:
							save = False
					except:
						save = False

					self.cipher.saveKey(op.split(" ")[1], save)
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.split(" ")[0] == "loadKey":
				try:
					try:
						if op.split(" ")[2] == "true":
							save = True
						else:
							save = False
					except:
						save = False

					self.cipher.loadKey(op.split(" ")[1], save)
					print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op=="generateKey":
				self.cipher.generateKey()
				print(Fore.GREEN+" [*]"+Fore.WHITE+" Done!.")

			elif op=="showKeys":
				print(Fore.GREEN+" [*]"+Fore.WHITE+" Saved keys:")
				for key in self.cipher.showKeys():
					print(Fore.YELLOW+" [=] "+Fore.WHITE+key)

			elif op.split(" ")[0] == "changeKey":
				try:
					self.cipher.changeKey(int(op.split(" ")[1]))
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op.split(" ")[0] == "getKey":
				try:
					if op.split(" ")[1] == "true":
						save = True
					else:
						save = False
				except:
					save = False

				print(Fore.YELLOW+" [#] "+self.cipher.getKey(save))

			elif op.split(" ")[0] == "setKey":
				try:
					self.cipher.setKey(op.split(" ")[1])
					print(Fore.GREEN+" [#]"+Fore.WHITE+" Done!.")
				except IndexError:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: missing arguments.")
				except Exception as e:
					print(Fore.RED+" [!]"+Fore.WHITE+" Error: {}".format(e))

			elif op == "exit":
				print(Fore.GREEN+" [#]"+Fore.WHITE+" Goodbye!")
				break

			elif op == "cls":
				system('cls')
				self.title()

			else:
				print(Fore.RED+" [!]"+Fore.WHITE+" Command not recognized.")


	def title(self):
		print(Fore.CYAN+" ##            # "+Fore.GREEN+"           ###                      #           "+Fore.YELLOW+" ### \n"
				+Fore.CYAN+" # #  ## ##  ### ### ### "+Fore.GREEN+"   #   ##  ### ### # # ### ### ### ###"+Fore.YELLOW+"     # \n"
				+Fore.CYAN+" ##  # # # # # # # # ###  "+Fore.GREEN+"  ##  # # #   #   ### # #  #  # # #   "+Fore.YELLOW+"  ### \n"
				+Fore.CYAN+" # # ### # # ### ### # #   "+Fore.GREEN+" #   # # ### #     # ###  ## ### #    "+Fore.YELLOW+" #   \n"
				+Fore.CYAN+" # #                        "+Fore.GREEN+"###             ### #                 "+Fore.YELLOW+"### "+Fore.RED+"\n by: Katrioska\n"
				)
		print(Fore.GREEN+" [#]"+Fore.WHITE+" Welcome to Random Encryptor 2 Pre-Alpha 1.1.0")
		print(Fore.GREEN+" [*]"+Fore.WHITE+" Note: This version can have bugs. Don't use for professional porposes.")
		print(Fore.GREEN+" [#]"+Fore.WHITE+" Use 'help' to show commands.")

	def help(self):
		print(Fore.GREEN+" [#]"+Fore.CYAN+" Commands:")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\thelp")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tencrypt [text]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tdecrypt [text]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tencryptFile [path] [save path]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tdecryptFile [path] [save path]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tsaveKey [path] [save in ram(true/false)]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tloadKey [path] [save in ram(true/false)]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tgenerateKey")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tshowKeys")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tcls")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tgetKey [save in disk(true/false)]")
		print(Fore.GREEN+" [*]"+Fore.WHITE+"\tsetKey [key]")

if __name__ == "__main__":
	ui = ConsoleUI()
	ui.main()