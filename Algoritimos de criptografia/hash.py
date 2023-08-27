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


