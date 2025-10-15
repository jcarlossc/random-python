import pytest
from random_python.ClasseRandom import ClasseRandom

random_class = ClasseRandom()

def test_gera_float():
    """ 
        Testa se gera um número float entre 0 e 1. 
    """
    valor = random_class.gera_float()
    assert isinstance(valor, float)
    assert 0 <= valor <= 1

def test_gera_float_com_parametro():
    """ 
        Testa se gera um número float dentro do intervalo fornecido.
    """
    num1, num2 = 1.0, 5.0
    valor = random_class.gera_float_com_parametro(num1, num2)
    assert isinstance(valor, float)
    assert num1 <= valor <= num2

def test_gera_inteiro_com_parametro():
    """
        Testa se gera um número inteiro dentro do intervalo fornecido.
    """
    num1, num2 = 1, 10
    valor = random_class.gera_inteiro_com_parametro(num1, num2)
    assert isinstance(valor, int)
    assert num1 <= valor <= num2

def test_gera_inteiro_passos():
    """
        Testa se gera número inteiro com passos corretos.
    """
    num1, num2, passos = 1, 10, 2
    valor = random_class.gera_inteiro_passos(num1, num2, passos)
    assert isinstance(valor, int)
    assert num1 <= valor < num2
    # Verifica o passo
    assert (valor - num1) % passos == 0

def test_seleciona_elemento_lista():
    """
        Testa se escolhe um elemento válido da lista.
    """
    lista = ['A', 'B', 'C', 'D']
    valor = random_class.seleciona_elemento_lista(lista)
    assert valor in lista

def test_seleciona_quantidade_elementos():
    """
        Testa se seleciona a quantidade correta de elementos.
    """
    lista = [1, 2, 3, 4, 5]
    quantidade = 3
    resultado = random_class.seleciona_quantidade_elementos(lista, quantidade)
    assert isinstance(resultado, list)
    assert len(resultado) == quantidade
    # Verifica se os elementos estão contidos na lista original
    assert all(elem in lista for elem in resultado)

def test_embaralha_lista():
    """
        Testa se embaralha a lista corretamente.
    """
    lista = [1, 2, 3, 4, 5]
    copia = lista.copy()
    resultado = random_class.embaralha_lista(lista)
    assert sorted(resultado) == sorted(copia)
    assert isinstance(resultado, list)

def test_seleciona_multiplos_elementos():
    """
        Testa se seleciona múltiplos elementos com peso.
    """
    lista = ['A', 'B', 'C']
    peso = [0.1, 0.3, 0.6]
    quantidade = 4
    resultado = random_class.seleciona_multiplos_elementos(lista, peso, quantidade)
    assert isinstance(resultado, list)
    assert len(resultado) == quantidade
    assert all(elem in lista for elem in resultado)
