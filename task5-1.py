import numpy as np
import matplotlib.pyplot as plt


def func_control(vector):
    res = []
    for t_ in vector:
        u = np.sin(t_)+2*np.sin(2*t_)+3*np.sin(3*t_)
        res.append(u)
    return res


def method_Euler(matrix_tup, x0, t0, h, u_lst, vector):
    res = []
    A_, b_, c_,  d_ = matrix_tup
    x = x0
    i = 1
    for t_ in vector:
        if t_ == t0:
            print(len(c_))
            print(len(x0))
            y = c_ @ x0 + d_ * u_lst[0]
            res.append(float(y))
        else:
            x = x + h * (A_ @ x + b_ * u_lst[i-1])
            y = c_ @ x + d_ * u_lst[i]
            res.append(float(y))
            i += 1
    return res


if __name__ == '__main__':
    A = np.loadtxt('A.txt')
    b = np.loadtxt('b.txt')
    c = np.loadtxt('c.txt')
    d = np.loadtxt('d.txt')
    tup = (A, b.reshape(-1, 1), c, d)
    x_0 = np.zeros(A.shape[0]).reshape(-1, 1)
    t_0 = 0
    step = 0.001
    n = 20
    t = np.arange(0, 20, 0.001)
    control = func_control(t)
    exit_values = method_Euler(tup, x_0, t_0, step, control, t)
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))
    axes[0].plot(t, control, label='U', c='purple')
    axes[0].grid()
    axes[0].set_title('График зависимости U(t)')
    axes[0].set_xlabel('Время t')
    axes[0].set_ylabel('Управление U')
    axes[0].legend()
    axes[1].plot(t, exit_values, label='Y', c='g')
    axes[1].grid()
    axes[1].set_title('График зависимости Y(t)')
    axes[1].set_xlabel('Время t')
    axes[1].set_ylabel('Выход Y')
    axes[1].legend()
    plt.show()
