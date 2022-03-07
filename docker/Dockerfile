FROM debian:latest

RUN apt update -y && apt install -y sudo apt-utils wget python3-pip python3-venv python3-dev python3-pandas git curl
COPY ./install_ta_lib.sh /install_ta_lib.sh

RUN bash install_ta_lib.sh

RUN adduser --disabled-password --home /home/container container

WORKDIR /home/container
USER root

USER container
ENV  USER=container HOME=/home/container

COPY ./entrypoint.sh /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]
