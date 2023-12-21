
def all_left_right_truncatable_prime(test_list):
    res = []
    for item in test_list:
        if is_left_right_truncatable_prime(item):
            res.append(item)
    return res

def is_left_right_truncatable_prime(test_int):
    max_quotient = 1
    for i in range(2, test_int // 2 + 1):
        if test_int % i == 0:
            max_quotient = i
            break
    if test_int == 1 or test_int == max_quotient:
        return True
    for i in range(2, test_int // 2 + 1):
        if test_int % i == 0:
            return False
    return True
