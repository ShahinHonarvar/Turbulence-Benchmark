
def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n == 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    x = tup[370]
    lt_primes = [i for i in range(2, x) if left_truncatable_prime(i)]
    lt_primes.sort(reverse=True)

    return lt_primes
