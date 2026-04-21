# 🧙‍♂️ Sistema de Missões RPG - Herança, Enum e Relacionamento entre Classes

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Tecnologia de Orientação a Objetos (TOO)** do curso de **Ciência da Computação**.

O objetivo principal é aplicar conceitos fundamentais de Programação Orientada a Objetos (POO), com foco em:

* Herança
* Encapsulamento
* Enumerações (Enum)
* Relacionamento entre Classes (Agregação)

O sistema simula um conjunto de missões de um RPG fictício chamado **"Ecos de Arcadia"**, permitindo criar diferentes tipos de missões com comportamentos específicos e agora também vinculadas a um personagem.

---

## 🧠 Conceitos Aplicados

### 🔹 Herança

As classes de missões específicas herdam da classe base `Missao`, reutilizando atributos e métodos comuns.

### 🔹 Encapsulamento

Os atributos são protegidos utilizando `__` e acessados via propriedades (`@property`).

### 🔹 Enum

O status das missões é controlado utilizando a classe `Status`, garantindo maior segurança e padronização.

### 🔹 Agregação (Relacionamento entre Classes)

A classe `Personagem` possui uma lista de missões (`list<Missao>`), caracterizando um relacionamento do tipo **um-para-muitos**.

* Um personagem pode ter várias missões
* As missões existem independentemente do personagem
* O personagem é responsável por gerenciar suas missões

---

## 🏗️ Estrutura do Projeto

```
📁 projeto/
│
├── status.py                # Enum com estados da missão
├── Missao.py               # Classe base (classe mãe)
├── MissaoCombate.py        # Missões de combate
├── MissaoColeta.py         # Missões de coleta
├── MissaoExploracao.py     # Missões de exploração
├── Personagem.py           # Classe que gerencia as missões
└── teste.py                # Execução e testes do sistema
```

---

## ⚙️ Funcionalidades

* Criação de missões com:

  * Nome
  * Descrição
  * Recompensa
  * Status controlado por Enum

* Tipos de missão:

  * ⚔️ Combate (derrotar inimigos)
  * 🌿 Coleta (coletar itens)
  * 🗺️ Exploração (explorar regiões)

* Controle de fluxo da missão:

  * `iniciar_missao()`
  * `concluir_missao(valor)`

* Sistema de personagem:

  * Adicionar missões (`add_missao`)
  * Concluir missões (`concluir_missao`)
  * Acumular experiência (XP)

* Validação específica por tipo de missão:

  * Coleta → verifica quantidade de itens
  * Combate → verifica inimigos derrotados
  * Exploração → verifica distância percorrida

* Exibição de dados detalhados

---

## 🔄 Fluxo das Missões

As missões seguem o seguinte ciclo:

```
PENDENTE → EM_ANDAMENTO → CONCLUIDA
```

Ou, em caso de falha:

```
EM_ANDAMENTO → FRACASSADA
```

O controle é feito automaticamente pelos métodos da classe `Missao` e suas subclasses.

---

## 🔗 Relacionamento Personagem x Missões

O personagem atua como responsável pela execução das missões:

1. As missões são criadas separadamente
2. São adicionadas ao personagem
3. O personagem inicia automaticamente a missão
4. O personagem envia os dados para conclusão
5. A missão valida se foi concluída com sucesso
6. O personagem recebe XP em caso de sucesso

Esse modelo respeita:

* Separação de responsabilidades
* Reutilização de código
* Encapsulamento

---

## ▶️ Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repo.git
```

2. Acesse a pasta:

```
cd seu-repo
```

3. Execute o arquivo de teste:

```
python teste.py
```

---

## 🧪 Exemplo de Uso

```python
p = Personagem("renjiro")

m = MissaoCombate("Caçar Goblins", "Derrotar goblins", 50, "Goblin", 5)

p.add_missao(m)

p.concluir_missao(m, 5)

print(p.exibir_dados())
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram reforçados conceitos importantes como:

* Organização de código em múltiplos arquivos
* Uso correto de herança
* Criação de sistemas reutilizáveis
* Boas práticas com encapsulamento
* Uso de Enum para evitar erros de estado
* Implementação de relacionamento entre classes
* Separação de responsabilidades entre objetos

---

## 🚀 Possíveis Melhorias

* Sistema de nível automático para o personagem
* Sistema de progresso de missões
* Persistência de dados (JSON ou banco de dados)

---

## 👨‍💻 Autor

Desenvolvido por **Thomas Cansian**

---

## 📌 Observação

Este projeto tem fins educacionais e foi desenvolvido para prática de conceitos de Programação Orientada a Objetos.
