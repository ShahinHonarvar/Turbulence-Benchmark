
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in num_list[28:45] if is_prime(n)]
    primes.sort()
    return primes
