
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [num for num in num_list[5:9] if is_prime(num)]
    return sorted(primes, reverse=True)
