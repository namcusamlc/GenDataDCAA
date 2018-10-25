# import lib
import numpy as np
import random

def genTest(N, Pt):
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

    # the channel coefficient vectors from/to S1 to/from the replays
    f1 = genComplexMatrix(N, 1)
    # the channel coefficient vectors from/to S2 to/from the replays
    f2 = genComplexMatrix(N, 1)

    # the covariance at the replays
    sigmaR = 1

    # the covariances at 2 sources
    sigma1 = 1
    sigma2 = 1
    # the channel coefficient vectors from all replays tothe eavesdropper
    l = genComplexMatrix(N, 1)
    L = np.matrix(np.diag(l.flat))

    # the covariances at the eavesdropper during the two phases
    sigma1E = 1
    sigma2E = 1

    F1 = np.matrix(np.diag(f1.flat))
    F2 = np.matrix(np.diag(f2.flat))

    g1 = genComplexMatrix(1, 1)
    g1 = g1.flat[0]
    g2 = genComplexMatrix(1, 1)
    g2 = g2.flat[0]

    D1 = F1 * F1.H
    D2 = F2 * F2.H

    Z = L * np.hstack((f1, f2))

    # compress data into dictionary 'data' then write to file
    data = {}
    data['N'] = N
    data['f1'] = f1
    data['f2'] = f2
    data['sigmaR'] = sigmaR
    data['sigma1'] = sigma1
    data['sigma2'] = sigma2
    data['L'] = L
    data['sigma1E'] = sigma1E
    data['sigma2E'] = sigma2E
    data['F1'] = F1
    data['F2'] = F2
    data['g1'] = g1
    data['g2'] = g2
    data['D1'] = D1
    data['D2'] = D2
    data['Z'] = Z
    data['Pt'] = Pt


    np.savez("data/Testdata_Exp1_" + str(N) + "_" + str(Pt), N=N,
                                                             f1=f1,
                                                             f2=f2,
                                                             sigmaR=sigmaR,
                                                             sigma1=sigma1,
                                                             sigma2=sigma2,
                                                             L=L,
                                                             sigma1E = sigma1E,
                                                             sigma2E = sigma2E,
                                                             F1=F1,
                                                             F2=F2,
                                                             g1=g1,
                                                             g2=g2,
                                                             D1=D1,
                                                             D2=D2,
                                                             Z=Z,
                                                             Pt=Pt)

for N in range(4, 9, 2):
    for Pt in range(30, 41, 1):
        genTest(N, Pt)
