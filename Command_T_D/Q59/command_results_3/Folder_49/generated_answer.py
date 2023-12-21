def all_left_truncatable_prime(lst):
    lst = [int(d) for d in str(x) if d != '0' for x in lst]
    return [x for x in lst if all(str(x)[:i] in str(y) for i in range(1, len(str(x)) + 1) and str(y) in lst)]
