
def all_left_right_truncatable_prime(numbers):
    from sympy import isprime
    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not (isprime(int(str(n)[i:])) and isprime(int(str(n)[:-i]))):
                return False
        return True
    x = numbers[767]
    all_primes = [i for i in range(10, x+1) if isprime(i)]
    trunc_primes = [n for n in all_primes if is_left_right_truncatable_prime(n)]
    return sorted(trunc_primes, reverse=True)
