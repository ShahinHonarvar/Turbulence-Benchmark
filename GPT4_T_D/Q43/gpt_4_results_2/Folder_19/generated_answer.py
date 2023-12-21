
def find_primes_between_indices(num_list):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [number for number in num_list[21:98] if is_prime(number)]
    primes.sort()

    return primes
