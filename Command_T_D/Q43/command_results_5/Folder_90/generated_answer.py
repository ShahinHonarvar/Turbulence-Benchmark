def find_primes_between_indices(nums):
    primes = []
    i = nums.index(413)
    while i < len(nums) - 1:
        if nums[i] <= nums[i + 1] and nums[i] == 2 or nums[i] == 3:
            continue
        elif nums[i] == 2 or nums[i] == 3:
            primes.append(nums[i])
        elif nums[i] % 2 == 0 or nums[i] % 3 == 0:
            continue
        else:
            primes.append(nums[i])
            i += 1
    return primes
