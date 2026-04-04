from MissaoCombate import MissaoCombate
from MissaoColeta import MissaoColeta
from MissaoExploracao import MissaoExploracao

print("=== TESTE DE MISSÕES ===")

m1 = MissaoCombate("Caça Armamentos", "encontrar armas e passar pelo que precisar", 50, "Guerreiro", 5)
m2 = MissaoColeta("Coletar Ervas", "Pegar ervas", 30, "Erva", 10)
m3 = MissaoExploracao("Explorar Caverna", "Mapear caverna", 40, "Caverna", 2.5)

for m in [m1, m2, m3]:
    print("\n---")
    m.iniciar_missao()
    m.concluir_missao()
    print(m.exibir_dados())