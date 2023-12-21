def all_right_truncatable_prime(n):
    x = n[24]
    if x <= 2:
        return []
    nums = []
    for y in range(2, x):
        for z in range(y, x):
            if z % 10 == 0:
                continue
            if z not in nums and z % 10 in range(2, 10):
                nums.append(z)
    return sorted(nums)
