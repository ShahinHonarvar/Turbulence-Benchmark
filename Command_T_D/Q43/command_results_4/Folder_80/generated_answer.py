def find_primes_between_indices(nums):
    l, r = 13, 29
    primes = []
    for i in range(l, r + 1):
        if nums[i] > 1:
            primes.append(nums[i])
            if len(primes) > 1:
                break
    return sorted(primes)[::-1] if primes else []
