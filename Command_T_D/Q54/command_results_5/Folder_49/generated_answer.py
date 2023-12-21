def all_right_truncatable_prime(nums):
    return sorted(set(str(nums[14]) for num in nums if num < 10**9 and num % 2 == 1 and num % 5 == 0))
