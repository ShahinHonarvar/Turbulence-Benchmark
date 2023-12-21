
def all_left_right_truncatable_prime(nums):
    return sorted(nums for n in range(2, nums[0]) if all(n % d != 0 for d in range(2, int(n ** .5) + 1) if n % d != 0))
