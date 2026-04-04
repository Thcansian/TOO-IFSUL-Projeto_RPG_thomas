from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = None
        self.__descricao = None
        self.__recompensa = None
        self.__status = Status.PENDENTE 

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip()
        else:
            raise ValueError("nome invalido")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor.strip()

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, valor):
        if 1 <= valor <= 50:
            self.__recompensa = valor
        else:
            raise ValueError("entre 1 e 50")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if isinstance(novo_status, Status):
            self.__status = novo_status
        else:
            raise ValueError("status deve ser do tipo Status")
        

    def iniciar_missao(self):
        if self.__status == Status.PENDENTE:
            self.__status = Status.EM_ANDAMENTO
            print(f"A missão '{self.nome}' começou!")
            print(f"Objetivo: {self.descricao}")
        else:
            print("Não é possível iniciar essa missão.")

    def concluir_missao(self):
        if self.__status == Status.EM_ANDAMENTO:
            self.__status = Status.CONCLUIDA
            print(f"Missão concluída! Recompensa: {self.recompensa} XP")
        else:
            print("Não é possível concluir essa missão.")

    def __eq__(self, other):
        return isinstance(other, Missao) and self.nome == other.nome

    def __str__(self):
        return f"missao: {self.nome} | status: {self.status.name}"

    def exibir_dados(self):
        msg = (f"nome: {self.nome}\n")
        msg += (f"descricao: {self.descricao}\n")
        msg += (f"recompensa: {self.recompensa}\n")
        msg += (f"status: {self.status.name}")
        return msg