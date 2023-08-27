from pyDes import des

# Chave de criptografia DES (precisa ter 8 caracteres)
chave = "chave123"

# Dados a serem criptografados (precisa ter um tamanho múltiplo de 8 caracteres)
dados = "mensagem"

# Garantir que os dados tenham um tamanho múltiplo de 8 caracteres
tamanho_bloco = 8
dados += "\x00" * (tamanho_bloco - len(dados) % tamanho_bloco)

# Codificar os dados como UTF-8
dados = dados.encode('utf-8')

# Criptografar
cipher = des(chave.encode('utf-8'))
mensagem_criptografada = cipher.encrypt(dados)

# Descriptografar
cipher = des(chave.encode('utf-8'))
mensagem_descriptografada = cipher.decrypt(mensagem_criptografada)

# Decodificar a mensagem descriptografada para UTF-8
mensagem_descriptografada = mensagem_descriptografada.decode('utf-8').rstrip('\x00')

print("Mensagem criptografada:", mensagem_criptografada)
print("Mensagem descriptografada:", mensagem_descriptografada)