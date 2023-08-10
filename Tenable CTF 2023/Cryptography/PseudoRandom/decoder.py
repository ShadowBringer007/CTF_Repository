import random
import time
import datetime  
import base64

#PyCryptodome
from Crypto.Cipher import AES
flag = b"IDK"
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

distance = []


#time given 2023-08-02 10:27 
#Epoch range beginning to end to account for all seconds
epoch = datetime.datetime(2023, 8, 2, 10, 27, 0).strftime('%s')
print(int(epoch) * 1000)
distance.append(int(epoch) * 1000)


epoch = datetime.datetime(2023, 8, 2, 10, 28, 0).strftime('%s')
print(int(epoch) * 1000)
distance.append(int(epoch) * 1000)


#print(distance)
ciphertext = b"lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y"
ciphertext_b64decode = base64.b64decode(ciphertext)

key = []

for x in range(distance[0], distance[1]+1):
	key = []
	#print(x)
	random.seed(x)

	for i in range(0, 16):
		key.append(random.randint(0,255))

	key = bytearray(key)
	

	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext_b64decode)
	print(plaintext)
	if b"flag" in plaintext:
		print(x)
		print(plaintext)
		break
