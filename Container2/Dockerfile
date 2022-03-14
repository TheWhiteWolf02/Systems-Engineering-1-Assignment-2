FROM ubuntu:16.04
      
MAINTAINER Shifat Ur Rahman <shifat_ur.rahman@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt -y install python

RUN apt install -y openssh-server

RUN useradd -rm -d /home/ubuntu --shell /bin/bash --groups sudo -u 1000 ubuntu

COPY gitlab_id_rsa.pub /home/ubuntu/.ssh/
COPY new /home/ubuntu/.ssh/
COPY new.pub /home/ubuntu/.ssh/
COPY id_rsa /home/ubuntu/.ssh/
COPY id_rsa.pub /home/ubuntu/.ssh/

RUN cd /home/ubuntu/.ssh/ && cat id_rsa.pub >> authorized_keys && cat gitlab_id_rsa.pub >> authorized_keys && cat new.pub >> authorized_keys && touch /home/ubuntu/.ssh/known_hosts

COPY Benchmark.py /home/ubuntu
COPY Dudefile /home/ubuntu
COPY graphs.R /home/ubuntu
COPY run.sh /home/ubuntu

RUN chmod +x /home/ubuntu/run.sh
RUN chmod 777 /home/ubuntu/.ssh/known_hosts
RUN chmod 777 /home/ubuntu/.ssh/new /home/ubuntu/.ssh/new.pub

EXPOSE 22

RUN apt update && apt -y install libevent-dev
RUN apt update && apt -y install build-essential

# mcperf
RUN wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz && tar -zxf mcperf-0.1.1.tar.gz && cd mcperf-0.1.1 && ./configure && make && make install

# dude
RUN apt -y install unzip
RUN wget https://bitbucket.org/db7/dude/get/fea6e9012597.zip
RUN mkdir dude && unzip fea6e9012597.zip -d dude/
RUN cd dude/db7-dude-fea6e9012597/ && python setup.py install

# R
RUN apt-get install -y r-base

RUN service ssh start

CMD [ "/usr/sbin/sshd", "-D" ]
