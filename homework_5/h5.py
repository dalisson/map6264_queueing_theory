import argparse
import numpy as np
import random
from functools import partial

'''
setting  ia 
    arrival time = -1/4 * np.log(1 - random) for sthocastic
    arrival time = 1/4 for constant
setting x
    x = -2.4 * np.log(1 - random) for sthocastic
    x = 2.4 for constant
'''

__all__ = ['simulation']

def exp_times(x):
    return -x * np.log(1 - random.uniform(0,1))

#for arrival simulate with either 1/4.2 and 1/4
arrival = partial(exp_times, x = 1/0.8) 


def simulation(n_arrivals, mu, k, s):
   
    c = [0] * s
    a = 0
    sx = 0
    w = [0] * n_arrivals
    queue = [0] * k
    service_time = partial(exp_times, x = mu)
    lost_customers = 0
    for index in range(n_arrivals):
        ia =  arrival() #inter arrival time
        a = a + ia
        x = service_time() #service time
        sx = sx + x
        j = 0
        #server with least time
        for i in range(s):
            j = i if c[i] < c[j] else j
        if c[j] <= a:
            c[j] = a + x
        elif k == 0:
            lost_customers += 1
            sx -= x
        else:
            q = 0
            for i in range(k):
                q = i if queue[i] < queue[q] else q
            if queue[q] < a:
                queue[q] = c[j]
                w[index] = (c[j] - a) # divide by 2.4 to calculate fractions of service time waited
                c[j] += x
            else:
                lost_customers += 1
                sx -= x
                
          
     
    w = np.array(w)
    
    print('-----------')
    print('utilization ', (sx/a)/s)
    print('E(W)', w.mean())
    print('Fraction of lost customers', float(lost_customers)/n_arrivals)
    print('-----------')
    #for i in range(9):
    #    print('E(W>%s)' % i, (w > i).mean())

if __name__ == '__main__':
    simulation(100000, 1, 1, 1)