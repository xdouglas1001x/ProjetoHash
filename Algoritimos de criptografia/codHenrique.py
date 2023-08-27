from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encryption(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB) 
    encrypted_text = cipher.encrypt(pad(plaintext, DES.block_size))
    return encrypted_text

def des_decryption(key, encrypted_text):
    cipher = DES.new(key, DES.MODE_ECB) 
    plaintext = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return plaintext

# key = get_random_bytes(8)
key = b"Henrique"

data = "Jonas".encode()

encrypted = b'\xc3\x1b\xd4\x90\xf7H\xf5\'\\j\xfc\xc2\x9cPd}BJ4\x88\xa4\x9f\x16*\xf5;\x07_``\x16\xb2qJP\xbb\x06\xb1\x08\xae\xdc\xf1 \xaf\xdb\x0e\xe9\xce\xb5\rP\x92\xdf\xd6\x96\xfb\x9e\xe3\xb2w\xe0\xbbp\x11\xc1\xca\xe6\xbe\t<\x92\xe3\x94\x9aD\x7f\x1d\xa9z"F\xf0\xb2\x8e\x10;\xc9x\x11\x1aW\xc3lv\xd8\xa3'
print("\nTexto cifrado:", encrypted)

decrypted = des_decryption(key, encrypted)
print("\n\nTexto decifrado:", decrypted.decode())