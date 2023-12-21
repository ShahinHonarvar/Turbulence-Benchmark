
def all_left_right_truncatable_prime(numbers):
    from sympy import isprime

    def check_truncatable(n):
        if '0' in str(n):
            return False
        for x in range(1, len(str(n))):
            if not isprime(int(str(n)[x:])) or not isprime(int(str(n)[:-x])):
                return False
        return True

    x = numbers[36]
    truncatable_primes = [i for i in range(11, x+1) if isprime(i) and check_truncatable(i)]
    
    return sorted(truncatable_primes)
