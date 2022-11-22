class FalseTrue:

    def __init__(self, status: bool) -> None:
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self,valor: bool):
        if isinstance(valor, bool):
            self.__status = valor

