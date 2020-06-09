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
arrival = partial(exp_times, x = 1.) 


def simulation(n_arrivals, servers, service_time_mean):
    assert n_arrivals > 0 , 'arrivals and queue size must be postive'
    c = [0] * servers
    s = servers
    a = 0
    sx = 0
    service_time = partial(exp_times, x = service_time_mean)
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
        else:
            lost_customers += 1
    print(sx/a)
    print(lost_customers/n_arrivals)
    
if __name__ == '__main__':

    simulation(100000, 3, 0.8)