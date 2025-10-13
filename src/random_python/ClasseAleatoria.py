import random

class ClasseAleatoria:
    def __init__(self) -> None:
        pass

    def gera_float(self) -> float:
        return random.random()
    
    def gera_float_entre(self, num1: float, num2: float) -> float:
        return random.uniform(num1, num2)
    
    def gera_inteiro_entre(self, num1: int, num2: int) -> int:
        return random.randint(num1, num2)