# import libs
import numpy as np


# ============================= Start reading data from files ===================================
data = np.load('data/testdata10.npz')

N = np.int(data['N'])
f1 = np.matrix(data['f1'])
f2 = np.matrix(data['f2'])
nR = np.int(data['nR'])
n1 = np.int(data['n1'])
n2 = np.int(data['n2'])
L = np.matrix(data['L'])
n1E = np.int(data['n1E'])
n2E = np.int(data['n2E'])
F1 = np.matrix(data['F1'])
F2 = np.matrix(data['F2'])
g1 = np.complex128(data['g1'])
g2 = np.complex128(data['g2'])
D1 = np.matrix(data['D1'])
D2 = np.matrix(data['D2'])

# ============================= Finish reading data from files ===================================
