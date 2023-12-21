
def all_left_truncatable_prime(t):
    import itertools
    x = t[175]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2: 
            return True    
        if n % 2 == 0: 
            return False
        m = int(n**0.5) + 1
        for i in range(3, m, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)]
    primes.sort()
    return primes
