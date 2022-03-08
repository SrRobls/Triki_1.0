#Este tablero sirve de referencia al hora de verficar si ya sean puesto un valor X o O en el valor de la celda aportado por el ususario.
tablero_guia = [['|', 1, '|', 2, '|', 3, '|'],
                ['-------------------------'],
                ['|', 4, '|', 5, '|', 6, '|'],
                ['-------------------------'],
                ['|', 7, '|', 8, '|', 9, '|']]

# En este tablero es donde ser haran los cambios 
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

# Para verficar si la celda ya ha sido tomada o no:
def comproborar_valor_de_celda(tablero, celda_a_cambiar):
    for j in range(0, 5, 2):
        if celda_a_cambiar in tablero_guia[j]:
            ind = tablero_guia[j].index(celda_a_cambiar)
            if tablero[j][ind] == 'X' or tablero[j][ind] == 'O':
                return False
            return True

mostrar_triqui(tablero)
i = 1
celda_a_cambiar = 0
while i <= 9:
    if i % 2 != 0:

        print('Turno Del Jugador #1')
        while True:
            try:
                celda_a_cambiar = int(input('¿En cual celda deseas porner la X?: '))
            except ValueError:
                print('El valor es incorreto')
                continue
            if comproborar_valor_de_celda(tablero, celda_a_cambiar):
                break
            print('Esa celda ya esta ocupada o esta fuera de los parametros (los parameros son entre 0 a 9), intenta con otra.')
        cambiar_celda(tablero, celda_a_cambiar, 'X')
        mostrar_triqui(tablero)

    else:

        print('Turno Del Jugador #2')
        while True:
            try:
                celda_a_cambiar = int(input('¿En cual celda deseas porner la O?: '))
            except ValueError:
                print('El valor es incorreto')
                continue
            if comproborar_valor_de_celda(tablero, celda_a_cambiar):
                break
            print('Esa celda ya esta ocupada o esta fuera de los parametros (los parameros son entre 0 a 9), intenta con otra.')
        cambiar_celda(tablero, celda_a_cambiar, 'O')
        mostrar_triqui(tablero)

    i += 1
    if i > 9:
        print('Empate')