
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    x = tup[39]
    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
