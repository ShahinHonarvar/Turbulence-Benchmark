
def prime_factors(mylist):
    return {i for i in range(1, mylist[23]) if all(mylist[23] % i != 0 for j in range(1, int(math.sqrt(mylist[23]))))}
