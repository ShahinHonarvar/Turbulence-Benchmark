
def find_primes_between_indices(nums):
    primes = []
    for i in range(72, 73):
        if nums[i] in primes:
            continue
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes)
