
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    range_list = lst[80:85]
    primes = list(filter(is_prime, range_list))
    return sorted(primes, reverse=True)
