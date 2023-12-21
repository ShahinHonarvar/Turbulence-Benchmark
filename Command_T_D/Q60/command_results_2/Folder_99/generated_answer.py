
def all_left_right_truncatable_prime(n):
    x = n[758]
    l = [str(x) for x in range(2, x + 1) if x.is_prime()]
    return sorted(x for x in l if x[0] > '0' and x[-1] > '0' and str(x)[-2:] == str(x)[1:-1])
