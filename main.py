import urllib.request
import json 
from MyHTMLParser import MyHTMLParser 


data = {}

with open('seed.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines() 

for url in urls:
    url = url.strip()

    if not url:
        continue
    
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')

    parser = MyHTMLParser()
    parser.feed(html_content)

    data[parser.title] = parser.images

with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Dados extraídos e salvos com sucesso no arquivo 'dados.json'!")