def find_primes_between_indices(nums):
    primes = []
    for n in range(149, 979):
        if n % 2 == 0:
            continue
        for i in range(3, int(n ** .5) + 1):
            if n % i == 0:
                break
            primes.append(n)
    return sorted(primes)
