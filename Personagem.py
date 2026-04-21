class Personagem:
    def __init__(self, nome):
        self.__nome = None
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0
        self.__missoes = []  

        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip().title()
        else:
            raise ValueError("Nome inválido")

    # add missao
    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)
            print(f"Missão '{missao.nome}' adicionada ao personagem.")
            missao.iniciar_missao()
        else:
            print("Missão já adicionada.")

    # conclui missao
    def concluir_missao(self, missao, valor):
        if missao in self.__missoes:
            sucesso = missao.concluir_missao(valor)

            if sucesso:
                self.__xp += missao.recompensa
                print(f"{self.nome} ganhou {missao.recompensa} XP!")
        else:
            print("Essa missão não pertence ao personagem.")

    def exibir_dados(self):
        msg = (f"\nNome: {self.nome}\n")
        msg += (f"XP: {self.__xp}\n")
        msg += ("Missões:\n")

        for m in self.__missoes:
            msg += f"- {m.exibir_dados()}\n"

        return msg