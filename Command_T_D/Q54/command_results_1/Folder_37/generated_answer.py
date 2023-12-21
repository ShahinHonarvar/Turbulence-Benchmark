import re
def all_right_truncatable_prime(test_tup):
    x = test_tup[35]
    res = []
    for y in range(2, x//2 + 1):
        if re.match(r'^[2-9][0-9]0$', str(y)):
            res.append(y)
            break
    return res
