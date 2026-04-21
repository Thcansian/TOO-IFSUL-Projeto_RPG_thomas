from Missao import Missao
from status import Status

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, quantidade):
        super().__init__(nome, descricao, recompensa)
        self.__tipo_inimigo = tipo_inimigo
        self.__quantidade = quantidade

    def concluir_missao(self, valor):
        if valor >= self.__quantidade:
            return super().concluir_missao(valor)
        else:
            print("Inimigos derrotados insuficientes! Missão fracassada.")
            self.status = Status.FRACASSADA
            return False

    def exibir_dados(self):
        msg = super().exibir_dados()
        msg += f"\ntipo inimigo: {self.__tipo_inimigo}"
        msg += f"\nquantidade: {self.__quantidade}"
        return msg
    