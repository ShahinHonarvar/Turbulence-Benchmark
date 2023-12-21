def find_primes_between_indices(nums):
    primes = []
    for i in range(6, 7):
        is_prime = True
        for j in range(2, i // 2):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    return primes
