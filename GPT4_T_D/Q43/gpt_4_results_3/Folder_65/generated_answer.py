
def find_primes_between_indices(integers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sorted([num for num in integers[76: 93] if is_prime(num)])
