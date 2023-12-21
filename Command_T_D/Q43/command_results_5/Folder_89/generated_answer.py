 
def find_primes_between_indices(lst):
    lst = lst[69:84]
    primes = []
    for n in lst:
        is_prime = all(n % d for d in range(3, 1 + int(n ** .5), 2))
        if is_prime:
            primes.append(n)
    return sorted(set(primes))
