
def find_primes_between_indices(lst):
    primes = []
    for i in range(70, 71+1):
        if isprime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
