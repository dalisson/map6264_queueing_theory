import argparse
import numpy as np
import random
from functools import partial


def exp_times(x):
    return -x * np.log(1 - random.uniform(0,1))

#adjusts a_hat to keep a_star = pre defined intended offered load

def a_hat_calc(a_star, n):
        t = a_star/n
        return t/(1-t)


def simulation(n):
    c = [0] * 50
    n = n
    s = 10
    source = [0] * n
    a = 0
    sx = 0
    d = 100000
    lost_client = 0
    all_servers_busy_time = 0


    a_star = 9.6 #the intended offered load will be kept at 9.6 erlangs
    #calculate a_hat according to a_star
    a_hat = a_hat_calc(a_star, n)
    #gamma has to be set up for every n
    tal = 1 
    gamma = a_hat/tal
    arrival = partial(exp_times, x = 1/gamma) 
    service_time = partial(exp_times, x = tal) 
    for i in range(n):
        source[i] = arrival()

    for _ in range(d):
        ia = 0
        for i in range(n):
            ia = i if source[i] < source[ia] else ia
        a = source[ia]
        x = service_time()
        j = 0
        for i in range(s):
            j = i if c[i] < c[j] else j
        if c[j] < a:
            c[j] = (a + x)
            source[ia] = c[j] + arrival()
            sx += x
            
            j = 0
            for i in range(s):
                j = i if c[i] < c[j] else j
            if c[j] > a:
                all_servers_busy_time += c[j] - a
        else:
            lost_client += 1
            source[ia] += arrival()
        
    print('P[{}] - {:.3f} '.format(n, all_servers_busy_time/a))
    print('PI[{}] - {:.3f}'.format(n, lost_client/d))
    print('utilization {:.3f}'.format(sx/a/s))
    print('----------------------')

if __name__ == '__main__':
   simulation(11)
   # for n in [10, 11, 12, 13, 14, 15, 25, 50, 100, 1000]:
   #     simulation(n)
