def all_left_truncatable_prime(n):
    lst = []
    for i in range(2, n[0]):
        s = str(i)
        if len(s) == 1:
            lst.append(i)
        elif s[0] != '0' and all(int(s[i]) for i in range(1, len(s))):
            lst.append(i)
    return lst
