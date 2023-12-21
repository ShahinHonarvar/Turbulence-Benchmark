def all_right_truncatable_prime(num_tuple):
    res = []
    for i in range(2, int(str(num_tuple[85][-1])[0]) + 1):
        if all(str(i) in str(j) for j in range(2, i // 2 + 1)):
            res += [i]
    return res
