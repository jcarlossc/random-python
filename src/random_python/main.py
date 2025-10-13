from random_python.ClasseAleatoria import ClasseAleatoria

def main():
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f' ESTUDO SOBRE O MÓDULO RANDOM EM LINGUAGEM PYTHON')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    aleatorio = ClasseAleatoria()
    print(f'Gera float entre 0 e 1: {aleatorio.gera_float():.2f}')
    print(f'Gera float entre os parâmetros: {aleatorio.gera_float_entre(1, 2):.2f}')










if __name__ == "__main__":
    main()