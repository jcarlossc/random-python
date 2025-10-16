# 📌 Projeto: Estudo do Módulo Random em Python 
 Projeto simples, usado como modelo para uma postagem no Blogger.

Este projeto apresenta uma classe chamada **`ClasseRandom`**, criada com o objetivo de explorar e exemplificar as principais funções do módulo **`random`** da biblioteca padrão do Python.

Através de métodos organizados e documentados, o projeto demonstra como gerar números aleatórios, selecionar elementos de listas, embaralhar sequências e trabalhar com pesos probabilísticos.

---

## 📌 Conceitos Estudados

- Funções principais do módulo random:
- random(), uniform(), randint(), randrange()
- choice(), sample(), shuffle(), choices()
- Tipagem estática com typing.List
- Estrutura de testes automatizados com pytest
- Gerenciamento de ambiente e dependências com Poetry

---

## 📌 Tecnologias Utilizadas

- Python 3.13+
- Poetry → gerenciamento de dependências e empacotamento
- Pytest → testes automatizados
- mypy → teste de tipagem estática
- Visua Studio Code
- Windows 10

---

## 📌 Estrutura do Projeto

```
andom-python/
│
├── src/
│   └── random_python/
│           └── init.py
│           ├── ClasseRandom.py
│           └── main.py
├── tests/
│    └── test_ClasseRandom.py 
│
├── .gitignore
├── LICENSE
├── poetry.lock
├── pyproject.toml
└── README.md 
```
---

## 📌 Descrição dos Métodos da Classe
| Método |	Descrição |	Retorno |
| ------ | --------- | ------- |
| gera_float() |	Gera número aleatório entre 0 e 1. |	float |
| gera_float_com_parametro(num1, num2) |	Gera float entre num1 e num2. |	float |
| gera_inteiro_com_parametro(num1, num2) |	Gera inteiro entre num1 e num2. |	int |
| gera_inteiro_passos(num1, num2, passos) |	Gera inteiro com saltos definidos por passos. |	int |
| seleciona_elemento_lista(lista) |	Retorna um elemento aleatório da lista. |	str |
| seleciona_quantidade_elementos(lista, quantidade) |	Retorna vários elementos distintos da lista. |	list |
| embaralha_lista(lista) |	Embaralha elementos de uma lista. |	list |
| seleciona_multiplos_elementos(lista, peso, quantidade) |	Seleciona elementos com base em pesos probabilísticos. |	list |

---

## 📌 Instalação e Configuração do projeto

### 📌 1. Clonar repositório

```
git clone https://github.com/jcarlossc/random-python.git
cd random-python
```

Este projeto utiliza o [**Poetry**](https://python-poetry.org/) para gerenciar dependências, empacotamento e ambiente virtual.

### 📌 2. Instalar o Poetry

No terminal:

```bash
pip install poetry

```

### 📌 3. Verificar instalação

```
poetry --version

```

### 📌 4. Instalar dependências do projeto

```
poetry install
```

---

### 📌 5. Executar projeto

```
poetry run random
```

## 📌 Testes Automatizados com Pytest

```
poetry run pytest -v
```

---

## 📌 Testes de tipagem estática: mypy

```
poetry run mypy .
```

---

## 📌 Contribuições
Se quiser contribuir:

- Faça um fork deste repositório
- Crie uma branch para sua feature ou correção (git checkout -b minha-feature)
- Faça commits descritos claramente
- Submeta um Pull Request

---

## 📌 Licença
Este projeto está licenciado sob a MIT License.

---

## 📌 Contatos

- 📌Autor: Carlos da Costa<br>
- 📌Recife, PE - Brasil<br>
- 📌Telefone: +55 81 99712 9140<br>
- 📌Telegram: @jcarlossc<br>
- 📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>
- 📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>
- 📌Email: jcarlossc1977@gmail.com<br>
- 📌Portfólio em construção: https://portfolio-carlos-costa.netlify.app/<br>
- 📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>
- 📌GitHub: https://github.com/jcarlossc<br>
- 📌Kaggle: https://www.kaggle.com/jcarlossc/<br>
- 📌Twitter/X: https://x.com/jcarlossc1977
---
