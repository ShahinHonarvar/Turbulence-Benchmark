def find_primes_between_indices(nums):
    if not nums:
        return []
    res = []
    max_num = nums[-1]
    if max_num <= 112:
        return []
    for i in range(112, max_num // 2):
        if nums[i] % i == 0:
            continue
        for j in range(2, int(nums[i] ** .5) + 1):
            if nums[i] % j == 0:
                break
            res += [i, j]
    if max_num % 2 == 0:
        res += [max_num]
    return res[::-1]
