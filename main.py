import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho_senha = int(input("insira o tamanho de sua senha"))
senha = ''

for i in range(tamanho_senha):
    senha = senha + random.choice(caracteres)

print(f'A senha gerada e {senha}')