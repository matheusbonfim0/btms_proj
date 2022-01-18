import requests
from pandas import json_normalize
import json

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://btms5.com.br',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://btms5.com.br/',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"dados":{"head":{"servico":"autenticacao","chave":"","teste":"xxxxxxxxxxxx"},"data":{"empresa":"bonitour","nome":"matheus bonfim","senha":"girassol"}}}'

response = requests.post('https://btms5.com.br/ws/wsbtms.php', headers=headers, data=data)

json = json_normalize(response.json())
json.columns
key = json.loc[0][3]
