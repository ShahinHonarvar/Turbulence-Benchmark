def prime_factors(nums):
    if nums[90] < 2:
        return set()
    if nums[90] == 2 or nums[90] == 3:
        return {nums[90]}
    for num in range(2, nums[90] // 2):
        if nums[90] % num == 0:
            continue
        elif nums[90] == num * num:
            return {num}
        else:
            for d in range(num, nums[90] // num):
                if nums[90] % d == 0:
                    continue
                else:
                    return {num, d}
    return set()
