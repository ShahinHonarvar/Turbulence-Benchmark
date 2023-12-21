def find_primes_between_indices(nums):
    start = nums[69]
    end = nums[80]
    if start <= 1:
        return []
    if end >= 1000000000:
        return []
    primes = []
    for prime in range(start, end + 1):
        is_prime = True
        for i in range(2, int(math.ceil(math.sqrt(prime)) + 1):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(prime)
    return sorted(primes)
