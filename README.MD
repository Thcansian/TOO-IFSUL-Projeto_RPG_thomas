# 🧙‍♂️ Sistema de Missões RPG - Herança e Enum

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Tecnologia de Orientação a Objetos (TOO)** do curso de **Ciência da Computação**.

O objetivo principal é aplicar conceitos fundamentais de Programação Orientada a Objetos (POO), com foco em:

* Herança
* Encapsulamento
* Enumerações (Enum)

O sistema simula um conjunto de missões de um RPG fictício chamado **"Ecos de Arcadia"**, permitindo criar diferentes tipos de missões com comportamentos específicos.

---

## 🧠 Conceitos Aplicados

### 🔹 Herança

As classes de missões específicas herdam da classe base `Missao`, reutilizando atributos e métodos comuns.

### 🔹 Encapsulamento

Os atributos são protegidos utilizando `__` e acessados via propriedades (`@property`).

### 🔹 Enum

O status das missões é controlado utilizando a classe `Status`, garantindo maior segurança e padronização.

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
├── Personagem.py           # Classe de personagem (apoio)
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
  * `concluir_missao()`

* Exibição de dados detalhados

---

## 🔄 Fluxo das Missões

As missões seguem o seguinte ciclo:

```
PENDENTE → EM_ANDAMENTO → CONCLUIDA
```

O controle é feito automaticamente pelos métodos da classe `Missao`.

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
m = MissaoCombate("Caçar Goblins", "Derrotar goblins", 50, "Goblin", 5)

m.iniciar_missao()
m.concluir_missao()
print(m.exibir_dados())
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram reforçados conceitos importantes como:

* Organização de código em múltiplos arquivos
* Uso correto de herança
* Criação de sistemas reutilizáveis
* Boas práticas com encapsulamento
* Uso de Enum para evitar erros de estado

---

## 👨‍💻 Autor

Desenvolvido por **Thomas Cansian**

---

## 📌 Observação

Este projeto tem fins educacionais e foi desenvolvido para prática de conceitos de Programação Orientada a Objetos.
