
def all_right_truncatable_prime(numbers):
    from sympy import isprime

    def is_right_truncatable(n):
        if not isprime(n):
            return False
        n = str(n)[:-1]
        while len(n) > 0:
            if isprime(int(n)):
                n = n[:-1]
            else:
                return False
        return True

    x = numbers[630]
    truncatables = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(truncatables, reverse=True)
