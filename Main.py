import secrets
import keyFile
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher

input = input("Enter what you would like to encrypt (must be at least 5 characters): ")
if len(input) < 5:
    print("Input must be at least 5 characters.")
    exit()
else:
    initialization_vector = secrets.token_bytes(16)
    
    algorithm = algorithms.AES(keyFile.key)
    mode = modes.CTR(initialization_vector)
    
    cipher = Cipher(algorithm, mode)
    encryptor = cipher.encryptor()
    
    encrypted_input = encryptor.update(input.encode('utf-8')) + encryptor.finalize()
    print(f'Here is the encrypted input: ', encrypted_input)
    
    file = open("encrypted.txt", "wb")
    file.write(encrypted_input)
    file.close()
    
    file = open("encrypted.txt", "rb")
    readData = file.read()
    print(f'Here is the Data back from the file: ', readData)
    
    cipher2 = Cipher(algorithms.AES(keyFile.key), modes.CTR(initialization_vector))
    decryptor = cipher2.decryptor()
    
    unencryptedData = decryptor.update(readData) + decryptor.finalize()
    print(f'Here is the unencrypted data: ', unencryptedData.decode('utf-8'))
    
    
    
    
    
    
