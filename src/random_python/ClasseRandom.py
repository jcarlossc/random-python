import random
from typing import List

class ClasseRandom:
    """
        Classe de estudo do módulo random.
    """
    def __init__(self) -> None:
        pass

    def gera_float(self) -> float:
        """
            Gera um número de ponto flutuante entre 0 e 1.

            Returns:
                float: Resultado: 0.2.
        """
        return random.random()
    
    def gera_float_com_parametro(self, num1: float, num2: float) -> float:
        """
            Gera um número de ponto flutuante de acordo com
            os parâmetros passados.

            Args:
                num1 (float): Primeiro número: 1.
                num2 (float): Segundo número: 2.

            Returns:
                float: Resultado: 1.2.
        """
        return random.uniform(num1, num2)
    
    def gera_inteiro_com_parametro(self, num1: int, num2: int) -> int:
        """
            Gera um número de inteiro de acordo com
            os parâmetros passados.

            Args:
                num1 (int): Primeiro número: 1.
                num2 (int): Segundo número: 9.

            Returns:
                int: Resultado: 4.
        """
        return random.randint(num1, num2)
    
    def gera_inteiro_passos(self, num1: int, num2: int, passos: int) -> int:
        """
            Gera um número inteiro de acordo com
            os parâmetros passados e o número de passos.

            Args:
                num1 (int): Primeiro número: 1.
                num2 (int): Segundo número: 10.
                passos (int): Terceiro número: 2. 

            Returns:
                float: Resultado: 7. Número ímpar.
        """
        return random.randrange(num1, num2, passos)
    
    def seleciona_elemento_lista(self, lista: List[str]) -> str:
        """
            Seleciona um elemento aleatório de uma lista.

            Args:
                lista (List): Lista de elementos.

            Returns:
                str: Resultado: 1 elemento da lista.
        """
        return random.choice(lista)
    
    def seleciona_quantidade_elementos(self, lista: List, quantidade: int) -> List[int]:
        """
            Seleciona de uma lista uma quantidade de elementos passados
            como parâmetro.

            Args:
                lista (List): Lista de elementos.
                quantidade (int): Quantidade de elementos.

            Returns:
                List: Resultado: Quantidade de elementos passados.
        """
        return random.sample(lista, quantidade)
    
    def embaralha_lista(self, lista: List) -> str:
        """
            Embaralha elementos de uma lista.

            Args:
                lista (List): Lista de elementos.

            Returns:
                List: Resultado: Elementos embaralhados.
        """        
        random.shuffle(lista)
        return lista

    def seleciona_multiplos_elementos(self, lista: List, peso: List, quantidade: int) -> str:
        """
            Seleciona elementos de uma lista de acordo com
            pesos (passados como floats) e quantidades.

            Args:
                lista (List): Lista de elementos.
                peso (List): Lista de pesos.
                quantidade (int): quantidade de elementos.

            Returns:
                List: Resultado: Quantidades de elementos com pesos maiores.
        """
        return random.choices(lista, peso, k = quantidade)    