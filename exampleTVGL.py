import numpy as np 

from TVGL_L1 import TVGL_L1
from TVGL_L2 import TVGL_L2
from TVGL_Laplacian import TVGL_Laplacian
from TVGL_Linf import TVGL_Linf
from TVGL_PN import TVGL_PN


Cov = np.array([[5, 1], [1, 7]])
data = np.random.multivariate_normal(np.zeros(2), Cov, 50)

data = np.genfromtxt('./TVGL_py3/PaperCode/Datasets/finance.csv', delimiter=',')
data = data[0:30,0:10]
lamb = 2.5
beta = 12
lengthOfSlice = 10

def TVGL(data, lengthOfSlice, lamb, beta, indexOfPenalty, verbose = False, eps = 3e-3, epsAbs = 1e-3, epsRel = 1e-3):  
    if indexOfPenalty == 1:
        print('Use l-1 penalty function')
        thetaSet = TVGL_L1(data, lengthOfSlice, lamb, beta, verbose=True)
    
    elif indexOfPenalty == 2:
        print('Use l-2 penalty function')
        thetaSet = TVGL_L2(data, lengthOfSlice, lamb, beta, verbose=True)

    elif indexOfPenalty == 3:
        print('Use laplacian penalty function')
        thetaSet = TVGL_Laplacian(data, lengthOfSlice, lamb, beta, verbose=True)
    
    elif indexOfPenalty == 4:
        print('Use l-inf penalty function')
        thetaSet = TVGL_Linf(data, lengthOfSlice, lamb, beta, verbose=True)
    elif indexOfPenalty == 5:
        print('Use perturbation node penalty function')
        thetaSet = TVGL_PN(data, lengthOfSlice, lamb, beta, verbose=True)
    else:
        raise Exception("Wrong penalty selection")

    return thetaSet


thetaSet = TVGL(data, lengthOfSlice, lamb, beta, indexOfPenalty = 6, verbose=True)
print(thetaSet)



