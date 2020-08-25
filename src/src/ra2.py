from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
from os import remove, path
from pickle import dumps, loads, dump, load

class RandomEncryptor2:
	def __init__(self):
		self.__key = self.generateKey()

	def saveKey(self, path):
		with open(path+"\\key.dat", 'wb') as f:
			f.write(self.__key)

	def loadKey(self, path):
		with open(path, 'rb') as f:
			self.__key = f.read()

	def encrypt(self, data):
		cipher = AES.new(self.__key, AES.MODE_CFB)
		cipher_data = cipher.encrypt(data.encode())

		data_output = {
			"data" : cipher_data,
			"iv" : cipher.iv
		}

		return dumps(data_output).hex()

	def decrypt(self, data):
		todecrypt = loads(bytearray.fromhex(data))
		cipher = AES.new(self.__key, AES.MODE_CFB, iv=todecrypt["iv"])
		return cipher.decrypt(todecrypt["data"]).decode()

	def encryptFile(self, pathFile, savePath):
		cipher = AES.new(self.__key, AES.MODE_CFB)
		with open(pathFile, "rb") as f:
			cipher_data = cipher.encrypt(f.read())

		file_name = pathFile.split('\\')[-1]
		file_extension = pathFile.split(".")[-1]
		data_to_dump = [file_name, cipher_data.hex()]
		
		with open(savePath+"\\"+file_name.replace("."+file_extension, ".bin"), "wb") as ff:
			dump(data_to_dump, ff)

		remove(pathFile)

	def decryptFile(self, pathFile, savePath):
		cipher = AES.new(self.__key, AES.MODE_CFB)
		with open(pathFile, "rb") as f:
			data_to_load = load(f)

		with open(savePath+"\\"+data_to_load[0], "wb") as fd:
			fd.write(cipher.decrypt(bytearray.fromhex(data_to_load[1])))

		remove(pathFile)

	def generateKey(self):
		return get_random_bytes(32)