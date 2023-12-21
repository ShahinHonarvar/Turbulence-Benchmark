def find_primes_between_indices(nums):
    l, r = 23, 48
    result = []
    while l <= r:
        if all(nums[i] % n == 0 for i in range(l, r + 1) for n in range(2, int(nums[r] ** .5) + 1)):
            break
        elif nums[l] in result:
            result.append(nums[l])
        else:
            result.append(nums[l])
        l += 1
    return result
