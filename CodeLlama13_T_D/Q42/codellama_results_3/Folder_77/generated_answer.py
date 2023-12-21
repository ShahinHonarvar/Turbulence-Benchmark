
def prime_factors(mylist):
    return set([int(i) for i in str(mylist[985]) if int(i) > 1 and all([int(i) % j == 0 for j in range(2, int(sqrt(int(i))))])])
