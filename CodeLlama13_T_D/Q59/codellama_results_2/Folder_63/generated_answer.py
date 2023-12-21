
def all_left_truncatable_prime(nums):
    result = []
    for x in nums:
        if str(x).count('0') == 0 and is_prime(x) and all([is_prime(int(str(x)[1:i])) for i in range(len(str(x)))]):
            result.append(x)
    return sorted(result)
