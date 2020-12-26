from pymongo import MongoClient

# criando banco de dados

client = MongoClient('localhost', 27017)

db = client.get_database('receita_cnpj')

cnpjs = db.get_collection('cnpjs')


# extraindo os dados do arquivo txt e inserindo no db

with open('cnpjs.txt', 'r') as file:
    for line in file:
        if line.startswith('0'):
            continue
        elif line.startswith('1'):
            data = line.split()
            db.cnpjs.insert_one({
                'estrutura': 'matriz',
                'cnpj': line[3:18],
                'nome': line[18:40],
                'cep': data[-5]
            })

        elif line.startswith('2'):
            data = line.split()
            db.cnpjs.insert_one({
                'estrutura': 'filial',
                'cnpj': line[3:18],
                'nome': line[18:50],
                'data_cadastro': data[-5][21:]})

