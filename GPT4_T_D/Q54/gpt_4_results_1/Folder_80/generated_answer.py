
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tup[14]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes
