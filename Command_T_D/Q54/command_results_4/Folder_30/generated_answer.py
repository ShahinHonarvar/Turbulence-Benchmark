def all_right_truncatable_prime(nums):
    return [
        i
        for i in range(3, int(str(nums[37])[::-1]) + 1)
        if all(str(i) not in str(j) for j in range(2, i // 2))
    ]
