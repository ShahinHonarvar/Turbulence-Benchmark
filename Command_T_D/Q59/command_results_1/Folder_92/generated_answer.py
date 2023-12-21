def all_left_truncatable_prime(nums):
    x = nums[7]
    return sorted(nums[:7] + [n for n in range(2, x // 2) if all(n % i for i in range(2, int(str(n))[0] + 1))])
