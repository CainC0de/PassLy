import random
import string
from termcolor import colored

def gerar_senha_forte(tamanho=20):
    # Lista de caracteres que serão usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gerar senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha

# Gerar senha forte com 20 caracteres
senha_forte = gerar_senha_forte()
print(colored("Senha forte gerada:", "green"), senha_forte)
