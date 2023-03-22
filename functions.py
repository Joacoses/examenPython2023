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
    #print(dic_final)
    return dic_final
    

#-------------------------------------------------------------------------------------------------------------------------------------------------
dic_white = {}
dic_red = {}
def split(d):
    contador_white = 0
    contador_red = 0
    for dicctionary in d.values():
        #pillamos la clave para comparar con "type"
        for key in dicctionary.keys():
            
            if key == "type" and dicctionary.get(key) == "white":
                contador_white += 1
                llave1 = tuple(dicctionary.keys())
                eliminar_llave = "type"
                llave_white = tuple([elemento for elemento in llave1 if elemento != eliminar_llave])

                valor1 = tuple(dicctionary.values())
                eliminar_valor_white = "white"
                valor_white = tuple([elemento for elemento in valor1 if elemento != eliminar_valor_white])


                lista_tuplas = list(zip(llave_white, valor_white))
                dic_white.update({"dato"+ str(contador_white): dict(lista_tuplas)})
            
            elif key == "type" and dicctionary.get(key) == "red":
                contador_red += 1

                llave1 = tuple(dicctionary.keys())
                eliminar_llave = "type"
                llave_red = tuple([elemento for elemento in llave1 if elemento != eliminar_llave])

                valor1 = tuple(dicctionary.values())
                eliminar_valor_red = "red"
                valor_red = tuple([elemento for elemento in valor1 if elemento != eliminar_valor_red])

                lista_tuplas_red = list(zip(llave_red, valor_red))

                dic_red.update({"dato"+ str(contador_red): dict(lista_tuplas_red)})

    #print(dic_white)
    #print(dic_red) 
    
    return dic_white, dic_red


#-------------------------------------------------------------------------------------------------------------------------------------------------
def reduce(d, string):
    datos = []
    for dicctionary in d.values():
        
        for key in dicctionary.keys():
            if key == string:
                datos.append(dicctionary.get(key))
            else:
                print("El dato introducido no se encuentra")
    return datos


