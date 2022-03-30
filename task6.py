import numpy as np
import matplotlib.pyplot as plt


def build_test_signals(w_lst_):
    res = [[None for i in range(20000)] for j_ in range(len(w_lst_))]
    for i_ in range(len(w_lst_)):
        j_ = 0
        for t_ in np.arange(0, 20, 0.001):
            res[i_][j_] = np.sin(w_lst_[i_]*t_)
            j_ += 1
    return res


def method_Euler(matrix_tup, x0, t0, h, u_lst, vector, N_):
    res = [[None for i in range(20000)] for j_ in range(N_)]
    A_, b_, c_ = matrix_tup
    x = x0
    for i_ in range(N_):
        j_ = 0
        for t_ in vector:
            if t_ == t0:
                y = c_ @ x0
                res[i_][j_] = float(y)
                j_ += 1
            else:
                x = x + h * (A_ @ x + b_ * u_lst[i_][j_-1])
                y = c_ @ x
                res[i_][j_] = float(y)
                j_ += 1
    return res


def find_max_ind(f_):
    res = 0
    for i in range(0, 10000):
        if f_[i] >= f_[i+1]:
            res = i
            break
    return res


def build_C(y, N_):
    res = []
    for i_ in range(N_):
        ampl = max(np.abs(y[i_]))
        phi = find_max_ind(y[i_])
        C_i = ampl * np.e ** complex(0, phi)
        res.append(C_i)
    return res


if __name__ == '__main__':
    num = np.loadtxt('num.txt')
    denum = np.loadtxt('denum.txt')
    N = len(denum)
    w_lst = np.array(range(N))*2+1
    control = build_test_signals(w_lst)
    A = np.zeros((N, N))
    for j in range(N-1):
        A[j][j+1] = 1
        A[N-1][j] = - denum[::-1][j]
    A[N-1][N-1] = - denum[0]
    b = np.zeros(N).reshape(-1, 1)
    b[N-1] = 1
    c = num[::-1]
    tup = (A, b, c)
    x_0 = np.zeros(A.shape[0]).reshape(-1, 1)
    t_0 = 100
    step = 0.001
    t = np.arange(0, 20, 0.001)
    exit_values = method_Euler(tup, x_0, t_0, step, control, t, N)
    C_lst = build_C(exit_values, N)
    print(C_lst)
    fig, axes = plt.subplots(4, 1, figsize=(10, 10))
    axes[0].plot(t, exit_values[0])
    axes[1].plot(t, exit_values[1])
    axes[2].plot(t, exit_values[2])
    axes[3].plot(t, exit_values[3])
    axes[0].grid()
    axes[1].grid()
    axes[2].grid()
    axes[3].grid()
    plt.show()
