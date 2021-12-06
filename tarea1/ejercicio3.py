def resuelve(casillas, valores_por_acomodar):
    # Si ya no tenemos valores que acomodar, entonces hemos encontrado una solución
    if not valores_por_acomodar:
        return casillas
    # En otro caso, apara cada valor que aún no tiene lugar
    for n in valores_por_acomodar:
        # Iteramos nuestro diccionario
        for i in range(4):
            for j in range(4):
                # Obtenemos el valor en la posición actual, en caso de no ser
                # parte del diccionario, regresamos un False
                posicion = casillas.get((i,j), 'Vacio')
                # Si la posición actual no es una casilla, continuamos a la siguiente
                if posicion == 'Vacio':
                    continue
                # Si la posición actual es vacía, entonces es posible que aquí podamos acomodar
                # el número n
                if posicion == None:
                    # Para poder colocar un número, los vecinos no pueden ser números consecutivos
                    # por lo que obtenemos a los vecinos, en caso de no ser una casilla, devolvemos None
                    arriba = casillas.get((i-1,j), None)
                    abajo = casillas.get((i+1,j), None)
                    der = casillas.get((i,j+1), None)
                    izq = casillas.get((i,j-1), None)
                    # y checamos que, en caso de ya tener un valor asignado, cumplamos con la condición
                    # en otro caso, debemos seguir buscando por un valor que poner en esta casilla
                    if arriba != None and (n == arriba + 1 or n == arriba - 1):
                        continue
                    if abajo != None and (n == abajo + 1 or n == abajo - 1):
                        continue
                    if der != None and (n == der + 1 or n == der - 1):
                        continue
                    if izq != None and (n == izq + 1 or n == izq - 1):
                        continue
                    # Si sí podemos colocar n en esta posición, lo hacemos en una nueva solución
                    # para que en caso de que esta posible solución falle, se pueda continuar
                    # con la busqueda
                    posible_solucion = casillas.copy()
                    # Asignamos a la casilla el posible lugar de n
                    posible_solucion[(i,j)] = n
                    # Obtenemos una copia de los valores que aún no hemos podido acomodar
                    lista_menos_n = valores_por_acomodar[:]
                    # Eliminamos n ya que este ya fue acomodado en la posición (i,j)
                    lista_menos_n.remove(n)
                    # Y hacemos recursión para calcular la solución
                    solucion = resuelve(posible_solucion, lista_menos_n)
                    # Si la solución obtenida no es vacía, es porque hemos logrado acomodar todos
                    # los números en alguna casilla
                    if solucion:
                        return solucion
    # Si terminamos de iterar los números y no conseguimos una solución, entonces esta es una
    # solución fallida, por lo que regresamos una lista vacía para que se siga buscando una
    # solución
    return []


dict1 = {(0,1): 3, (0,2): None, (1,1): None, (1,2): 8
        ,(2,0): None, (2,1): None, (2,2): 6, (2,3): None}

print('Una posible solución es la siguiente:')
print(resuelve(dict1, [1,2,4,5,7]))