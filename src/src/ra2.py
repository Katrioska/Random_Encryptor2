from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
from os import remove, path, walk
from pickle import dumps, loads, dump, load

class RandomEncryptor2:
	def __init__(self):
		self.__key = self.generateKey()
		self.__bufferSize = 65536
		self.__previuslyLoadedKeys = []

	def setKey(self, key):
		self.__key = bytearray.fromhex(key)

	def getKey(self, save=False):
		if save:
			f = open("key_text.txt", 'w')
			f.write(self.__key.hex())
			f.close()

		return self.__key.hex()

	def changeKey(self, keyId):
		self.__key = self.__previuslyLoadedKeys[keyId]

	def showKeys(self):
		return [self.__previuslyLoadedKeys[0].hex(), self.__previuslyLoadedKeys[1].hex()]

	def saveKey(self, path, saveKeyList=False):
		v_keys = []
		for(dirpath, dirnames, filenames) in walk(path):
			for file in filenames:
				if file.startswith("key"):
					v_keys.append(filenames)

		cont = len(v_keys)

		with open(path+"\\key{}.dat".format(cont), 'wb') as f:
			f.write(self.__key)
		if saveKeyList:
			self.__previuslyLoadedKeys.append(self.__key)

	def loadKey(self, path, saveKeyList=False):
		with open(path, 'rb') as f:
			self.__key = f.read()
		if saveKeyList:
			self.__previuslyLoadedKeys.append(self.__key)

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
		input_file = open(pathFile, 'rb')
		output_file = open(savePath+"\\"+pathFile.split("\\")[-1]+".encrypted", 'wb')

		output_file.write(cipher.iv)
		bufferF = input_file.read(self.__bufferSize)

		while len(bufferF) > 0:
			cipher_bytes = cipher.encrypt(bufferF)
			output_file.write(cipher_bytes)
			bufferF	= input_file.read(self.__bufferSize)

		input_file.close()
		output_file.close()
		remove(pathFile)
		"""
		with open(pathFile, "rb") as f:
			cipher_data = cipher.encrypt(f.read())

		file_name = pathFile.split('\\')[-1]
		file_extension = pathFile.split(".")[-1]
		data_to_dump = [file_name, cipher_data.hex(), cipher.iv.hex()]
		
		with open(savePath+"\\"+file_name.replace("."+file_extension, ".bin"), "wb") as ff:
			dump(data_to_dump, ff)

		remove(pathFile)
		"""
	def decryptFile(self, pathFile, savePath):
		input_file = open(pathFile, 'rb')
		output_file = open(savePath+"\\"+pathFile.split("\\")[-1].replace(".encrypted", ""), 'wb')

		ivRestored = input_file.read(16)

		cipher = AES.new(self.__key, AES.MODE_CFB, iv=ivRestored)

		bufferF = input_file.read(self.__bufferSize)
		while len(bufferF) > 0:
			decrypt_bytes = cipher.decrypt(bufferF)
			output_file.write(decrypt_bytes)
			bufferF = input_file.read(self.__bufferSize)

		input_file.close()
		output_file.close()
		remove(pathFile)
		"""
		with open(pathFile, "rb") as f:
			data_to_load = load(f)

		cipher = AES.new(self.__key, AES.MODE_CFB, iv=bytearray.fromhex(data_to_load[2]))

		with open(savePath+"\\"+data_to_load[0], "wb") as fd:
			fd.write(cipher.decrypt(bytearray.fromhex(data_to_load[1])))

		remove(pathFile)
		"""

	def generateKey(self):
		self.__key = get_random_bytes(32)
		return self.__key