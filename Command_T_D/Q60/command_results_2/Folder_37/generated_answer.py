
def all_left_right_truncatable_prime(nums):
    res = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res

def is_left_right_truncatable_prime(num):
    x = num
    while x > 1:
        if x % 10 == 0:
            return False
        x //= 10
    return True
