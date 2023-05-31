import time

from cryptography.fernet import Fernet


class Try:
    def __init__(self):
        self.key = None


    def decrypt(self,file_name):
        # using the key

        fernet = Fernet(self.key)

        # opening the encrypted file
        with open(file_name, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file_name, 'wb') as dec_file:
            dec_file.write(decrypted)


    def encrypt(self,file_name):

        # key generation
        self.key = Fernet.generate_key()

        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)

        # opening the key
        with open('filekey.key', 'rb') as filekey:
            self.key = filekey.read()

        # using the generated key
        fernet = Fernet(self.key)

        # opening the original file to encrypt
        with open(file_name, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
t=Try()
t.encrypt('regex.txt')
time.sleep(30)
t.decrypt('regex.txt')
