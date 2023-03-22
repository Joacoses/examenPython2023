import csv

f = 'examenPython\examenPython2023\\winequality.csv'
def read_data(fichero):
    contador = 0
    dic = {}
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contador += 1
            for i in row:
                dic = {tuple(row[i] : )}
                dic = {'dato'+str(contador): 'John', tuple(row):'values'}
           
            print(dic)

res = read_data(f)