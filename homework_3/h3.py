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

def exp_times(x):
    return -x * np.log(1 - random.uniform(0,1))

#for arrival simulate with either 1/4.2 and 1/4
arrival = partial(exp_times, x = 1./4) 
service_time = partial(exp_times, x = 2.4) 

if __name__ == '__main__':
    c = [0] * 10
    s = 1
    a = 0
    sx = 0
    d = 100000
    w = [0] * d
    for index in range(d):
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
            w[index]= (c[j] - a)
            c[j] = c[j] + x
            
    
    w = np.array(w) 
    print('carried load ', sx/a) #dividir pelo numero de servidores para calcula utilizacao
    print('utilizacao ', (sx/a)/s)
    print('E(W)', w.mean())
    
    for i in range(9):
        print('E(W>%s)' % i, (w > i).mean())
        
