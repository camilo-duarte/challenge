import json
import mysql.connector
import os


input_file=open('resultado.json', 'r')
json_decode=json.load(input_file)
miConexion = mysql.connector.connect( user='root', host='127.0.0.1', password='izv#HIu2Y', database='clasificacion_info')
mycursor = miConexion.cursor()
for item in json_decode:
    my_dict={}
    my_dict['ID']=item.get('ID')
    my_dict['nombre']=item.get('nombre_bd')
    my_dict['user_id']=item.get('user_id')
    my_dict['criticidad']=item.get('criticidad')
    my_dict['tipo_usuario']=item.get('tipo_usuario')
    sql = "INSERT INTO tb_clasificacion_info (nombre_bd,tbl_id_user,tbl_criticidad_info) VALUES (%s, %s, %s)"
    val = (my_dict['nombre'],my_dict['user_id'],my_dict['criticidad'])
    mycursor.execute(sql, val)
    miConexion.commit()
print("Datos de json y csv insertados en base de datos........................................[OK]")
#preguntar si desea enviar correo a los manager con criticidad alta
print ("Desea enviar correo de confirmacion")
query = input()
if query == "y" or query == "Y":
    #query = "select tb_clasificacion_info.tbl_id_user, tbl_id_tipo_usuario, owner, tbl_user.correo_usuario,tb_clasificacion_info.nombre_bd,tb_clasificacion_info.tbl_criticidad_info from tb_clasificacion_info,tbl_user where tbl_criticidad_info = 'alta' and tbl_id_user = id_usuario;"
    query = "select correo_usuario,nombre_bd from tb_clasificacion_info,tbl_user where tbl_criticidad_info = 'alta' and tbl_id_user = id_usuario"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        os.system('echo "por favor de respuesta mediante este correo la calificacion de la base de datos %s" |mail -s "calificacion riesgo BD" %s' %(x[1],x[0]))
        print("Se envio correo a:......",x[0],"con la solicitud de confirmacion de la BD:.....",x[1])
miConexion.close()


