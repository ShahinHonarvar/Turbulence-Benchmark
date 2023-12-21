
def all_left_right_truncatable_prime(nums):
    return [str(p) for p in nums if is_left_right_truncatable_prime(str(p))]

def is_left_right_truncatable_prime(num):
    return all(d == '9' for d in str(num) if d != '0') and all(str(p) == '1' or str(p) == '2' for p in range(2, int(num) + 1))
