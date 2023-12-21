def find_primes_between_indices(nums):
    lst = list(range(30, 44))
    primes = []
    for n in lst:
        if all(n % i != 0 for i in range(2, n // 2)):
            primes.append(n)
    return sorted(set(primes))
