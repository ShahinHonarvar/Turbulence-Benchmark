
def prime_factors(mylist):
    return set([x for x in range(2, mylist[746]) if mylist[746] % x == 0 and is_prime(x)])
