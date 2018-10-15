# import lib
import numpy as np
import random

def genComplexMatrix(num_row, num_col):
    # calculate normal distribution
    mu, sigma = 0, 1.0
    norm_dist_real = np.random.normal(mu, sigma, num_row * num_col)
    norm_dist_imag = np.random.normal(mu, sigma, num_row * num_col)
    # generate complex random array based on normal distribution
    complex_norm = (1 / np.sqrt(2)) * (norm_dist_real + 1j * norm_dist_imag)

    # reshape the complex array to a num_row-row and num_col-col array
    complex_norm.shape = (num_row, num_col)

    # get the matrix form of complex_norm array
    return np.matrix(complex_norm)

# the number of relays
N = 20

# the channel coefficient vectors from/to S1 to/from the replays
f1 = genComplexMatrix(N, 1)
# the channel coefficient vectors from/to S2 to/from the replays
f2 = genComplexMatrix(N, 1)

# the additive zero-mean noise vector at the replays
nR = 1

# the additive zero-mean noises at 2 sources
n1 = 1
n2 = 1
# the channel coefficient vectors from all replays tothe eavesdropper
l = genComplexMatrix(N, 1)
L = np.matrix(np.diag(l.flat))

# the additive zero-mean noises at the eavesdropper during the two phases
n1E = 1
n2E = 1

F1 = np.matrix(np.diag(f1.flat))
F2 = np.matrix(np.diag(f2.flat))

g1 = genComplexMatrix(N, 1)
g2 = genComplexMatrix(N, 1)

D1 = F1 * F1.H
D2 = F2 * F2.H

Z = L * np.hstack((f1, f2))

# compress data into dictionary 'data' then write to file
data = {}
data['N'] = N
data['f1'] = f1
data['f2'] = f2
data['nR'] = nR
data['n1'] = n1
data['n2'] = n2
data['L'] = L
data['n1E'] = n1E
data['n2E'] = n2E
data['F1'] = F1
data['F2'] = F2
data['g1'] = g1
data['g2'] = g2
data['D1'] = D1
data['D2'] = D2

np.savez("data/testdata10", N=N, f1=f1, f2=f2, nR=nR, n1=n1, n2=n2, L=L, n1E = n1E, n2E = n2E, F1=F1, F2=F2, g1=g1, g2=g2, D1=D1, D2=D2)