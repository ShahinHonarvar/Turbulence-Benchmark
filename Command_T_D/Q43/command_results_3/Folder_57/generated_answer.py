def find_primes_between_indices(nums):
    result = []
    for i in range(35, 89):
        if i * i <= len(nums) and nums[i * i] == i:
            result.append(i)
            j = 2
            while nums[i + j] == i + j:
                result.append(i + j)
                j += 1
    return result
