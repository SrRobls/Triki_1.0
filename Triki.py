import random
import os

# Este tablero sirve de referencia a la hora de verficar si ya sean puesto un valor X o O en el valor de la celda aportado por el ususario
# y tambien para reiniciar el tablero si el ususario quiere volever a jugar.
tablero_guia = [['|', 1, '|', 2, '|', 3, '|'],
                ['-------------------------'],
                ['|', 4, '|', 5, '|', 6, '|'],
                ['-------------------------'],
                ['|', 7, '|', 8, '|', 9, '|']]

# En este tablero es donde se haran los cambios y se mostrara por pantalla, y es donde se jugara
tablero = [['|', 1, '|', 2, '|', 3, '|'],
          ['-------------------------'],
          ['|', 4, '|', 5, '|', 6, '|'],
          ['-------------------------'],
          ['|', 7, '|', 8, '|', 9, '|']]

# Codigo de la interfaz de inicio
def interfaz_inicial():
    if opciones() == 1:
        print('Modo de Juego: Juagador Vs Jugador')
        mostrar_triqui(tablero)
        Jugador_Vs_Jugador()
    else:
        print('Modo de Juego: Juagador Vs Maquina')
        opcion2 = opcion2_opciones()
        if opcion2 == 1:
            print('Dificultad: Baja')
        elif opcion2 == 2:
            print('Dificultad: Media')
        elif opcion2 == 3:
            print('Dificultad: Alta')
        Juagdor_Vs_Maquina(opcion2)

# Funcion para mostrar el tablero
def mostrar_triqui(tablero):
    for linea in tablero:
        for elemento in linea:
            print(elemento, end='   ')
        print()

# Funcion para cambiar el valor de la celdad por el valor X o O.
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

# Funcion para obtener todas las filas, columnas y diagonales del tablero donde estamos juagndo
def obtener_filas_columans_diagonales(tablero):
    filas_columnas_y_diagonales = []
    # Notar que los indices de los elementos donde vamosa trabajar son estos. esto lo hago para obtener meramnete estos valores y no los '|'
    indices = [1, 3, 5]

    # Para filas:
    for linea in [0, 2, 4]: # Linea itera por cada una de los elementos/listas del tablero
        filas_columnas_y_diagonales.append([tablero[linea][k] for k in indices])
    
    # Para las colmunas:
    for k in indices:
        filas_columnas_y_diagonales.append([tablero[linea][k] for linea in [0, 2, 4]])

    # Para las diagonales
    filas_columnas_y_diagonales.append([tablero[0][1], tablero[2][3], tablero[4][5]])
    filas_columnas_y_diagonales.append([tablero[0][5], tablero[2][3], tablero[4][1]])

    return filas_columnas_y_diagonales

# Funcion para reiniciar el tablero, en caso de que se seguira jugando
def reiniciar_tablero():
    reinicio = [['|', 1, '|', 2, '|', 3, '|'],
                ['-------------------------'],
                ['|', 4, '|', 5, '|', 6, '|'],
                ['-------------------------'],
                ['|', 7, '|', 8, '|', 9, '|']]
    return reinicio


# Funcion para la interfaz inicial. Le pide al usario en que modo desea juagar 
def opciones(): 
    print('''Selecciona el modo de juego:
         1. Para Jugador Vs Jugador
         2. Para Jugador Vs Maquina''')
    opcion = 0
    while True:
        try:
            opcion = int(input('Opcion: '))
        except ValueError:
            print('Por favor, selecciona un valor valido.')
            continue
        if opcion > 2 or opcion < 0:
            print('Por favor, selecciona un valor valido.')
            continue
        return opcion

# En el caso de que el usuario decida jugar contra la maquina, en esta funcion le pedira en que dificultad.
def opcion2_opciones():
    print('''Ahora selecciona que difcultad:
                1. Para dificultad baja
                2. Para dificultad media
                3. Para dificultad alta''')
    while True:
        try:
            dificultad = int(input('Dificultad: '))
        except ValueError:
            print('Por favor, selecciona un valor valido.')
            continue
        if dificultad > 3 or dificultad < 0:
            print('Por favor, selecciona un valor valido.')
            continue
        return dificultad

# Le solicita al usuario en que turno dese comenzar, si de primero o de ultimo.
def opcion2_turnos():
    print('''Deseas comenzar de primero o de segundo?
             1. Para comenzar primero
             2. Para comenzar segundo''')
    comienzo = 0
    while True:
        try:
            comienzo = int(input('Seleciona: '))
        except ValueError:
            print('Por favor, selecciona un valor valido.')
            continue
        if comienzo > 2 or comienzo < 0:
            print('Por favor, selecciona un valor valido.')
            continue
        return comienzo

# Comprobamos si hay un ganador cuando algunos de los dos jugadores termina de introducir su valor.
def comprobar_si_hay_ganador(valor_X_O):
    for linea in obtener_filas_columans_diagonales(tablero):
        if all(valor == valor_X_O for valor in linea):
            return True
    return False

