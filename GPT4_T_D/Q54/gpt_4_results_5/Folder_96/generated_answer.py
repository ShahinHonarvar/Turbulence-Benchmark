
def all_right_truncatable_prime(tuple):
    x = tuple[29]
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    list_of_primes = filter(is_right_truncatable_prime, range(x))
    return sorted(list(list_of_primes))
