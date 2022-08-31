FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN apt-get -y update

RUN apt-get install -y python3 && apt-get install python3-pip

CMD ["./run_bot.sh"]