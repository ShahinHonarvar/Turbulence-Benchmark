def all_left_truncatable_prime(tup):
    res = []
    for n in range(1, min(tup) + 1):
        if n == 0:
            continue
        while all(str(n).count(d) == 1 for d in str(n)):
            n //= 10
        if n < len(str(n)) and str(n)[-1] != '0' and all(str(n).count(d) == 1 for d in str(n)):
            res.append(n)
    return res
