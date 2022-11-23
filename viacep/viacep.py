import requests
class ViaCEP:
    '''consumo da api do viacep'''
    def __init__(self, cep) -> None:
        self.__cep = cep
        return self.__get(self.__cep)
    # get
    def __get(self, get_cep):
        try:
            response = requests.get('https://viacep.com.br/ws/%s/json/'%get_cep)
            json_cep = response.json()
            cep = json_cep['cep']
            logradouro = json_cep['logradouro']
            bairro = json_cep['bairro']
            localidade = json_cep['localidade']
            uf = json_cep['uf']
            ddd = json_cep['ddd']
            print(f'''
                    cep {cep}
                    logradouro {logradouro}
                    bairro {bairro}
                    localidade {localidade}
                    estado {uf}
                    DDD {ddd}
                ''')
                
        except:
            print(f'{get_cep} não encontrado; tente novamente')
            
            



