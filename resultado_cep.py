
###VOCÊ DIGITA O CEP E O PROGRAMA IRÁ TE DIZER A LOCALIDADE E TAMBÉM ALGUMAS INFORMAÇÕES SOBRE SUA CIDADE/ESTADO.

import requests
from googlesearch import search

def pesquisa_cep():
    cep = input("Digite o CEP: ")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)
    if response.status_code == 200:
        endereco = response.json()
        resultado_pesquisa = (f"Endereço: {endereco['localidade']}, {endereco['uf']}")
        print(f'FAZENDO PESQUISA POR: {resultado_pesquisa}')
        query = resultado_pesquisa
        print(f'CONFIRA ALGUMAS NOTÍCIAS SOBRE {resultado_pesquisa}')
        num_results = 5
        for i, result in enumerate(search(query, num_results=num_results)):
            print(f"Resultado {i + 1}: {result}")

    else:
        print("Não foi possível obter o endereço.")

pesquisa_cep()