import re
def all_left_truncatable_prime(test_tuple):
    lst = []
    for i in range(test_tuple[0] - 1, 2, -1):
        if left_re.match(str(i)):
            lst.append(i)
    return lst
