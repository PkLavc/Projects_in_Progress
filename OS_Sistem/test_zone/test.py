# with open('test.txt', 'r') as arquivo:
# # arquivo = open('test.txt','r')
# # conteudo = arquivo.read()
# print(conteudo)
# # arquivo.close()

import sys
import os

# Adiciona o caminho do diretório onde está o arquivo figures.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'resource'))

# Agora você pode importar o que precisar do figures.py
from figures import placa_coelho

print(placa_coelho)