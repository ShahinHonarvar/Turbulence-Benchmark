def all_right_truncatable_prime(nums):
    return sorted(filter(lambda x: all(str(x)[-1] not in str(y) for y in range(2, int(str(x)[-1]) + 1)), nums), reverse=True)
