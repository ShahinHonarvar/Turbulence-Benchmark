def all_left_truncatable_prime(test_tup):
    res = []
    for x in range(test_tup[0], test_tup[1]):
        if is_left_truncatable_prime(x):
            res.append(x)
    return res
def is_left_truncatable_prime(x):
    s = str(x)
    while s[0] != '0':
        s = s[1:]
        if not all(map(str.isprime, [int(s)])):
            return False
    return True
