from Personagem import Personagem
from MissaoColeta import MissaoColeta
from MissaoExploracao import MissaoExploracao

# cria personagem
p = Personagem("rengiro")

# cria missões
m1 = MissaoColeta("Coletar Ervas", "Pegar ervas", 50, "Erva", 10)
m2 = MissaoExploracao("Explorar Caverna", "Mapear caverna", 40, "Caverna", 5)

# Adiciona missões
p.add_missao(m1)
p.add_missao(m2)

# teste
print("\nSIMULAÇÃO")

p.concluir_missao(m1, 10)

p.concluir_missao(m2, 2)

print(p.exibir_dados())