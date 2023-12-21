def find_primes_between_indices(nums):
    primes = []
    for i in range(33, 36):
        if all(num % i != 0 for num in nums):
            primes.append(i)
    return sorted(primes)
