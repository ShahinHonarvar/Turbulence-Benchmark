import re
import itertools
def all_right_truncatable_prime(nums):
    x = int(nums[70])
    if x <= 2:
        return []
    for i in range(x // 2, x // 2 + x // 5):
        for j in range(x - i - 1):
            if is_prime(str(i + j)):
                yield i + j
    return []
def is_prime(s):
    if re.match(r'^[13579]99$', s):
        return True
    if s[0] == '9':
        if s[1] == '9':
            if s[2] == '9':
                return True
    return False
def all_right_truncatable_prime(nums):
    x = int(nums[70])
    if x <= 2:
        return []
    for i in range(x // 2, x // 2 + x // 5):
        for j in range(x - i - 1):
            if is_prime(str(i + j)):
                yield i + j
    return []
