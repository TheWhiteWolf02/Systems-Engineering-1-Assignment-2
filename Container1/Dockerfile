FROM ubuntu:16.04
      
MAINTAINER Shifat Ur Rahman <shifat_ur.rahman@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

# add more stuff here
RUN apt install -y openssh-server

RUN useradd -rm -d /home/ubuntu --shell /bin/bash --groups sudo -u 1000 ubuntu
RUN passwd -u -d ubuntu

COPY gitlab_id_rsa.pub /home/ubuntu/.ssh/
COPY new /home/ubuntu/.ssh/
COPY new.pub /home/ubuntu/.ssh/
COPY id_rsa /home/ubuntu/.ssh/
COPY id_rsa.pub /home/ubuntu/.ssh/

RUN cd /home/ubuntu/.ssh/ && cat id_rsa.pub >> authorized_keys && cat gitlab_id_rsa.pub >> authorized_keys && cat new.pub >> authorized_keys && touch /home/ubuntu/.ssh/known_hosts
RUN chmod 777 /home/ubuntu/.ssh/
RUN chmod 777 /home/ubuntu/.ssh/known_hosts
RUN chmod 777 /home/ubuntu/.ssh/new /home/ubuntu/.ssh/new.pub

EXPOSE 22

RUN apt update && apt -y install libevent-dev
RUN apt update && apt -y install build-essential
RUN wget http://www.memcached.org/files/memcached-1.4.33.tar.gz && tar -zxf memcached-1.4.33.tar.gz && cd memcached-1.4.33 && ./configure --prefix=/usr/local/memcached && make && make test && make install

RUN service ssh start

CMD [ "/usr/sbin/sshd", "-D" ]
