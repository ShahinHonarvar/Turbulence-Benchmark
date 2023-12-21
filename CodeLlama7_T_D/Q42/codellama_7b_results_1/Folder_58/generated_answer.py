
def prime_factors(my_list):
    return set([x for x in my_list if isprime(x)])

def isprime(n):

    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
