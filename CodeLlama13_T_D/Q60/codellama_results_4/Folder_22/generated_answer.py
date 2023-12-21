
def all_left_right_truncatable_prime(nums):
    left_trunc = []
    right_trunc = []
    for num in nums:
        if str(num)[1:-1]:
            continue
        if is_prime(num) and is_prime(num[:-1]) and is_prime(num[1:]):
            left_trunc.append(num)
            right_trunc.append(num)
    return sorted(left_trunc + right_trunc)
