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


class NeuralNet:
    def __init__(self):
        weight = np.array([0,1])
        bias = 0

        self.hidden_neuron1 = Neuron(bias,weight)
        self.hidden_neuron2 = Neuron(bias,weight)
        self.output_neuron = Neuron(bias,weight)

    def propagate(self,input):
        o_h1 = self.hidden_neuron1.neuron_propage(input)
        o_h2 = self.hidden_neuron2.neuron_propage(input)

        o1 = self.output_neuron.neuron_propage(np.array([o_h1,o_h2]))
        return o1

n_net = NeuralNet()
input = np.array([2,3])

print(n_net.propagate(input))