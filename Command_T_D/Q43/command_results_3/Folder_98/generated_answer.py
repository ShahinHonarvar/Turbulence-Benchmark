def find_primes_between_indices(nums):
    primes = []
    for i in range(1, len(nums) + 1):
        if nums[i] < 2 or nums[i] == 2 or nums[i] == 3:
            continue
        for j in range(2, int(nums[i] ** .5) + 1):
            if nums[i] % j == 0:
                break
            else:
                primes.append(nums[i])
                break
    return sorted(primes)[::-1]
