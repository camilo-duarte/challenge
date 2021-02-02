import csv
import json
lista_general = []

filejson = open("BD.json", "r")
content = filejson.read()
jsondecoded = json.loads(content)
# print(jsondecoded)

lista = []
with open('info_usuario.csv', newline='') as filecsv:  
    csvdecoded = csv.reader(filecsv)
    for item in csvdecoded:
        lista.append(item[1].split(","))
#print(lista)
for data in jsondecoded:
    valor_buscar = data['user_id']
    for dat in lista:
        if valor_buscar == dat[0]:
            y = json.loads(valor_buscar)
            lista_general.append(data)

exec(open('conexion.py').read())

#print(lista_general)
            # guardar en la BD


 #guarda resultado en archivo json  
with open('resultado.json', 'w') as file:
    json.dump(lista_general, file, indent=4)
#print ("lectura archivo!")
#print (lista_general)


##f = open ('resultado.json', "r") 
#mostrar resultado linea por linea  
##data = json.loads(f.read()) 
# Iterating through the json 
# list 
##for i in data['BasesdeDatos']: 
##    print(i) 
# Closing file 
##f.close()



