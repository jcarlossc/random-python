from random_python.ClasseAleatoria import ClasseAleatoria

def main():
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f' ESTUDO SOBRE O MÓDULO RANDOM EM LINGUAGEM PYTHON')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    aleatorio = ClasseAleatoria()
    print(f'Gera float entre 0 e 1: {aleatorio.gera_float():.2f}')
    print(f'Gera float entre os parâmetros: {aleatorio.gera_float_entre(1, 2):.2f}')
    print(f'Gera inteiro entre os parâmetros: {aleatorio.gera_inteiro_entre(1, 5)}')
    print(f'Gera inteiro com passos: {aleatorio.gera_inteiro_passos(1, 10, 2)}')










if __name__ == "__main__":
    main()