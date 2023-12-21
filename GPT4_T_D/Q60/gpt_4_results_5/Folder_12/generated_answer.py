
def all_left_right_truncatable_prime(t):
    x = t[70]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i+1])):
                return False
        return True

    for i in range(11, x+1):
        if truncatable(i):
            primes.append(i)

    return sorted(primes, reverse=True)
