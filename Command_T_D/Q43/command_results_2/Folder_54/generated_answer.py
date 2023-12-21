def find_primes_between_indices(nums):
    primes = []
    for i in range(13, 63):
        is_prime = all(nums[j] != i for j in range(1, int(math.ceil(math.sqrt(i)) + 1)) if i % nums[j] == 0)
        if is_prime:
            primes.append(i)
    return primes
