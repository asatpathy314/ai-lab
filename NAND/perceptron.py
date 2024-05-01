from random import random, choice
import numpy as np

class Perceptron():
    """ A naive implementation of a perceptron.

    Args:
        num_inputs (int) : Number of inputs to the perceptron.
        learning_rate (float) : Learning rate, initialized to 0.00001.
        weight_scale : Random initialization multiplier.
        bias : Negative threshold of the perceptron.
    """

    def __init__(self, num_inputs=0, learning_rate = 0.00001, weight_scale = 1, threshold = 1):
        self.learning_rate = learning_rate
        self.bias = -1 * threshold
        self.weights = np.array([random()*weight_scale*choice((1, -1)) for i in range(num_inputs)])

    def rule_function(self, value):
        """ Determines a binary output given a float value """
        if isinstance(value, float) or isinstance(value, int):   
            if value + self.bias <= 0:
                return 0
            else:
                return 1
        else:
            raise ValueError("Input is not of type float.")    
        
    def calculate_output(self, input):
        """ Calculates the outputs for any number of inputs stored in a matrix.

        Args:
            input (numpy.array)
        """

        if input.shape[1] != self.weights.shape[0]:
            raise ValueError(f"Dimensionality of input {input.shape[0]}x{input.shape[1]} " +
                             f"cannot be multiplied by weights of size {self.weights.shape[0]}x{self.weights.shape[1]}.")
        else:
            return np.vectorize(self.rule_function)(np.matmul(input, self.weights))


        
