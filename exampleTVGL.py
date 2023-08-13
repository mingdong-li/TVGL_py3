import TVGL as tvgl
import numpy as np 





Cov = np.array([[5, 1], [1, 7]])
data = np.random.multivariate_normal(np.zeros(2), Cov, 50)


data = np.genfromtxt('./TVGL_py3/PaperCode/Datasets/finance.csv', delimiter=',')
data = data[0:30,0:10]
lamb = 2.5
beta = 12
lengthOfSlice = 10
thetaSet = tvgl.TVGL(data, lengthOfSlice, lamb, beta, indexOfPenalty = 1, verbose=True)
print(thetaSet)



