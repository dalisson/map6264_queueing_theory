import argparse
import numpy as np
import random
'''
parser = argparse.ArgumentParser(description="queueing theory first simulation")
parser.add_argument('n_customers', type=int, help="number of customers to be simulated")
parser.add_argument('n_servers', type=int, help="number of servers on the simulation")

args = parser.parse_args()
'''

'''
setting  ia 
    arrival time = -1/4 * np.log(1 - random) for sthocastic
    arrival time = 1/4 for constant
setting x
    arrival time = -2.4 * np.log(1 - random) for sthocastic
    arrival time = 2.4 for constant

'''
poisson = lambda : -1/2.857 * np.log(1 - random.uniform(0,1))
if __name__ == '__main__':

    c = [0] * 50
    s = 10
    n = 11
    source = [0] * n
    nstop = 10000
    a = 0
    k = 0
    ab = 0
    sx = 0
    for i in range(n):
        source[i] = poisson()
    for d in range(nstop):
        ia = 0
        for i in range(n):
            ia = i if source[i] < source[ia] else ia
        a = source[ia]
        j = -1
        for i in range(s):
            if a < c[i]:
                continue
            j = i
        if j == -1:
            k = k + 1
            continue
        x =  2.4               #service time
        sx += x
        c[j] = a + x
        source[ia] = a + x + poisson()
        m = c[0]
        for i in range(s):
            m = c[i] if c[i] < m else m
        if m > a:
            ab = ab + m - a
    print("customers blocked (pi): ", k/nstop)
    print("fraction of all servers busy (Pj): ", ab/a)