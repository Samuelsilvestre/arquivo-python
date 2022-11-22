class Taxe:

    def __init__(self, nome, destino):
        self.__nome = nome
        self.__destino = destino
        return self.__chamar()

    def __chamar(self):
        return print(f'O cliente {self.__nome}, chama o taxe para uma corrida; destino {self.__destino}')

    def cancelar(self, motivo):
        print('__________')
        print(f'Nome: {self.__nome}')    
        print(f'Destino: {self.__destino}')
        print(f'Corrida: {self.__nome} cancelou a corrida')
        print(f'Motivo: {motivo}')
        print('__________')


