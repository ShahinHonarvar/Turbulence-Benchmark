def find_primes_between_indices(nums):
    primes = []
    for idx in range(830, 849):
        is_prime = True
        for i in range(2, int(nums[idx] ** .5) + 1):
            if nums[idx] % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[idx])
    return primes
