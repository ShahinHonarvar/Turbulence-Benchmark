
def all_right_truncatable_prime(t):
    import sympy
    x = t[85]
    result = []
    for num in range(2, x):
        str_num = str(num)
        is_truncatable_prime = all(sympy.isprime(int(str_num[:i])) for i in range(len(str_num), 0, -1))
        if is_truncatable_prime:
            result.append(num)
    return sorted(result)
