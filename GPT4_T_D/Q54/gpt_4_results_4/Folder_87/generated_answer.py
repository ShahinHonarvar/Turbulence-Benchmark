
def all_right_truncatable_prime(t):
    x = t[39]
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))
    
    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    sorted_primes = sorted(right_truncatable_primes, reverse=True)
    return sorted_primes
