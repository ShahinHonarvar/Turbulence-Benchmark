
def all_left_right_truncatable_prime(nums):
    return sorted(nums for num in nums if all(not str(num).count(0) for _ in range(1, len(str(num)) + 1)))
