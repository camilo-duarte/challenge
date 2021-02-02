#!/bin/bash
service postfix start
service mysql stop
usermod -d /var/lib/mysql/ mysql
service mysql start
mysql -u root -e "create database clasificacion_info"
mysql -u root clasificacion_info   < /home/Docker/mysql/script_bd_mysql.txt
mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'izv#HIu2Y';"
