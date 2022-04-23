import numpy as np
from tbcontrol.symbolic import routh
import sympy as sp


s = sp.Symbol('s')


def check_definition(poly_):
    roots = poly_.roots()
    for item in roots:
        if item.real >= 0:
            return False
    return True


def check_Hurwitz(poly_):
    mtr = np.diag(list(poly_)[poly_.degree()-1::-1])
    tmp = list(poly_)[::-1]
    shift = 0
    for i in range(len(mtr)):
        if i % 2 == 0:
            k = 1
        else:
            k = 0
        for j in range(len(mtr)):
            if k < len(tmp):
                mtr[i][j+shift] = tmp[k]
            k += 2
        if i % 2 != 0:
            shift += 1
    if tmp[0] <= 0:
        return False
    for i in range(len(mtr)):
        tmp_mtr = mtr[0:1+i, 0:1+i]
        if np.linalg.det(tmp_mtr) <= 0:
            return False
    return True


def check_Routh(poly_):
    p = sp.Poly(poly_, s)
    res = routh(p)
    res = np.array(res)
    tmp = list(poly_)[::-1]
    if tmp[0] <= 0:
        return False
    for i in range(len(res)):
        if res[i][0] <= 0:
            return False
    return True


if __name__ == '__main__':
    poly = np.loadtxt('poly.txt')
    poly = poly[::-1]
    poly = np.polynomial.Polynomial(poly)
    print(poly)
    print(check_definition(poly))
    print(check_Hurwitz(poly))
    print(check_Routh(poly))
