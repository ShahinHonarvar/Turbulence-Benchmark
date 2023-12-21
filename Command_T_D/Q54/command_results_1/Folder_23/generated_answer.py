def all_right_truncatable_prime(nums):
    return [x for x in range(3, nums[77], 2) if is_right_truncatable_prime(str(x))]
def is_right_truncatable_prime(s):
    return all(int(s[-1]) not in x for x in range(2, int(s[0]) + 1))
