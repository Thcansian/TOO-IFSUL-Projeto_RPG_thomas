from Missao import Missao

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao, distancia):
        super().__init__(nome, descricao, recompensa)
        self.__regiao = regiao
        self.__distancia = distancia

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\nregiao: {self.__regiao}"
        msg += f"\ndistancia: {self.__distancia} km"
        return msg