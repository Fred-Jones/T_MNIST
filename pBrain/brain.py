from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer, SoftmaxLayer
test = buildNetwork(3, 5, 1)
print test['in'], test['out'], test['hidden0']
ds = SupervisedDataSet(3, 1)
ds.addSample((1,2,3), 0)
ds.addSample((3,3,3), 0)
ds.addSample((1,7,1), 0)
ds.addSample((7,6,5), 1)
ds.addSample((5,5,5), 1)
ds.addSample((1,2,9), 1)

trnr = BackpropTrainer(test, ds)
print trnr.trainUntilConvergence()
print test.activate([1,2,3])
print test.activate([3,2,4])
print test.activate([8,1,1])
print test.activate([1,9,1])
