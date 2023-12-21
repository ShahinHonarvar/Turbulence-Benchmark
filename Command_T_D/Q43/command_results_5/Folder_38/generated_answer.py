def find_primes_between_indices(nums):
    primes = []
    for i in range(55, 87+1):
        if all(num % i for num in nums):
            primes.append(i)
    return sorted(set(primes))
