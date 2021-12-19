FROM ubuntu:20.04

WORKDIR /usr/src/app

ENV TZ=Europe/Istanbul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y htop net-tools iputils-ping wget
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y ray
RUN pip3 install numpy
RUN pip3 install ray
RUN pip3 install flask

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]