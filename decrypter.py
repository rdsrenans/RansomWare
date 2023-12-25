import os
import pyaes as ps

file_name = 'alvo.txt.ransoso'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = b'alvosransomwares'
aes = ps.AESModeOfOperationCTR(key)
decrypted = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'alvo.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted)
new_file.close()
