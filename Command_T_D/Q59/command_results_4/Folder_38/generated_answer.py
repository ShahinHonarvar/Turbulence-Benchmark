def all_left_truncatable_prime(nums):
    return sorted(nums for n in range(1, int(nums[28]) + 1) if all(str(n).count(d) == 1 for d in str(n) if d not in "0"))
