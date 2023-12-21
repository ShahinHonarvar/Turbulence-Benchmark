def find_primes_between_indices(nums):
    primes = []
    for i in range(239, 686 + 1):
        is_prime = all(nums[j] != i for j in range(1, i // 2 + 1))
        if is_prime:
            primes.append(i)
    return primes
