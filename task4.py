import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
import os


def check_and_dot(a, b):
    if len(a) == len(b):
        return np.dot(a, b)
    else:
        print('ValueError: shapes are not corrected')
        exit(1)


def build_transform_func(A, b, c, d, iw):
    I = np.eye(len(A), len(A[0]), dtype=int)
    iwI = np.dot(iw, I)
    tmp = np.linalg.inv(iwI - A)
    tmp = check_and_dot(c, tmp)
    tmp = check_and_dot(tmp, b)
    W = tmp + d
    return W


if __name__ == '__main__':
    if (os.stat('A.txt').st_size == 0) | (os.stat('b.txt').st_size == 0) | (os.stat('c.txt').st_size == 0) | \
            (os.stat('d.txt').st_size == 0):
        print('Error: one of the files is empty')
        exit(1)
    A = np.loadtxt('A.txt')
    b = np.loadtxt('b.txt')
    c = np.loadtxt('c.txt')
    d = np.loadtxt('d.txt')
    print(c)
    M = 10
    list_L = []
    list_phi = []
    for w in np.linspace(0, M, 1000):
        iw = complex(0, w)
        W = build_transform_func(A, b, c, d, iw)
        Abs = abs(W)
        L = 20 * math.log(Abs, 10)
        list_L.append(L)
        phi = cmath.phase(W)
        list_phi.append(phi)
    plt.suptitle('Bode Diagram')
    plt.subplot(2, 1, 1)
    plt.plot(list_L)
    plt.grid()
    plt.xscale('log')
    plt.ylabel('Magnitude [dB]')
    plt.subplot(2, 1, 2)
    plt.plot(list_phi)
    plt.grid()
    plt.xscale('log')
    plt.ylabel('Phase [deg]')
    plt.show()



