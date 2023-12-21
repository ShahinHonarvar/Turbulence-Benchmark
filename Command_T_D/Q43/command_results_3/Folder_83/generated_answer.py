def find_primes_between_indices(nums):
    primes = []
    for i in range(14, 73 + 1):
        if all(num % k != 0 for k in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
