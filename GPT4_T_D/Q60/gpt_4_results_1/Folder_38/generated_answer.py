
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    x = t[28]
    truncatable_primes = [i for i in range(x+1) if is_left_right_truncatable(i)]
    if len(truncatable_primes) == 0:
        return []
    else:
        return sorted(truncatable_primes)
