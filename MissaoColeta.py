from Missao import Missao
from status import Status

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__item = item
        self.__quantidade = quantidade

    def concluir_missao(self, valor):
        if valor >= self.__quantidade:
            return super().concluir_missao(valor)
        else:
            print("Itens insuficientes! Missão fracassada.")
            self.status = Status.FRACASSADA
            return False