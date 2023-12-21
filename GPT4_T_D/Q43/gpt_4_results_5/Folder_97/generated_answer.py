
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sorted([i for i in lst[295:456] if is_prime(i)], reverse=True)
