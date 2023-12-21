
from sympy import isprime 

def all_left_right_truncatable_prime(numbers):

    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:i+1])): return False
        return True

    x = numbers[37]
    truncatable_primes = [num for num in range(x + 1) if check_truncatable(num) if isprime(num)]
    truncatable_primes.sort(reverse=True)

    return truncatable_primes
