
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = tup[10]
    truncatable_primes = [i for i in range(11, x+1) if is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)
