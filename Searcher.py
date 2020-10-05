#from bs4 import BeautifulSoup
import requests
import json
import os

# API's to use
#
# utep

class Cadena:
    def __init__(self):
        for i in os.listdir():
            if i == 'Guardados':
                return None
        os.mkdir('Guardados')
        return None

    def utep_api(self, level):
        source = requests.get(f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level={level}').text
        answer = json.loads(source)
        if answer.get('response') == False:
            raise Exception('Failed request')
        valores = answer.get('squares')
        list_prov = [ list('0'*9) for _ in range(9)]
        for elemento in valores:
            list_prov[elemento.get('x')][elemento.get('y')] = elemento.get('value')
        str_prov = ''
        for i in range(9):
            for j in range(9):
                str_prov += str(list_prov[i][j])
        return str_prov
    
    def local_charge(self, number):
        source = f'Guardados/{number}.sdku'
        

if __name__ == "__main__":
    sudoku1 = Cadena()
    print(sudoku1.utep_api(1))

#