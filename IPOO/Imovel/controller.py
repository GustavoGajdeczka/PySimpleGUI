from model import Apartamento
import json
import random
import string

def pega_dados(obj):
    table = make_table(
        endereco = obj['endereco'],
        andar = obj['andar'],
        valor = obj['valor']
    )

try:
    with open('dados.json') as f:
        data_loaded = json.load(f)

except Exception as erro:
    print(f"## Erro: {erro}")

class make_table:
    def __init__(self, endereco, andar, valor):
        self.endereco = endereco
        self.andar = andar
        self.valor = valor

print(data_loaded)


        
