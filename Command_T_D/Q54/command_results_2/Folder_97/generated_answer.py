import itertools
def all_right_truncatable_prime(test_list):
    res = list(filter(lambda x: is_right_truncatable_prime(x), test_list))
    return res
def is_right_truncatable_prime(x):
    if x < 2:
        return False
    if x < 3:
        return True
    x = str(x)
    i = len(x) - 1
    while i > 0:
        if x[i] == '9':
            break
        elif x[i] == '0' and x[i-1] != '5':
            return False
        elif x[i] == '0' and x[i-1] == '5':
            return True
        elif x[i] != '0' and x[i-1] == '0':
            return False
        elif x[i] != '0' and x[i-1] != '5':
            return True
        i -= 1
    return True
