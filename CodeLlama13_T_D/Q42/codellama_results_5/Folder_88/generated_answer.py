
def prime_factors(mylist):
    return set([p for i in range(len(mylist)) if mylist[i] % p == 0 for p in range(2, int(mylist[i]**0.5) + 1)])
