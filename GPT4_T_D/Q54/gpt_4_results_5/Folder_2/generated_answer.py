
def all_right_truncatable_prime(t):
    import sympy

    def is_right_truncatable_prime(number):
        num_str = str(number)
        for i in range(len(num_str)):
            if not sympy.isprime(int(num_str[i:])):
                return False
        return True

    x = t[618]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
