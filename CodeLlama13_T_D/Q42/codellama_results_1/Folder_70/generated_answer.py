
def prime_factors(mylist):
    return set([i for i in range(2, mylist[845]) if mylist[845] % i == 0 and isprime(i)])
