def find_primes_between_indices(nums):
    primes = []
    for i in range(87, 89 + 1):
        if all(num % j != 0 for j in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
