def find_primes_between_indices(nums):
    primes = []
    for n in range(478, 949):
        if all(n % i != 0 for i in range(2, int(n ** .5) + 1)):
            primes.append(n)
    return sorted(primes)[::-1]
