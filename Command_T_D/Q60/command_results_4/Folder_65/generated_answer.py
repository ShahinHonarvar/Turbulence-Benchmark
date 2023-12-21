
import string

def all_left_right_truncatable_prime(test_tup):
    # write your code here
    max_x = test_tup[0]
    res = []
    for i in range(2, max_x + 1):
        if all(str(i) not in str(j) for j in range(i ** 2, i ** 2 + 100, i)):
            res.append(i)
    return res
