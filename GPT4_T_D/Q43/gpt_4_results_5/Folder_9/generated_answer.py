
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(16, min(72, len(int_list))):
        if is_prime(int_list[i]):
            primes.append(int_list[i])

    return sorted(primes)
