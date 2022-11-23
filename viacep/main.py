from viacep import ViaCEP
class Cep:
    '''construtor da class 
        input do cep'''
    def __init__(self) -> None:
        self.__cep = input('CEP:').strip()
        return self.__consutar(self.__cep)
    #metodo de consuta
    def __consutar(self, cep):
        obj_cep = ViaCEP(cep)

