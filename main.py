import urllib.request
import urllib.error
import json 
from MyHTMLParser import MyHTMLParser 

def raspar_pagina(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

        parser = MyHTMLParser()
        parser.feed(html_content)

        chave = parser.title if parser.title else url
        return chave, parser.images
        
    except urllib.error.URLError as e:
        print(f"Erro de conexão ao acessar {url}: {e.reason}")
        return None, None
    except Exception as e:
        print(f"Erro inesperado ao processar {url}: {e}")
        return None, None

data = {}
minha_data = {}
minha_url = 'https://exa-618-atividade-1.vercel.app/EXA618/atividade1'

print("Lendo o arquivo seed.txt...")
try:
    with open('seed.txt', 'r', encoding='utf-8') as file:
        urls = file.readlines() 
except FileNotFoundError:
    print("Erro: seed.txt não encontrado.")
    exit()

for url in urls:
    url = url.strip()
    if not url:
        continue
    
    chave, imagens = raspar_pagina(url)
    if chave:
        data[chave] = imagens

print(f"\n--- Iniciando o Crawler para a MINHA URL ---")
chave_minha, imagens_minha = raspar_pagina(minha_url)
if chave_minha:
    minha_data[chave_minha] = imagens_minha


with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open('minha_url.json', 'w', encoding='utf-8') as file:
    json.dump(minha_data, file, ensure_ascii=False, indent=4)

print("\nConcluído! Dados extraídos e salvos com sucesso nos arquivos JSON.")
