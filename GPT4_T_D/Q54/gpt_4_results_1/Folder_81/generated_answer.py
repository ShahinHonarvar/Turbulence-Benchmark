
def all_right_truncatable_prime(tpl):
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % m for m in range(3, int(n**0.5) + 1, 2))

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tpl[98]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes)
