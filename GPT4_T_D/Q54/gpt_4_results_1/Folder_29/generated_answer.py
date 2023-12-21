
def all_right_truncatable_prime(t):
    from sympy import isprime
    x = t[55]

    def is_right_truncatable_prime(n):
        while n != 0:
            if not isprime(n):
                return False
            n //= 10
        return True

    result = [i for i in range(x) if is_right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result
