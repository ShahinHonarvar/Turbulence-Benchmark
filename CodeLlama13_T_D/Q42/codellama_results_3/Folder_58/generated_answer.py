
def prime_factors(mylist):
    return set([x for x in range(2, mylist[714]) if all(mylist[714] % y != 0 for y in range(2, int(mylist[714] ** .5) + 1))])
