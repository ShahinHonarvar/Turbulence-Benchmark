
def prime_factors(mylist):
    return set([x for x in range(2, int(math.sqrt(mylist[93]))+1) if mylist[93] % x == 0 and math.gcd(x, mylist[93]) == 1])
