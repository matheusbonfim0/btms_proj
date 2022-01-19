import requests
from pandas import json_normalize
import pandas as pd
import json

cookies = {
    'JSESSIONID': '6c71404656249e73',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://sistema.bonitour.com.br/',
    'content-type': 'text/plain',
    'Origin': 'https://sistema.bonitour.com.br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = (
    ('a', '404660316'),
    ('v', '1214.62a3223'),
    ('to', 'dgsNFkUJDg4EQ0pCV0EBChBYFU0PDkcMXV1bEAw9Uw8DEAhe'),
    ('rst', '14313'),
    ('ck', '1'),
    ('ref', 'https://sistema.bonitour.com.br/roteiros/movimento_diario'),
)

data = 'bel.6;e,\'fcp,310,;e,\'load,3ab,'

response = requests.post('https://bam-cell.nr-data.net/events/1/de73bebc6e', headers=headers, params=params, cookies=cookies, data=data)

df = pd.read_html(response.content)
print(df)