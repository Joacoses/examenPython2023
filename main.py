import csv

def read_data(fichero):
    with open('examenPython\examenPython2023\\winequality.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)