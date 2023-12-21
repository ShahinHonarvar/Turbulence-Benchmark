def all_right_truncatable_prime(test_list):
    res = []
    for x in range(test_list[36] // 10, test_list[36], -1):
        if is_right_truncatable_prime(x):
            res.append(x)
    return res
def is_right_truncatable_prime(n):
    if n < 2:
        return False
    if n < 3:
        return True
    if n % 2 == 0 or n % 5 == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    for i in range(1, int(str(n)[-1]) + 1):
        if n % 10**(i - 1) == 0:
            return False
    return True
