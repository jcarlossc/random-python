import random
from typing import List

class ClasseAleatoria:
    def __init__(self) -> None:
        pass

    def gera_float(self) -> float:
        return random.random()
    
    def gera_float_entre(self, num1: float, num2: float) -> float:
        return random.uniform(num1, num2)
    
    def gera_inteiro_entre(self, num1: int, num2: int) -> int:
        return random.randint(num1, num2)
    
    def gera_inteiro_passos(self, num1: int, num2: int, passos: int) -> int:
        return random.randrange(num1, num2, passos)
    
    def seleciona_elemento_lista(self, lista: List[str]) -> str:
        return random.choice(lista)
    
    def seleciona_quantidade_elementos(self, lista: List, quantidade: int) -> int:
        return random.sample(lista, 6)
    
    def embaralha_lista(self, lista: List) -> str:
        random.shuffle(lista)
        return lista