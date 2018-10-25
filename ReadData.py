# import libs
import numpy as np


# ============================= Start reading data from files ===================================
data = np.load('data/Testdata_Exp1_4_30.npz')

N = np.int(data['N'])
f1 = np.matrix(data['f1'])
f2 = np.matrix(data['f2'])
sigmaR = np.int(data['sigmaR'])
sigma1 = np.int(data['sigma1'])
sigma2 = np.int(data['sigma2'])
L = np.matrix(data['L'])
sigma1E = np.int(data['sigma1E'])
sigma2E = np.int(data['sigma2E'])
F1 = np.matrix(data['F1'])
F2 = np.matrix(data['F2'])
g1 = np.complex128(data['g1'])
g2 = np.complex128(data['g2'])
D1 = np.matrix(data['D1'])
D2 = np.matrix(data['D2'])
Z = np.matrix(data['Z'])
Pt = np.int(data['Pt'])
# ============================= Finish reading data from files ===================================
