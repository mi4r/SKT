import numpy as np


def build_series1(k_):
    res = []
    for i in k_:
        ser = 3 * np.sin(2 * 0.001 * i)
        res.append(ser)
    return res


def build_series2(k_):
    res = []
    for i in k_:
        ser = 4 * np.sin(2 * 0.001 * i + np.pi / 2)
        res.append(ser)
    return res


def find_max_ind(f_):
    res = 0
    for i in range(0, 10000):
        if f_[i] >= f_[i+1]:
            res = i
            break
    return res


def func_task_sol(f1_, f2_):
    amp1 = max(np.abs(f1_))
    amp2 = max(np.abs(f2_))
    max_ind1 = find_max_ind(f1_)
    max_ind2 = find_max_ind(f2_)
    phi = (max_ind1 - max_ind2) * 10 * 2 / 10000
    k_ = phi // (2 * np.pi)
    return amp2 / amp1, phi + 2 * np.pi * k_


if __name__ == '__main__':
    k = range(0, 10000)
    f1 = build_series1(k)
    f2 = build_series2(k)
    tup = func_task_sol(f1, f2)
    print(tup)
