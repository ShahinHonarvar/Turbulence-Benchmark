
def all_left_truncatable_prime(numbers):
    from sympy import isprime

    def is_left_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        else:
            leftmost_removed = int(str(n)[1:])
            return isprime(n) and is_left_truncatable_prime(leftmost_removed)

    x = numbers[94]
    return sorted([i for i in range(x) if '0' not in str(i) and is_left_truncatable_prime(i)])
