from termcolor import colored
import random
import string

def exibir_logo_passly():
    print (colored(r"""
$$$$$$$\                           $$\                     $$\                       $$$$$$\ $$\   $$\$$$$$$\$$\   $$\ 
$$  __$$\                          $$ |                    $$ |                     $$  __$$\$$ |  $$ \_$$  _$$$\  $$ |
$$ |  $$ $$$$$$\  $$$$$$$\ $$$$$$$\$$ |    $$\   $$\       $$$$$$$\ $$\   $$\       $$ /  \__$$ |  $$ | $$ | $$$$\ $$ |
$$$$$$$  \____$$\$$  _____$$  _____$$ |    $$ |  $$ |      $$  __$$\$$ |  $$ |      $$ |     $$$$$$$$ | $$ | $$ $$\$$ |
$$  ____/$$$$$$$ \$$$$$$\ \$$$$$$\ $$ |    $$ |  $$ |      $$ |  $$ $$ |  $$ |      $$ |     \_____$$ | $$ | $$ \$$$$ |
$$ |    $$  __$$ |\____$$\ \____$$\$$ |    $$ |  $$ |      $$ |  $$ $$ |  $$ |      $$ |  $$\      $$ | $$ | $$ |\$$$ |
$$ |    \$$$$$$$ $$$$$$$  $$$$$$$  $$$$$$$$\$$$$$$$ |      $$$$$$$  \$$$$$$$ |      \$$$$$$  |     $$ $$$$$$\$$ | \$$ |
\__|     \_______\_______/\_______/\________\____$$ |      \_______/ \____$$ |       \______/      \__\______\__|  \__|
                                           $$\   $$ |               $$\   $$ |                                         
                                           \$$$$$$  |               \$$$$$$  |                                         
                                            \______/                 \______/                                          
    """, 'green'))

def gerar_senha_forte(tamanho=20):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Chame a função para exibir o logo PassLy
exibir_logo_passly()

# Gerar senha forte com 20 caracteres
senha_forte = gerar_senha_forte()
print(colored("Senha gerada:", "green"), senha_forte)
