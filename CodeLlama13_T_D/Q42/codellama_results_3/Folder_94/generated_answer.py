
def prime_factors(mylist):
    return set([x for x in mylist[93].split() if is_prime(int(x))])

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
