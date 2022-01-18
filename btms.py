import requests
from pandas import json_normalize
import json
from btms_token import key

date = str(input())

headers = {
    'Origin': 'https://btms5.com.br',
}

data = '{"dados":{"head":{"servico":"transporte_compartilhado_lista","chave":"%s","nao_converte_charset":"1"},"data":{"data":"%s","cdgbtms_atrativo":"","cdgbtms_transportador":"","cdg_cidade_origem":"","cdg_cidade_destino":"","cdg_tipo_rota":"","detalhes":"1","incluir_existentes":"1"}}}' % (key, date)

response = requests.post('https://btms5.com.br/ws/wsbtms.php', headers=headers, data=data)


json = json_normalize(response.json())
json.columns
transfer = json.loc[0][0]

i = len(transfer)

for x in range(i):
    obj = transfer[x]
    if obj.get('id_grupo') == '*':
        continue
    else:        
        print(obj.get('empresa'),
              obj.get('ida_h_saida'),
              obj.get('rota'),
              #obj.get('saida_data'),
              obj.get('reserva_numero'),
              obj.get('id_grupo'),
              obj.get('r_pax')
             )
