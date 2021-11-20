
#python -m graphsage.supervised_train --train_prefix ./example_data/ppi --model graphsage_mean --sigmoid

from __future__ import division
from __future__ import print_function

import os
import time
import tensorflow as tf
import numpy as np

from graphsage.models import SampleAndAggregate, SAGEInfo, Node2VecModel
from graphsage.minibatch import EdgeMinibatchIterator
from graphsage.neigh_samplers import UniformNeighborSampler
from graphsage.utils import load_data
    

def main(argv=None):
    print("Loading training data..")
    train_data = load_data("./example_data/toy-ppi", load_walks=True)
    print("train_data: " + str(len(train_data)))

if __name__ == '__main__':
    tf.app.run()
#python -m graphsage.run_final_comp --train_prefix ./example_data/ppi --model node2vec --max_total_steps 1000 --validate_iter 10