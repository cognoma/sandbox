FROM continuumio/miniconda3 

MAINTAINER Gregory Way <gregway@mail.med.upenn.edu>

RUN apt-get install -y vim

RUN git clone https://github.com/cognoma/sandbox.git 

RUN cd sandbox && conda env create --quiet --force --file environment.yml

