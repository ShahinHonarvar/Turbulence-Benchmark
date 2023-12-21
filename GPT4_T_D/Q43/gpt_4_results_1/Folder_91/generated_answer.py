
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not lst or len(lst) < 2:
        return []

    start, end = lst[0], lst[1]
    primes = [i for i in range(start, end + 1) if is_prime(i)]
    return sorted(primes)
