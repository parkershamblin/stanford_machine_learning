# coding python solution to linear regression problem
# described here: https://www.coursera.org/learn/machine-learning/lecture/N09c6/cost-function-intuition-i

import numpy as np
import matplotlib.pyplot as plt

tset = [(1, 1), (2,2), (3,3)]
xs = (1, 2, 3)


def hypothesis(x, p1):
    p0 = 0
    return p0+p1*x

def cost(p1):
    # fixed problem
    p1=p1-1
    derivative = (1 / (2*len(tset)))
    sum_differences = np.sum([hypothesis(x, p1)**2 for x in xs])
    return derivative * sum_differences

print(cost(-0.5))