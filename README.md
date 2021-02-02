# challenge
Pruebas

Prerequisitos
Descargar el repositorio mediante git clone 
ingresar a la carpeta challenge
tener previamente instalado docker para ejecutar una imagen

Ejecucion
1. Estar en la ruta donde este el archivo Dockerfile
2. docker build -t "meli:v1" .
3. 
root@ubuntu:/home/kandalf/Documents/Docker# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
meli                v1                  4623d7d5b487        4 seconds ago       1.35GB
ubuntu              latest              f63181f19b2f        12 days ago         72.9MB

4
root@ubuntu:/home/kandalf/Documents/Docker# docker run -dti --name meli 4623d7d5b487

5.
docker run -ti 4623d7d5b487  bash

6. 
root@67437b96ecc2:/# cd /home/Docker/meli/
root@67437b96ecc2:/home/Docker/meli# ls -alh
total 36K
drwxr-xr-x 2 root root 4.0K Feb  2 21:54 .
drwxr-xr-x 1 root root 4.0K Feb  2 21:55 ..
-rw-rw-r-- 1 root root 1.3K Feb  2 18:18 BD.json
-rwxrwxr-x 1 root root 1.1K Feb  1 23:57 conexion.py
-rw-rw-r-- 1 root root  191 Jan 28 21:02 info_usuario.csv
-rwxrwxr-x 1 root root 1.9K Feb  2 00:36 insertar_datos_bd.py
-rwxrwxr-x 1 root root 1.1K Feb  2 00:29 lecturas.py
-rw-rw-r-- 1 root root 1.2K Feb  2 21:44 resultado.json
-rwxrwxr-x 1 root root 1.2K Feb  2 21:42 validar_datos_json.py
root@67437b96ecc2:/home/Docker/meli# python3 validar_datos_json.py

7. 
root@67437b96ecc2:/home/Docker/meli# python3 validar_datos_json.py

"Siga las instrucciones de lo solicitado en CLI, hacer uso de Y7y o N/n para tomar decision.
Ejemplo de ejecucion de script
root@67437b96ecc2:/home/Docker/meli# python3 validar_datos_json.py
 * Starting MySQL database server mysqld                                                                                                                         [ OK ]
 * Starting Postfix Mail Transport Agent postfix                                                                                                                 [ OK ]
datos incompleto en el ID7
¿Desea corregir los datos?      y/Y/n/N:     n
los datos fueron insertados en la BD........................[OK]
Datos de json y csv insertados en base de datos........................................[OK]
Desea enviar correo de confirmacion
y
Se envio correo a:...... manager1@yopmail.com con la solicitud de confirmacion de la BD:..... rrhh
Se envio correo a:...... manager3@yopmail.com con la solicitud de confirmacion de la BD:..... contabilidad
Se envio correo a:...... manager3@yopmail.com con la solicitud de confirmacion de la BD:..... cliente
Se envio correo a:...... owner3@yopmail.com con la solicitud de confirmacion de la BD:..... publicidad

root@67437b96ecc2:/home/Docker/meli# mailq
-Queue ID-  --Size-- ----Arrival Time---- -Sender/Recipient-------
DA992101CC0      453 Tue Feb  2 21:57:47  root@67437b96ecc2
           (connect to smtp.yopmail.com[87.98.164.155]:25: Connection refused)
                                         owner3@yopmail.com

D3EB7101CBF      452 Tue Feb  2 21:57:47  root@67437b96ecc2
           (connect to smtp.yopmail.com[87.98.164.155]:25: Connection refused)
                                         manager3@yopmail.com

C0CD4101CBA      449 Tue Feb  2 21:57:47  root@67437b96ecc2
           (connect to smtp.yopmail.com[87.98.164.155]:25: Connection refused)
                                         manager1@yopmail.com

C8D6D101CBD      457 Tue Feb  2 21:57:47  root@67437b96ecc2
           (connect to smtp.yopmail.com[87.98.164.155]:25: Connection refused)
                                         manager3@yopmail.com

-- 1 Kbytes in 4 Requests.




