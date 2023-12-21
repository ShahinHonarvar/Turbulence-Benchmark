def find_primes_between_indices(nums):
    primes = []
    for i in range(15, 48 + 1):
        if all(num % i for num in nums if num > i):
            primes.append(i)
    return sorted(set(primes))
