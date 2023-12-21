
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True
    prime_nums = [num for num in lst[239:687] if is_prime(num)]
    return sorted(prime_nums)
