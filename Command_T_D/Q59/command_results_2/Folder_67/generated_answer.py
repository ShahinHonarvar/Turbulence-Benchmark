def all_left_truncatable_prime(nums):
    l = [int(str(x)[-1]) for x in nums if all(str(x)[-1] not in str(x) for x in range(2, int(str(x)[-1]))) and str(x)[-1] not in str(x)]
    return sorted(set(l))
