def find_primes_between_indices(nums):
    result = []
    for i in range(66, 79):
        is_prime = True
        for j in range(2, i // 2):
            if nums[j] == 0:
                continue
            elif nums[i] == 0:
                break
            elif nums[j] == nums[i]:
                is_prime = False
                break
        if is_prime:
            result.append(nums[i])
    return result
