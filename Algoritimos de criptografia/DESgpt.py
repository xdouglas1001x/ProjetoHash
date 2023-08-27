from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encryption(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB) 
    encrypted_text = cipher.encrypt(pad(plaintext, DES.block_size))
    return encrypted_text

def des_decryption(key, encrypted_text):
    cipher = DES.new(key, DES.MODE_ECB) 
    plaintext = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return plaintext

def main():
    choice = input("Escolha 'E' para encriptar ou 'D' para descriptar: ").upper()

    key_input = input("Digite a chave de encriptação (8 caracteres): ")
    key = key_input.encode()

    if choice == 'E':
        data = input("Digite a mensagem a ser encriptada: ").encode()
        encrypted = des_encryption(key, data)
        print("\nTexto cifrado:", encrypted.hex())
    elif choice == 'D':
        encrypted_input = input("Digite o texto cifrado em hexadecimal: ")
        encrypted = bytes.fromhex(encrypted_input)
        decrypted = des_decryption(key, encrypted)
        print("\nTexto decifrado:", decrypted.decode())
    else:
        print("Escolha inválida. Encerrando.")

if __name__ == "__main__":
    main()