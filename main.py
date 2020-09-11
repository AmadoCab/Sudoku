import Sudoku as s
import Searcher as fs

#finder = fs.Cadena()

#cadena = finder.utep_api(1)

cadena = '006904080083000900504036007840050009960070058005680240300540806600208030000103792'

print(cadena, end='\n\n')

puzzle = s.Sudoku(cadena)
s.imprimir(puzzle)
print('\n\n')
puzzle.posibilities()
puzzle.solve(10)
s.imprimir(puzzle)
print(puzzle.make_status())

#