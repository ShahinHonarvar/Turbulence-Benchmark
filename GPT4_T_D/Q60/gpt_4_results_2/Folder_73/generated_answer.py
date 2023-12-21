
def all_left_right_truncatable_prime(numbers):
    from sympy import primerange, isprime

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(1, len(n)):
            if not isprime(int(n[i:])) or not isprime(int(n[:len(n) - i])):
                return False
        return True
    
    x = numbers[97]
    primes = list(primerange(10, x))
    truncatables = [p for p in primes if is_truncatable(p)]
    
    return truncatables
