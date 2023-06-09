import random
import numpy as np

def sigmoid(x):
  #Sigmoid Squishification
  return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self,bias,weight):
        self.bias = bias
        self.weight = weight
    
    def neuron_propage(self,input):
        activate = np.dot(input,self.weight) + self.bias
        return sigmoid(activate)
