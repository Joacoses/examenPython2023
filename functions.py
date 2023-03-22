import csv

f = 'examenPython\examenPython2023\\winequality.csv'
def read_data(fichero):
    contador = 0
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contador += 1
            for i in 
            dic = {}

            print(row)

res = read_data(f)