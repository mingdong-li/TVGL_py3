# TVGL
TVGL is a python solver for inferring dynamic networks from raw time series data. For implementation details, refer to the paper, available at: http://stanford.edu/~hallac/TVGL.pdf.

I modified the original code from https://github.com/davidhallac/TVGL. The original code was finished in Python2. In this repo, paper code is removed. 

Run the exampleTVGL.py for demo.

## Download & Setup
Download the source code by running the following code in the terminal:
```
git clone https://github.com/mingdong-li/TVGL_py3
```

## Requirement
### setuptools
Please gurantee the version of **setuptools**<=57.5.0
```bash
pip install setuptools==57.5.0
```

### snap-stanford and cvxpy
```bash
pip install snap-stanford
pip install cvxpy==0.4.11 
```
According to a closed issue in TVGL, TVGL relies on CVXPY version 0.4. You may encounter *"error in cvxpy setup command: use_2to3 is invalid"* when you have a newer version (e.g 1.0)


### log_sum_exp
I think it is also caused by version conflict. Package import of cvxpy.atoms.log_sum_exp should be changed

In cvxpy.atoms.log_sum_exp: change scipy.misc to scipy.special for the import of logsumexp


### Other problems (not fix yet)
Code ```from XXX import *``` is not allowed in function.
```python
# TVGL.py 
# def TVGL()
    if indexOfPenalty == 1:
        print('Use l-1 penalty function')
        from inferGraphL1 import *
    elif indexOfPenalty == 2:
        print('Use l-2 penalty function')
        from inferGraphL2 import *
    elif indexOfPenalty == 3:
        print('Use laplacian penalty function')
        from inferGraphLaplacian import *
    elif indexOfPenalty == 4:
        print('Use l-inf penalty function')
        from inferGraphLinf import *
    else:
        print('Use perturbation node penalty function')
        from inferGraphPN import *
```

Now, I put ```from inferGraphL1 import *``` out of the function ```TVGL()``` and comment the above code, which means only one Penalty can be used. You can change it according to your required method in this stupid way. 

The parameter *indexOfPenalty* should still be adjusted according to the used penalty.


## Usage
TVGL can be called through the following file:
```
TVGL.py
```
**Parameters**

data : a T-by-n numpy array with the raw data (each row is a new timestamp)

lengthOfSlice : Number of samples in each ``slice'', or timestamp

lamb : the lambda regularization parameter controlling the network sparsity (as described in the paper)

beta : the beta parameter controlling the temporal consistency (as described in the paper)

indexOfPenalty : The regularization penalty to use (1 = L1, 2 = L2, 3 = Laplacian, 4 = L_inf, 5 = perturbed node)

verbose = False : Whether or not to run ADMM in ``verbose'' mode (to print intermediate steps)

eps = 3e-3 : Threshold at which we treat output network weight as zero

epsAbs = 1e-3 : ADMM absolute tolerance threshold (see full details in http://stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf)

epsRel = 1e-3 : ADMM relative tolerance threshold (see http://stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf)




## Example
Running the following script provides an example of how the TVGL solver can be used:
```
exampleTVGL.py
```
