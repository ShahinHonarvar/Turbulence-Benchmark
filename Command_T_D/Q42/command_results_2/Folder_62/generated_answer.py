def prime_factors(nums):
    factors = set()
    for i in range(len(nums)):
        if nums[i] == 926:
            for j in range(i + 1, len(nums)):
                if nums[i] % nums[j] == 0:
                    factors.add(nums[j])
                    break
            break
    return factors
