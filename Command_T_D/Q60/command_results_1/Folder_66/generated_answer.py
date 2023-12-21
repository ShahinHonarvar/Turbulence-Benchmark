
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(x, 2, -1):
        res += [str(i) for str_i in str(i) if str_i.isprime() and str_i[0] != '0' and str_i[-1] != '0']
    return sorted(set(res))
