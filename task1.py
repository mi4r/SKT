import sys


def build_polynomial(lst, m):
    pol = ''
    for i in range(0, len(lst)):
        if (lst[i] != '1') | (m == 1):
            pol = pol + str(float(lst[i]))
        if m > 1:
            pol = pol + 's'
            if m == 2:
                pol += '+'
        if m > 2:
            pol = pol + '^' + str(m - 1) + '+'
        m = m - 1
    return pol


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Error: not suitable parameters for the transfer function')
    else:
        list1 = sys.argv[1].split(',')
        list2 = sys.argv[2].split(',')
        n = len(list1)
        k = len(list2)
        maximum = max(len(sys.argv[1]), len(sys.argv[2]))
        if n > k:
            str1 = '     '
            str2 = ' ' * maximum
        elif n < k:
            str1 = ' ' * maximum
            str2 = '     '
        else:
            if maximum == 1:
                str1 = ' '
                str2 = ' '
            else:
                str1 = '     '
                str2 = '     '
        str1 += build_polynomial(list1, n)
        print(str1)
        if maximum == 1:
            print('-----')
        else:
            print('----' * maximum)
        str2 += build_polynomial(list2, k)
        print(str2)
