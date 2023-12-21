
def all_left_right_truncatable_prime(test_tup):
    res = []
    for num in range(test_tup[0], test_tup[1] + 1):
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res

def is_left_right_truncatable_prime(test_num):
    for d in range(10, test_num // 10):
        if test_num % d == 0:
            return False
    return True
