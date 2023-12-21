def find_primes_between_indices(nums):
    primes = []
    for i in range(61, 80):
        is_prime = True
        for j in range(2, i // 2):
            if nums[j] % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
