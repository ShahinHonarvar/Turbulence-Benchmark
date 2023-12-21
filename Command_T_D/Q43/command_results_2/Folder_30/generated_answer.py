def find_primes_between_indices(lst):
    lst = lst[:61] + lst[61:-80] + lst[-80:]
    primes = []
    for n in lst:
        if all(n % i for i in range(2, int(n ** .5) + 1)):
            primes.append(n)
    return primes
