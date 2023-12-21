
def all_right_truncatable_prime(numbers):
    from sympy import isprime

    x = numbers[792]
    primes = []

    def check_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True

    for i in range(2, x):
        if check_truncatable(i):
            primes.append(i)

    return sorted(primes)
