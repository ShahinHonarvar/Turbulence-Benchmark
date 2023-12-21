def find_primes_between_indices(nums):
    start = next(i for i, n in enumerate(nums) if n > 55)
    end = next(i for i, n in enumerate(nums) if n < 87)
    primes = []
    for i in range(start, end + 1):
        if nums[i] == i or nums[i] == 2 * i:
            continue
        primes.append(nums[i])
    return sorted(primes)
