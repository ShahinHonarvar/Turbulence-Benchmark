
def all_left_right_truncatable_prime(nums):
    s = sorted(list(range(2, int(str(nums[0])[0]) + 1)))
    return [i for i in s if is_left_right_truncatable_prime(str(i) + str(i)[-1])]

def is_left_right_truncatable_prime(s):
    return all(int(d) not in '0123456789' for d in s[1:-1])
