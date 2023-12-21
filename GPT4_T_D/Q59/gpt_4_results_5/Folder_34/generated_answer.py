
def all_left_truncatable_prime(numbers):
    from sympy import isprime
    
    def is_left_truncatable_prime(n):
        str_number = str(n)
        if "0" in str_number:
            return False
        for i in range(len(str_number)):
            if not isprime(int(str_number[i:])):
                return False
        return True

    x = numbers[18]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
