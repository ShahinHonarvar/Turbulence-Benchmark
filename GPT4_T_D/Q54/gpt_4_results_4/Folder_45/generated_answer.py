
def all_right_truncatable_prime(t):
    import sympy
    def check_right_truncatable_prime(n):
        if sympy.isprime(n):
            n = str(n)
            for i in range(len(n)):
                if not sympy.isprime(int(n[:len(n) - i])):
                    return False
            return True
        else:
            return False
    x = t[61]
    result = []
    for num in range(2, x):
        if check_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)
