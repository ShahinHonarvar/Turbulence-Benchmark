def find_primes_between_indices(nums):
    primes = []
    for i in range(424, 552 + 1):
        if all(num % j != 0 for j in range(2, int(num ** .5) + 1)):
            primes.append(num)
    return sorted(set(primes))
