
def all_right_truncatable_prime(t):
    x = t[92]
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True

    truncatable_primes = []
    for i in range(x):
        if is_right_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes)
