FROM python:3.7-buster
ENV TZ="America/Sao_Paulo"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update
RUN apt upgrade -y 
RUN apt install awscli -y 
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python-dev \
    python-numpy \
    python-protobuf\
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN aws configure set region us-east-1 
RUN aws configure set aws_access_key_id AKIA5QBC3TLEVI2DPPNE
RUN aws configure set aws_secret_access_key  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

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

WORKDIR /heatmap
COPY . /heatmap
WORKDIR /heatmap
RUN  pip3 install -r requirements.txt	
CMD python3.7 ./run.py 
