
def find_primes_between_indices(num_list):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    primes = [num for num in num_list[31:68] if is_prime(num)]
    primes.sort(reverse=True)
    return primes
