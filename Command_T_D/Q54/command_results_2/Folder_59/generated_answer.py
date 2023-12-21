def all_right_truncatable_prime(n):
    n = (10**n[0], int(str(n[1])))
    l = []
    while n[0] > 1:
        l += [n[0]]
        n = (10**n[0], int(str(n[1])))
    return l
