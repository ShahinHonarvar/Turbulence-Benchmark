
import itertools
import re

def all_left_right_truncatable_prime(test_list):
    res = []
    for (left, right) in itertools.permutations(test_list):
        if is_left_right_truncatable_prime(left, right):
            res.append(left)
            res.append(right)
    return res

def is_left_right_truncatable_prime(left, right):
    zero_cnt = sum(map(str.count, ('0', '2', '4', '6', '8')))
    if zero_cnt > 1:
        return False
    for i in range(len(left)):
        if left[i] == '0':
            return False
    for j in range(len(right)-1, -1, -1):
        if right[j] == '0':
            return False
    return True
