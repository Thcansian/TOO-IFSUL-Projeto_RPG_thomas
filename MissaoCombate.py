from Missao import Missao

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__tipo_inimigo = tipo_inimigo
        self.__quantidade = quantidade

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\ntipo inimigo: {self.__tipo_inimigo}"
        msg += f"\nquantidade: {self.__quantidade}"
        return msg
    