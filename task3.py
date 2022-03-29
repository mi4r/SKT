import matplotlib.pyplot as plt
import numpy as np
import os

""" 
1) Построить график АФЧХ для лин. об. в ПС 
2) Построить (нарисовать отдельным ярким цветом) точку (-1,0)
"""


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
    M = 10
    list_re = []
    list_im = []
    for w in np.linspace(0, M, 1000):
        iw = complex(0, w)
        W = build_transform_func(A, b, c, d, iw)
        re = W.real
        im = W.imag
        list_re.append(re)
        list_im.append(im)
    plt.plot(list_re, list_im)
    plt.scatter(-1, 0, color='r', s=40, marker='o')
    plt.text(-1, 0, '(-1,0)', color='g')
    plt.grid()
    ax = plt.gca()
    ax.axhline(y=0, color='k', alpha=0.6)
    ax.axvline(x=0, color='k', alpha=0.6)
    ax.set_xlabel('Действительная часть  U(w)')
    ax.set_ylabel('Мнимая часть  V(w)')
    ax.set_title('График АФЧХ')
    plt.show()

