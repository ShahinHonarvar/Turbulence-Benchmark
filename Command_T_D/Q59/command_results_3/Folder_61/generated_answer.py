def all_left_truncatable_prime(test_list):
    res = []
    for i in range(2, test_list[3] + 1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(x):
    s = str(x)
    while s[0] == '0':
        s = s[1:]
    return all(x % i for i in range(2, int(s[0])))
