
def all_left_right_truncatable_prime(nums):
    return sorted(nums for num in nums if all(str(num).count(d) == 1 for d in "2357"))
