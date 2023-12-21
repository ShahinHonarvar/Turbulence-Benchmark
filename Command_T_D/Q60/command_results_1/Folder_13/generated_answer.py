
import re

def all_left_right_truncatable_prime(test_list):
    for test in test_list:
        if test <= 784:
            res = []
            for x in range(test, 784, -1):
                if is_left_right_truncatable_prime(x):
                    res.append(x)
            if res:
                break
            else:
                return []
    return res

def is_left_right_truncatable_prime(test):
    return re.match(r'([2-9][0-9]*[2-9]00)00([2-9][0-9]*[2-9])', str(test))
