import bisect
def all_right_truncatable_prime(test_list):
    res = []
    for i in range(2, int(test_list[18])+1):
        if is_prime(i):
            res += [i]
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True
