
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = t[992]
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
