from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import hashlib

def hash_message(message):
    # Cria um objeto hashlib para o algoritmo SHA-3-256
    sha3_256 = hashlib.sha3_256()

    # Atualiza o objeto com a mensagem
    sha3_256.update(message.encode('utf-8'))

    # Retorna o valor de hash em formato hexadecimal
    return sha3_256.hexdigest()

if __name__ == "__main__":
    message = input("Digite a mensagem que você deseja " +
                    "encriptar com a função de hash: ")

    hashed_message = hash_message(message)
    print("Mensagem encriptada (hash):", hashed_message)


#Encriptador
def pad_text(text):
    block_size = 8
    padding_size = block_size - len(text) % block_size
    padding = bytes([padding_size] * padding_size)
    return text + padding

def unpad_text(padded_text):
    padding_size = padded_text[-1]
    return padded_text[:-padding_size]

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad_text(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad_text(padded_plaintext)
    return plaintext

if __name__ == "__main__":
    while True:
        key_input = input("Digite a chave de criptografia (8 bytes) ou 'sair' para encerrar: ")

        # Verifica se o usuário deseja sair
        if key_input.lower() == "sair":
            print("Encerrando o programa.")
            break

        key = key_input.encode()
        plaintext = input("Digite a mensagem a ser criptografada: ").encode()

        # Verifica se a chave tem o tamanho correto (8 bytes)
        if len(key) != 8:
            print("A chave deve ter exatamente 8 bytes!")
        else:
            ciphertext = des_encrypt(key, plaintext)
            decrypted_text = des_decrypt(key, ciphertext)

            print("Texto criptografado:", ciphertext)
            print("Texto descriptografado:", decrypted_text.decode())

#dencriptador

def unpad_text(padded_text):
    padding_size = padded_text[-1]
    return padded_text[:-padding_size]

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad_text(padded_plaintext)
    return plaintext

if __name__ == "__main__":
    key_input = input("Digite a chave de criptografia usada para criptografar a mensagem (8 bytes): ")
    key = key_input.encode()

    ciphertext_hex = input("Digite o texto criptografado (em hexadecimal): ")
    ciphertext = bytes.fromhex(ciphertext_hex)

    # Verifica se a chave tem o tamanho correto (8 bytes)
    if len(key) != 8:
        print("A chave deve ter exatamente 8 bytes!")
    else:
        try:
            decrypted_text = des_decrypt(key, ciphertext)
            print("Texto descriptografado:", decrypted_text.decode())
        except ValueError:
            print("Erro ao descriptografar. Verifique se a chave ou o texto criptografado estão corretos.")

