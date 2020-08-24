from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
from os import remove
from pickle import dumps, loads

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

	def generateKey(self):
		return get_random_bytes(32)