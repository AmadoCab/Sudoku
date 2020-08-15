GRID_INICIAL = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

GUIDE = """/ 1 2 3 4 5 6 7 8 9
A
B
C
D
E
F
G
H
I
"""

def imprimir(matriz):
    for i in range(9):
        print(matriz[i])
    print('\n')

def generate_sudoku(cadena):
    cadena = str(cadena)
    while len(cadena) != 81:
        print('La longitud de la cadena a ingresar debe ser de 81 caracteres')
        print('intentelo una vez más.')
        cadena = input('Reingrese el sudoku: ')
    for i in range(9):
        for j in range(9):
            GRID_INICIAL[i][j] = int(cadena[i*9+j])
    imprimir(GRID_INICIAL)

def make_from_i():
    pass

def make_from_str():
    print('Ingrese una cadena de la configuración de su sudoku')
    print('los valores que desconozca marquelos con un 0, no utilice espacios')
    print('los valores se colocaran por fila, correspondiendo los primeros')
    print('nueve a los valores Ai, i=1,2,...,9. y sucesivamente.')
    entrada = input('Ingrese su sudoku: ')
    generate_sudoku(entrada)

def posibilities():
    for i in range(9):
        for j in range(9):
            if GRID_INICIAL[i][j] == 0:
                GRID_INICIAL[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solve_horizontal(value, i, j):
    for x in range(9):
        if type(GRID_INICIAL[i][x]) == type([]):
            if GRID_INICIAL[i][x].count(value) != 0:
                GRID_INICIAL[i][x].remove(value)

def solve_vertical(value, i, j):
    for y in range(9):
        if type(GRID_INICIAL[y][j]) == type([]):
            if GRID_INICIAL[y][j].count(value) != 0:
                GRID_INICIAL[y][j].remove(value)

def solve_square(value, i, j):
    if 0<=i<3 and 0<=j<3:
        for x in range(0,3):
            for y in range(0,3):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 3<=i<6 and 0<=j<3:
        for x in range(0,3):
            for y in range(3,6):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 6<=i<9 and 0<=j<3:
        for x in range(0,3):
            for y in range(6,9):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 0<=i<3 and 3<=j<6:
        for x in range(3,6):
            for y in range(0,3):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 3<=i<6 and 3<=j<6:
        for x in range(3,6):
            for y in range(3,6):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 6<=i<9 and 3<=j<6:
        for x in range(3,6):
            for y in range(6,9):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 0<=i<3 and 6<=j<9:
        for x in range(6,9):
            for y in range(0,3):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 3<=i<6 and 6<=j<9:
        for x in range(6,9):
            for y in range(3,6):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)
    elif 6<=i<9 and 6<=j<9:
        for x in range(6,9):
            for y in range(6,9):
                if type(GRID_INICIAL[y][x]) == type([]):
                    if GRID_INICIAL[y][x].count(value) != 0:
                        GRID_INICIAL[y][x].remove(value)

def solve():
    for i in range(9):
        for j in range(9):
            if type(GRID_INICIAL[i][j]) == type(6):
                solve_horizontal(GRID_INICIAL[i][j], i, j)
                solve_vertical(GRID_INICIAL[i][j], i, j)
                solve_square(GRID_INICIAL[i][j], i, j)
                substitute()
                imprimir(GRID_INICIAL)
            else:
                pass

def substitute():
    for i in range(9):
        for j in range(9):
            if type(GRID_INICIAL[i][j]) == type([]):
                if len(GRID_INICIAL[i][j]) == 1:
                    GRID_INICIAL[i][j] = GRID_INICIAL[i][j][0]
                else:
                    pass
            else:
                pass

def is_solved():
    for i in range(9):
        for j in range(9):
            if GRID_INICIAL[i][j] == type([]):
                return False
    return True

s1 = '005407000200065089603002704032058000806000003509043678300789040400536000007120806'
generate_sudoku(s1)
posibilities()

for _ in range(3):
    solve()

print(GUIDE)