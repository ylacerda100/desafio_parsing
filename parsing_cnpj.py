from pymongo import MongoClient

d = []

# extraindo os dados do arquivo txt

with open('cnpjs.txt', 'r') as file:
    for line in file:
        if line.startswith('0'):
            continue
        elif line.startswith('1'):
            data = line.split()
            d.append({
                'estrutura': 'matriz',
                'cnpj': line[3:18],
                'nome': line[18:40],
                'cep': data[-5]
            })

        elif line.startswith('2'):
            data = line.split()
            d.append({
                'estrutura': 'filial',
                'cnpj': line[3:18],
                'nome': line[18:50],
                'data_cadastro': data[-5][21:]})

# criando banco de dados e inserindo os cnpjs

cliente = MongoClient('localhost', 27017)

db = cliente.test_database

dados = db.test_collection

dados = db.dados

dados.insert_many(d)
