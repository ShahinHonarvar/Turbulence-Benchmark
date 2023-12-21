def all_right_truncatable_prime(nums):
    return [x for x in range(2, nums[0] + 1) if all(x % y == 0 or x % y == y for y in range(3, int(str(x)[-1]) + 1, 2))]
