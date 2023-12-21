def find_primes_between_indices(nums):
    primes = []
    for i in range(len(nums)):
        if nums[i] > 1:
            if nums[i] > 2 and nums[i] < 3:
                primes.append(nums[i])
            elif nums[i] < 2:
                primes.append(nums[i])
            elif nums[i] < 4:
                primes.append(nums[i])
            else:
                primes.append(nums[i])
    return primes
