import json
import os
os.system('service mysql start && service postfix start')

input_file=open('BD.json', 'r')
json_decode=json.load(input_file)
for item in json_decode:
    my_dict={}
    my_dict['ID']=item.get('ID')
    my_dict['nombre']=item.get('nombre_bd')
    my_dict['user_id']=item.get('user_id')
    my_dict['criticidad']=item.get('criticidad')
    my_dict['tipo_usuario']=item.get('tipo_usuario')
    if (my_dict['ID']) == 'null' or my_dict['nombre'] == 'null' or my_dict['user_id'] =='null' or my_dict['criticidad']== 'null' or my_dict['tipo_usuario']== 'null' :
        print ("datos incompleto en el ID", end=f"{my_dict['ID']} \n")
        print("¿Desea corregir los datos?      ", end="y/Y/n/N:     ")
        decision = input()
        if decision == "Y" or decision == "y":
            print ("corrija los datos y ejecute de nuevo este script")
            exit()
        elif decision == "N" or decision == "n":
            print ("los datos fueron insertados en la BD........................[OK]")
            exec(open('lecturas.py').read())
            exit()
else:
    exec(open('lecturas.py').read())
