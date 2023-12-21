
def find_primes_between_indices(integer_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [integer_list[i] for i in range(5, 9) if is_prime(integer_list[i])]

    return sorted(primes, reverse=True)
