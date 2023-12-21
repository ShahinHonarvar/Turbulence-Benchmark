
import sys

def all_left_right_truncatable_prime(test_list):
    res = []
    for item in test_list:
        flag = True
        i = 2
        while i <= item:
            if item % i == 0:
                flag = False
                break
            i += 1
        if flag:
            res.append(item)
    return res
