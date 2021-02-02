import mysql.connector
import json

input_file=open('resultado.json', 'r')
#output_file=open('test.json', 'w')
json_decode=json.load(input_file)
miConexion = mysql.connector.connect( user='root', host='127.0.0.1', password='izv#HIu2Y', database='clasificacion_info')
mycursor = miConexion.cursor()
#print("Succesfully Connected to database using MySQLdb!")
#for item in json_decode:
#    my_dict={}
#    my_dict['ID']=item.get('ID')
#    my_dict['nombre']=item.get('nombre_bd')
#    my_dict['user_id']=item.get('user_id')
#    my_dict['criticidad']=item.get('criticidad')
#    sql = "INSERT INTO tb_clasificacion_info (id_clasificacion,nombre_bd,tbl_id_user,tbl_criticidad_info) VALUES (%s, %s, %s, %s)"
#    val = (my_dict['ID'],my_dict['nombre'],my_dict['user_id'],my_dict['criticidad'])
#    mycursor.execute(sql, val)
#    miConexion.commit()

exec(open('insertar_datos_bd.py').read())

#query = "SELECT * FROM tb_clasificacion_info"
#mycursor.execute(query) 
#myresult = mycursor.fetchall() 
#for x in myresult: 
#    print(x) 
miConexion.close()