# La logica de modo facil de la maquina. basicamnete escoge las celdas vascias de forma aleatoria
def opcio2_maquina_facil(filas_columnas_diagonales):
    while True:
        linea = random.choice(filas_columnas_diagonales)
        valor_aleatorio = random.choice(linea)
        if valor_aleatorio != 'X' and valor_aleatorio != 'O':
            cambiar_celda(tablero, valor_aleatorio, 'O')
            break

# Funcion para que la mauina verifique si le falta un elemento para ganar, si es asi. coloca el valor correspondiente 'O' en esa celda y gana
# si no, sigue. esta funcion solo aplica para dificultada media y alta.
def maquina_apunto_de_ganar(filas_columnas_diagonales):
    lineas = filas_columnas_diagonales
    for linea in lineas:
        if linea.count('O') == 2 and linea.count('X') == 0:
            for i in linea:
                if i != 'O':
                    cambiar_celda(tablero, i, 'O')
                    break
            return True
    return False

# Funcion para la maquina en dificultad media 
def opcion2_maquina_medio(filas_columans_diagonales):
    if maquina_apunto_de_ganar(filas_columans_diagonales):
        return
    lineas = filas_columans_diagonales
    for linea in lineas:
        if linea.count('O') >= 1 and linea.count('X') >= 0:
            vlue = 0
            for i in linea:
                if i != 'O' and i != 'X':
                    vlue = i
                    cambiar_celda(tablero, vlue, 'O')
                    return
    opcio2_maquina_facil(lineas)

# Funcion para la maquina en dificultad alta
def opcion2_maquina_dificil(filas_columans_diagonales):
    if maquina_apunto_de_ganar(filas_columans_diagonales):
        return
    lineas = filas_columans_diagonales
    for linea in lineas:
        if linea.count('X') == 2 and linea.count('O') == 0:
            vlue = 0
            for i in linea:
                if i != 'X':
                    vlue = i
                    break
            cambiar_celda(tablero, vlue, 'O')
            return
    opcion2_maquina_medio(lineas)
            
        
# Funcion para ejecutar el codigo de Juagador Vs Jugador.
def Jugador_Vs_Jugador(): 
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
            if comprobar_si_hay_ganador('X'):
                print('El jugador #1 ha ganado. ¡Felicitaciones!.')
                print('El juego ha terminado.')
                break

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
            if comprobar_si_hay_ganador('O'):
                print('El jugador #2 ha ganado. ¡Felicitaciones!.')
                print('El juego ha terminado.')
                break

        i += 1
        if i > 9:
            print('Empate')
            print('El juego ha terminado.')

# Funcion para ejecutar el codigo de jugador vs maquina.
def Juagdor_Vs_Maquina(dificultad):
    i, final = 0, 0
    turno = opcion2_turnos()
    mostrar_triqui(tablero)

    if turno == 1:
        i, final = 1, 9
    else:
        i, final = 2, 10
    i_inicial = i
    while i <= final:
         
        if i % 2 != 0:
            print('Turno del juagdor')
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
            if comprobar_si_hay_ganador('X'):
                print('El jugador ha ganado. ¡Felicitaciones!.')
                print('El juego ha terminado.')
                break


        elif i % 2 == 0:
            print('Turno de la maquina')
            if dificultad == 1:
                opcio2_maquina_facil(obtener_filas_columans_diagonales(tablero))
                mostrar_triqui(tablero)
            elif dificultad == 2:
                if i == 1 or i == 2:
                    opcio2_maquina_facil(obtener_filas_columans_diagonales(tablero))
                    mostrar_triqui(tablero)
                    i += 1
                    continue
                opcion2_maquina_medio(obtener_filas_columans_diagonales(tablero))
                mostrar_triqui(tablero)
            elif dificultad == 3:
                if i == 1 or i == 2:
                    opcio2_maquina_facil(obtener_filas_columans_diagonales(tablero))
                    mostrar_triqui(tablero)
                    i += 1
                    continue
                opcion2_maquina_dificil(obtener_filas_columans_diagonales(tablero))
                mostrar_triqui(tablero)  

            if comprobar_si_hay_ganador('O'):
                print('La maquina te ha ganado :( ')
                print('El juego ha terminado.')
                break
        i += 1
        if i_inicial == 1:
            if i > 9:
                print('Empate')
                print('El juego ha terminado.')
        elif i_inicial == 2:
            if i > 10:
                print('Empate')
                print('El juego ha terminado.')


# Codigo principal.
print('Hola!, Bienvenido!')
while True:
    seguir = 0
    interfaz_inicial()
    while True:
        print('''Deseas Juagar Otra Partida?
                                    1. Si
                                    2. No''')
        try:
            seguir = int(input('Seleccion: '))
        except ValueError:
            print('Por favor escoge un valor valido.')
            continue
        if seguir > 2 and seguir <= 0:
            print('Por favor escoge un valor valido.')
            continue
        else:
            break
    if seguir == 2:
        os.system('cls')
        print('Gracias por jugar!!')    
        break
    os.system('cls')
    tablero = reiniciar_tablero()