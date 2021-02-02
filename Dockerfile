FROM ubuntu:latest
RUN mkdir -p /home/Docker/
RUN apt-get update
RUN apt-get install mysql-server -y
RUN apt-get install vim -y
RUN apt-get install python3-pip  -y 
RUN  pip3 install mysql-connector-python
COPY  meli /home/Docker/meli/
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get install -y mailutils
COPY mysql /home/Docker/mysql
RUN chmod a+x /home/Docker/mysql/mysql.sh
RUN cd /home/Docker/mysql/ && /bin/sh /home/Docker/mysql/mysql.sh
RUN cd /home/Docker/mysql/ 
CMD ["mysql", "start"]
RUN echo "maillog_file=/var/log/postfix.log" >> /etc/postfix/main.cf
CMD ["postfix", "start"]
