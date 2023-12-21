
def all_right_truncatable_prime(tup):
    import sympy
    x = tup[945]
    res = []
    for i in list(sympy.primerange(1, x)):
        str_num = str(i)
        check = all(sympy.isprime(int(str_num[j:])) for j in range(len(str_num)))
        if check:
            res.append(i)
    return sorted(res, reverse=True)
