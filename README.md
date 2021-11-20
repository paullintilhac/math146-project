## GraphSage: Representation Learning on Large Graphs

#### Authors: [William L. Hamilton](http://stanford.edu/~wleif) (wleif@stanford.edu), [Rex Ying](http://joy-of-thinking.weebly.com/) (rexying@stanford.edu)
#### [Project Website](http://snap.stanford.edu/graphsage/)

#### [Alternative reference PyTorch implementation](https://github.com/williamleif/graphsage-simple/)

### Overview

This directory contains code necessary to run the GraphSage algorithm.
GraphSage can be viewed as a stochastic generalization of graph convolutions, and it is especially useful for massive, dynamic graphs that contain rich feature information.
See our [paper](https://arxiv.org/pdf/1706.02216.pdf) for details on the algorithm.

For professor Mucha:

In order to run the ipython notebook in this repo, please first install docker. you can do that on the docker website:
https://docs.docker.com/get-docker/
Then, run the following commands:

	$ pip install -r requirements.txt
	$ docker build -t graphsage .
    $ docker run -it -p 8888:8888 graphsage

	This will generate a link on the command line that you can then use to open a jupyter notebook in the browser. 

	Sorry this is more complicated than I would like -- the repository I based my code on uses docker because it is meant to be deployed in production, and it would have been very difficult to get it to work outside of the container. 

	Alternatively, the pdf is also attached.