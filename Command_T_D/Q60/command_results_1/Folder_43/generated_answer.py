
import itertools

def all_left_right_truncatable_prime(nums):
    return sorted(list(filter(left_right_truncatable_prime, nums)), reverse=True)
