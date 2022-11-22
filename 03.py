from random import randint as ri
class MasterMatriz:

    def __init__(self) -> None:
        self.__x = [
            [ri(1,10)], [ri(10,20)],
            [ri(20,30)], [ri(30,40)]
        ]
        return self.__find(self.__x)
    
    def __find(self, matriz):
        list = []
        for y in matriz:
            list.append(y * 4)
        return print(list)

