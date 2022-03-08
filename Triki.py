tablero = [['|', 1, '|', 2, '|', 3, '|'],
          ['-------------------------'],
          ['|', 4, '|', 5, '|', 6, '|'],
          ['-------------------------'],
          ['|', 7, '|', 8, '|', 9, '|']]

def mostrar_triqui(tablero):
    for linea in tablero:
        for elemento in linea:
            print(elemento, end='   ')
        print()

def cambiar_celda(tablero, celda_a_cambiar, valor_X_O):
    for linea in tablero:
        if celda_a_cambiar in linea:
            ind = linea.index(celda_a_cambiar)
            linea[ind] = valor_X_O
            return tablero

i = 1
while i <= 9:
    if i % 2 != 0:
        print('Turno Del Jugador #1')
        celda_a_cambiar = int(input('¿En cual celda deseas porner la X?: '))
        cambiar_celda(tablero, celda_a_cambiar, 'X')
        mostrar_triqui(tablero)
    else:
        print('Turno Del Jugador #2')
        celda_a_cambiar = int(input('¿En cual celda deseas porner el O?: '))
        cambiar_celda(tablero, celda_a_cambiar, 'O')
        mostrar_triqui(tablero)

    i += 1