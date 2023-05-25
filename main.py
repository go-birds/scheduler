# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def cost_matrix(file):

    return np.loadtxt(file, delimiter=',')

def build_Ab(n, m, s, k1, k2):

    A1 = np.zeros([n, n * m])
    A2 = np.zeros([m, n * m])
    A3 = np.zeros([m, n * m])
    A1n = A1

    for i in range(n):
        A1[i, i * m: (i + 1) * m] = 1
        A1n = A1 * -1
        b1 = np.ones([len(A1), 1])
        b1n = b1 * -1

    for j in range(m):
        A2[j, range(0 + j, n * m + j, m)] = 1
        b2 = np.ones([len(A2), 1]) * s

        # these should be handled more robustly
        A3[j, k1 * m + j] = 1
        A3[j, k2 * m + j] = 1
        b3 = np.ones([len(A3), 1])

    A = np.vstack([A1, A2, A3, A1n])
    b = np.vstack([b1, b2, b3, b1n])
    return A, b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    from scipy.optimize import linprog
    import numpy as np
    import sys
    np.set_printoptions(threshold=sys.maxsize)

    C0 = cost_matrix('upper_school_afternoon_C.csv')
    n = C0.shape[0]
    m = C0.shape[1]
    C = np.reshape(C0, (1, n*m))

    # set up A

    # custom constraint - kids 5 and 6 can't be in the same class
    k1 = 5
    k2 = 6

    # max class size
    s = 13

    A, b = build_Ab(n, m, s, k1 ,k2)

    res = linprog(C, A_ub=A, b_ub=b, bounds=(0,1))
    out = np.ndarray.round(np.reshape(res.x, (n,m)), 0)

    np.savetxt("solution2.csv", out)
    print(out)
