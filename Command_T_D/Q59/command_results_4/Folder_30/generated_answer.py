def all_left_truncatable_prime(test_tup):
    res = []
    for n in test_tup:
        prime_str = str(n)
        if len(prime_str) == 1:
            res.append(n)
        elif prime_str[0] == '0':
            continue
        elif all(int(prime_str[i:]) for i in range(1, len(prime_str))):
            res.append(n)
    return res
