import json

with open("dados.json", 'r') as json_file:
    dados = json.load(json_file)

print (dados)
input("insira nome: ")
 