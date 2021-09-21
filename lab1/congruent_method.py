
import math

def congruent_method_generator(a,m,x0):
    x= x0
    while True:
        x = a*x%m
        yield x


def get_x0(m):
    for i in range(m-1,1,-1):
        if math.gcd(i,m) == 1:
            return i
    return 1

m =10**10
x0=get_x0(m)
a=197

gen = congruent_method_generator(a,m,x0)
for i in range(1,100):
    print(next(gen))
