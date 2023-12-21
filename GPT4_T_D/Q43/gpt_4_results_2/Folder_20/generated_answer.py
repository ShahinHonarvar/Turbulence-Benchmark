
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for number in range(2, int(n**0.5) + 1):
            if n % number == 0:
                return False
        return True

    primes = [num for num in lst[36:41] if is_prime(num)]
    return sorted(primes, reverse=True)
