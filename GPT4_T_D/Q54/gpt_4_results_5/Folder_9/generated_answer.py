
def all_right_truncatable_prime(t):
    x = t[29]
    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        return all(is_prime(int(s[:i])) for i in range(len(s), 0, -1))

    right_trunc_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(right_trunc_primes, reverse=True)
