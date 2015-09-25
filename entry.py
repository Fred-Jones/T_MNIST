import numpy as np
import theano
import theano.tensor as T
import matplotlib.pyplot as plt

##helper function loads data located in ./data
from lib import GetData
tst, trn = GetData.read_csv()

## input vector
x = T.dvector('x')
## V: input to hidden weights
## W: hidden to output weights
V = T.dmatrix('V') ##V.shape = k x d
W = T.dmatrix('W') ##W.shape = m x h
## hidden layer bias
c = T.dvector('c')
## output units bias
b = T.dvector('b')
## map d vector to m vector
_G = b + W*T.tanh(c + V*x)

# g = theano.function([x, V, c, b], _G)
trn_labels = np.array(trn[['label']]).flatten()
print trn_labels[0:10]
#x_matrix = trn[!'label']

##FORWARD PROP##
##where L:layer i:node
##where a:activation as fxn of z:f(x_i, W_i)
##where c_L is the bias term for that layer
## a_1 = x
## a_L = sigmoid(z_L) + c_L

#GRADIENT#
## minimize cost J(W) as fxn of W
#### must supply J(W) & partial deriv d/dW for every i,j, and each layer
## ie must compute J(W) & d/dW J(W) where W is for every i,j,l
