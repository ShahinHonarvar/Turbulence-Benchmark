
def find_primes_between_indices(nums):
    primes = []
    for i in range(56, 58):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
