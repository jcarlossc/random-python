import random

class ClasseAleatoria:
    def __init__(self) -> None:
        pass

    def gera_float(self) -> float:
        return random.random()
    
    def gera_float_entre(self, num1: float, num2: float) -> float:
        return random.uniform(num1, num2)