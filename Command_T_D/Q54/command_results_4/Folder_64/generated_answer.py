def all_right_truncatable_prime(nums):
    return [x for x in range(2, nums[4] + 1) if all(str(x) in str(y) for y in range(2, int(str(x)[-1]) + 1) if all(str(x) in str(z) for z in range(2, int(str(x)[-1]) + 1) if all(str(x) in str(w) for w in range(2, int(str(x)[-1]) + 1) if x % w == 0)))]
