def all_right_truncatable_prime(nums):
    x = nums[14]
    return sorted([n for n in range(2, x) if all(n % d == 0 or n % d == d for d in range(3, int(str(n)[-1])))])
