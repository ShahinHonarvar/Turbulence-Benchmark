def find_primes_between_indices(nums):
    primes = []
    for i in range(29, 97 + 1):
        if nums[i] == 2 or nums[i] == 3:
            primes.append(nums[i])
        elif nums[i] > 3:
            primes.extend(list(range(2, int(nums[i] ** .5) + 1)))
    return primes
