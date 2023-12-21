
def prime_factors(my_list):
    return set([p for p in my_list if isprime(p)])

def isprime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False

    return True
