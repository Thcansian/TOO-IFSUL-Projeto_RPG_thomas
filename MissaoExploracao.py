from Missao import Missao
from status import Status

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao, distancia):
        super().__init__(nome, descricao, recompensa)
        self.__regiao = regiao
        self.__distancia = distancia

    def concluir_missao(self, valor):
        if valor >= self.__distancia:
            return super().concluir_missao(valor)
        else:
            print("Distância insuficiente! Missão fracassada.")
            self.status = Status.FRACASSADA
            return False