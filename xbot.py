class Xbot:
    '''class de teste de um simulacro de chatbot'''
    def __init__(self) -> None:
        self.nome = input('Seu nome')
        self.email = input('Seu e-mail:')
        return self.__op()
    #metodo privado
    def __op(self):
        while True:
            print('O que voce deseja saber sobre nosso produto')
            opicoes = input('''
            (1) Qual volor do produto?
            (2) Qual o prazo de entrega?
            ''')
            if opicoes == '1':
                return self.__op1()
            if opicoes == '2':
                return self.__op2()          
    def __op1(self):
        return print('O valor do produto é de R$ 35.58')
    def __op2(self):
        return print('O prazo de entrega é ate 5 dias últeis')
    
if __name__ == '__main__':
    obj = Xbot()