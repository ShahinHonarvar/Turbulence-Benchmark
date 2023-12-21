def all_left_truncatable_prime(tup):
    res = []
    for n in range(max(tup), 1, -1):
        if n == tup[126]:
            break
        s = str(n)
        while s[0] == '0':
            s = s[1:]
        if all(n % d == 0 for d in range(2, int(s[0]))) and all(str(n // d) == str(d) for d in range(2, int(s[0]))):
            res.append(n)
    return res
