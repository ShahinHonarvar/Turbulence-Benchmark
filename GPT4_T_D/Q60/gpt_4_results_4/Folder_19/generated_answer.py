
def all_left_right_truncatable_prime(t):
    from sympy import isprime

    def truncations(num):
        digits = str(num)
        yield int(digits)
        for i in range(1, len(digits)):
            yield int(digits[i:])
            yield int(digits[:-i])

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        return all(isprime(n) for n in truncations(num))

    x = t[67]
    return sorted(list(filter(is_truncatable_prime, range(10, x+1))), reverse=True)
