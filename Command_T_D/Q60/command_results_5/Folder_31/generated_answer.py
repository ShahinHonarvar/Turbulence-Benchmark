
def all_left_right_truncatable_prime(nums):
    res = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res

def is_left_right_truncatable_prime(num):
    return num > 1 and all(str(num)[0] != '0' for i in range(1, len(str(num)) + 1))
