
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in int_list[15:49] if is_prime(x)]
    primes.sort(reverse=True)
    return primes
