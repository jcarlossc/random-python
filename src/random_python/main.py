from random_python.ClasseRandom import ClasseRandom

def main():
    print(f'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f' ESTUDO SOBRE O MÓDULO RANDOM EM LINGUAGEM PYTHON')
    print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    random = ClasseRandom()
    print(f'Gera float entre 0 e 1: {random.gera_float():.2f}')
    print(f'Gera float com passagem de parâmetros: {random.gera_float_com_parametro(1, 2):.2f}')
    print(f'Gera inteiro com passagem de parâmetros: {random.gera_inteiro_com_parametro(1, 5)}')
    print(f'Gera inteiro com passos: {random.gera_inteiro_passos(1, 10, 2)}')

    frutas = ["maçã", "banana", "uva", "laranja"]
    print(f'Seleciona elementos aleatórios em lista: {random.seleciona_elemento_lista(frutas)}')
    
    numeros = list(range(1, 50))
    print(f'Seleciona quantidade de elementos de lista: {random.seleciona_quantidade_elementos(numeros, 6)}')
    
    letras = ['a', 'b', 'c', 'd', 'e']
    print(f'Embaralha os elementos da lista: {random.embaralha_lista(letras)}')

    simbolos = ['!', '@', '#', '$', '%', '&']
    peso = [0.1, 0.1, 0.1, 0.1, 0.1, 0.9]
    print(f'Seleciona multiplos elementos: {random.seleciona_multiplos_elementos(simbolos, peso, 4)}')

if __name__ == "__main__":
    main()