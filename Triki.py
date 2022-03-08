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

def obtener_filas_columans_diagonales(tablero):
    filas_columnas_y_diagonales = []
    indices = [1, 3, 5]

    # Para filas:
    for linea in [0, 2, 4]:
        filas_columnas_y_diagonales.append([tablero[linea][k] for k in indices])
    
    # Para las colmunas:
    for k in indices:
        filas_columnas_y_diagonales.append([tablero[linea][k] for linea in [0, 2, 4]])

    # Para las diagonales
    filas_columnas_y_diagonales.append([tablero[0][1], tablero[2][3], tablero[4][5]])
    filas_columnas_y_diagonales.append([tablero[0][5], tablero[2][3], tablero[4][1]])

    return filas_columnas_y_diagonales

def comprobar_si_hay_ganador(valor_X_O, lista_filas_columnas_diagonales):
    pass

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