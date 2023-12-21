def all_left_truncatable_prime(n):
    res = []
    for i in range(2, n[36] + 1):
        s = str(i)
        while s:
            if int(s[0]) == 0:
                break
            s = int(s[1:])
            if s == 1:
                break
            if isprime(s):
                res.append(s)
    return sorted(res)
