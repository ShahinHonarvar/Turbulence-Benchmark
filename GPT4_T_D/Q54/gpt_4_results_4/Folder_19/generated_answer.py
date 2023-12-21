
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = t[67]
    primes = [p for p in range(2, x) if is_right_truncatable(p)]
    primes.sort(reverse=True)
    return primes
