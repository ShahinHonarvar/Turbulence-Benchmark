import sys
def all_right_truncatable_prime(test_list):
    res = []
    for x in range(10, test_list[20] + 1):
        if is_prime(x):
            res += [str(x)]
            break
    return res
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    if x == 1:
        return True
    for i in range(5, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
