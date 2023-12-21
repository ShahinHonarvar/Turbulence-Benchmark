
def all_left_right_truncatable_prime(nums):
    return sorted(set(nums) for n in nums if n > 9 and all(d % 10 == d for d in str(n) if d))
