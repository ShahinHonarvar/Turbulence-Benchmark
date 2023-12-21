
def all_right_truncatable_prime(t):
    import sympy
    def is_right_truncatable(num):
        num_str = str(num)
        return all(sympy.isprime(int(num_str[:i+1])) for i in range(len(num_str)))
    x = t[784]
    return sorted([num for num in range(2, x) if is_right_truncatable(num)])
