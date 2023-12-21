
def find_primes_between_indices(nums):
    primes = []
    for i in range(167, 785 + 1):
        if nums[i] in primes:
            continue
        is_prime = True
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    return sorted(primes, reverse=True)
