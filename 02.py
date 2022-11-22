class SistemaDeCadastro:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        return self.__validar(self.nome)
    def __validar(self, valor: str):
        if isinstance(valor, str):
            print('nome validado')
            return self.__cadastrar(valor)

        else:
            return print(f'erro no {valor}')

    def __cadastrar(self, valor):
        lista_de_cadastro = []
        lista_de_cadastro.append(valor)
        print(f'cadastrado {lista_de_cadastro}')            








def CadastrarNome():
    try:
        nome = str(input('Digite o nome: ')).strip().lower()
        obj_cadastro = SistemaDeCadastro(nome)
    except:
        print('erro digite o nome corretamente')

CadastrarNome()        
