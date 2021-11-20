FROM tensorflow/tensorflow:1.3.0

RUN pip install networkx==1.11
RUN pip install pandoc
RUN rm /notebooks/*

COPY . /notebooks
