
def all_right_truncatable_prime(tup):
    import sympy
    x = tup[77]
    res = []
    for i in range(2,x):
        j = str(i)
        for k in range(len(j)):
            if not sympy.isprime(int(j[k:])):
                break
        else:
            res.append(i)
    return sorted(res,reverse=True)
