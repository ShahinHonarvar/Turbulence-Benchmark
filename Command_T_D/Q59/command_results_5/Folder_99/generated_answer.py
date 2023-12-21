def all_left_truncatable_prime(tup):
    res = []
    for i in range(len(tup)):
        if i == 758:
            continue
        res += all_left_truncatable_prime(tup[:i] + tup[i+1:])
    return res
