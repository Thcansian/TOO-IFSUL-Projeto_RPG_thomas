from Missao import Missao

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__item = item
        self.__quantidade = quantidade

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nitem: {self.__item}"
        msg += f"\nquantidade: {self.__quantidade}"
        return msg