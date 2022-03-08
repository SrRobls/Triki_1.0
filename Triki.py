modelo = [['|', 1, '|', 2, '|', 3, '|'],
          ['-------------------------'],
          ['|', 4, '|', 5, '|', 6, '|'],
          ['-------------------------'],
          ['|', 7, '|', 8, '|', 9, '|']]

def mostrar_triqui(modelo):
    for linea in modelo:
        for elemento in linea:
            print(elemento, end='   ')
        print()

mostrar_triqui(modelo)