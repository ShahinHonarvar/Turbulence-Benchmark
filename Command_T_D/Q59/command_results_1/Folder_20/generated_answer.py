def all_left_truncatable_prime(nums):
    # Add your code here.
    return sorted(set(nums) for i in range(100, len(str(max(nums)))))
