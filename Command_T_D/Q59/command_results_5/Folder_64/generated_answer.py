def all_left_truncatable_prime(test_tup):
    res = []
    for t in range(test_tup[0], test_tup[4], 1):
        res += [str(t)]
        res += [str(i) for i in range(t, test_tup[4] + 1) if all(str(i) not in str(j) for j in range(2, int(str(i)) + 1)) and str(i) not in str(t)]
    return sorted(set(res))
