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

class Sudoku:
    # Propiedades
    grid_inicial = [
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
    completed = False
    correct = False

    def __init__(self, cadena):
        self.cadena = cadena
        cadena = str(cadena)
        if len(cadena) == 81:
            for i in range(9):
                for j in range(9):
                    self.grid_inicial[i][j] = int(cadena[i*9+j])
        else:
            raise Exception('LengthError: La longitud de la cadena debe ser de 81 caracteres')

    # Metodos
    def posibilities(self):
        """Coloca la posibilidad de valor en cada casilla que no tenga un valor 
        previamente no tenga un valor definido"""
        for i in range(9):
            for j in range(9):
                if self.grid_inicial[i][j] == 0:
                    self.grid_inicial[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def is_complete(self):
        """Verifica si en el sudoku los valores colocados son todos enteros"""
        for i in range(9):
            for j in range(9):
                if type(self.grid_inicial[i][j]) == type([]):
                    self.completed = False
                    return 0
        self.completed = True
        return 1

    def make_string(self):
        cadena_prov = ''
        for i in range(9):
            for j in range(9):
                if type(self.grid_inicial[i][j]) == type(1):
                    cadena_prov += str(self.grid_inicial[i][j])
                elif type(self.grid_inicial[i][j]) == type([]):
                    cadena_prov += 'p'
        self.cadena = cadena_prov

    def __substitute(self):
        for i in range(9):
            for j in range(9):
                if type(self.grid_inicial[i][j]) == type([]):
                    if len(self.grid_inicial[i][j]) == 1:
                        self.grid_inicial[i][j] = self.grid_inicial[i][j][0]
                    else:
                        pass
                else:
                    pass

    def __solve_horizontal(self, value, x, y):
        for i in range(9):
            if type(self.grid_inicial[x][i]) == type([]):
                if self.grid_inicial[x][i].count(value) != 0:
                    self.grid_inicial[x][i].remove(value)

    def __solve_vertical(self, value, x, y):
        for j in range(9):
            if type(self.grid_inicial[j][y]) == type([]):
                if self.grid_inicial[j][y].count(value) != 0:
                    self.grid_inicial[j][y].remove(value)

    def __solve_area(self):
        pass

    def solve(self, iteraciones):
        for _ in range(iteraciones):
            for i in range(9):
                for j in range(9):
                    if type(self.grid_inicial[i][j]) == type(6):
                        self.__solve_horizontal(self.grid_inicial[i][j], i, j)
                        self.__solve_vertical(self.grid_inicial[i][j], i, j)
                        self.__solve_area()
                        self.__substitute()

def imprimir(sudokuclase):
    sudokuclase.make_string()
    cadena = sudokuclase.cadena
    if type(cadena) == type('2'):
        if len(cadena) != 81:
            raise Exception('LengthError: La longitud de la cadena debe ser de 81 caracteres')
        print(f"""\t┌ — — — ┬ — — — ┬ — — — ┐
        | {cadena[0]} {cadena[1]} {cadena[2]} | {cadena[3]} {cadena[4]} {cadena[5]} | {cadena[6]} {cadena[7]} {cadena[8]} |
        | {cadena[9]} {cadena[10]} {cadena[11]} | {cadena[12]} {cadena[13]} {cadena[14]} | {cadena[15]} {cadena[16]} {cadena[17]} |
        | {cadena[18]} {cadena[19]} {cadena[20]} | {cadena[21]} {cadena[22]} {cadena[23]} | {cadena[24]} {cadena[25]} {cadena[26]} |
        | — — — ┼ — — — ┼ — — — |
        | {cadena[27]} {cadena[28]} {cadena[29]} | {cadena[30]} {cadena[31]} {cadena[32]} | {cadena[33]} {cadena[34]} {cadena[35]} |
        | {cadena[36]} {cadena[37]} {cadena[38]} | {cadena[39]} {cadena[40]} {cadena[41]} | {cadena[42]} {cadena[43]} {cadena[44]} |
        | {cadena[45]} {cadena[46]} {cadena[47]} | {cadena[48]} {cadena[49]} {cadena[50]} | {cadena[51]} {cadena[52]} {cadena[53]} |
        | — — — ┼ — — — ┼ — — — |
        | {cadena[54]} {cadena[55]} {cadena[56]} | {cadena[57]} {cadena[58]} {cadena[59]} | {cadena[60]} {cadena[61]} {cadena[62]} |
        | {cadena[63]} {cadena[64]} {cadena[65]} | {cadena[66]} {cadena[67]} {cadena[68]} | {cadena[69]} {cadena[70]} {cadena[71]} |
        | {cadena[72]} {cadena[73]} {cadena[74]} | {cadena[75]} {cadena[76]} {cadena[77]} | {cadena[78]} {cadena[79]} {cadena[80]} |
        └ — — — ┴ — — — ┴ — — — ┘""")
    else:
        raise TypeError

if __name__ == "__main__":
    s1 = '005407000200065089603002704032058000806000003509043678300789040400536000007120806'
    sudoku = Sudoku(s1)
    print(type(sudoku))
    imprimir(sudoku)
    print('\n\n')
    sudoku.posibilities()
    sudoku.solve(10)
    imprimir(sudoku)

#