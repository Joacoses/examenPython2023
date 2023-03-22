import csv

f = 'examenPython\examenPython2023\\winequality.csv'
dic_final = {}
def read_data(fichero):
    contador = 0
    datos = ["type", "fixed acidity", "volatile acidity", "citric acidity", "residual sugar", " chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "PH", "sulphates", "alcohol"]

    #leer
    with open(fichero, 'r') as file:
        reader = csv.reader(file)

        #inicializamos contador y transformamos a tupla para tratar mas facilmente
        for row in reader:
            contador += 1
            tuple(row)

            #juntamos los datos del csv con el texto
            lista_tuplas = list(zip(datos, row))
            diccionario = dict(lista_tuplas)

            #diccionario final
            for i in diccionario:
                dic_final.update({"dato"+ str(contador): diccionario})

    return dic_final
    

res = read_data(f)

def split(d):
    dic_white = {}
    dic_red = {}
    contador_white = 0
    contador_red = 0
    for dicctionary in d.values():
        #pillamos la clave para comparar con "success"
        for key in dicctionary.keys():
            if key == "type" and dicctionary.get(key) == "white":
                contador_white += 1
                dic_white.update({dicctionary})
        print(dic_white)




res2 = split(dic_final)

