import numpy as np
import sys
import os


def check_and_dot(a, b):
    if len(a[len(a) - 1]) == len(b):
        return np.dot(a, b)
    else:
        print('ValueError: shapes are not corrected')
        exit(1)


def var_subst(Str_A, Str_b, Str_c, Str_d):
    old_A = np.loadtxt('A.txt')
    old_b = np.loadtxt('b.txt')
    old_c = np.loadtxt('c.txt')
    old_d = np.loadtxt('d.txt')
    M = np.loadtxt('M.txt')
    inv_M = np.linalg.inv(M)
    new_A = check_and_dot(M, old_A)
    new_A = check_and_dot(new_A, inv_M)
    new_b = check_and_dot(M, old_b)
    if len(old_c) == len(inv_M):
        new_c = np.dot(old_c, inv_M)
    else:
        print('ValueError: shapes are not corrected')
        exit(1)
    new_d = old_d
    new_d = new_d.reshape(1, 1)
    np.savetxt(Str_A, new_A)
    np.savetxt(Str_b, new_b)
    np.savetxt(Str_c, new_c)
    np.savetxt(Str_d, new_d)


if __name__ == '__main__':
    if (os.stat('A.txt').st_size == 0) | (os.stat('b.txt').st_size == 0) | (os.stat('c.txt').st_size == 0) | \
            (os.stat('d.txt').st_size == 0) | (os.stat('M.txt').st_size == 0):
        print('Error: one of the files is empty')
        exit(1)
    if len(sys.argv) > 2:
        print('Error: more than one suffix')
    elif len(sys.argv) > 1:
        str_A = 'A' + sys.argv[1] + '.txt'
        str_b = 'b' + sys.argv[1] + '.txt'
        str_c = 'c' + sys.argv[1] + '.txt'
        str_d = 'd' + sys.argv[1] + '.txt'
        var_subst(str_A, str_b, str_c, str_d)
    else:
        var_subst('A.txt', 'b.txt', 'c.txt', 'd.txt')
