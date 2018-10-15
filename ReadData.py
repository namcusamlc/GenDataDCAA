# import libs
import numpy as np


# ============================= Start reading data from files ===================================
data = np.load('data/testdata1.npz')

N = data['N']
f1 = data['f1']
f2 = data['f2']
nR = data['nR']
n1 = data['n1']
n2 = data['n2']
L = data['L']
n1E = data['n1E']
n2R = data['n2E']
F1 = data['F1']
F2 = data['F2']
g1 = data['g1']
g2 = data['g2']
D1 = data['D1']
D2 = data['D2']

# ============================= Finish reading data from files ===================================
