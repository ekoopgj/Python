"""
L = ['adam', 'LISA', 'barT']

def fun(st):
        st = st[0].upper() + st[1:].lower()
        return st
        

L2 = list(map(fun,L))
print(L2)
"""
from functools import reduce

L = [1,2,3,4]
def prod(x,y):
    return x*y

print(reduce(prod,L))
    
