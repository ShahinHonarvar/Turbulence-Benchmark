
def all_right_truncatable_prime(numbers):
    from sympy import isprime
  
    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        while n > 9:
            n = n // 10
            if not isprime(n):
                return False
        return True

    x = numbers[370]

    right_truncatable_primes = [number for number in range(x) if is_right_truncatable_prime(number)]

    right_truncatable_primes.sort(reverse=True)

    return right_truncatable_primes
