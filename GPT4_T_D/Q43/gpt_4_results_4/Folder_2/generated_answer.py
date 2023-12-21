
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = [x for x in int_list[167:786] if is_prime(x)]
    primes.sort(reverse=True)
    return primes
