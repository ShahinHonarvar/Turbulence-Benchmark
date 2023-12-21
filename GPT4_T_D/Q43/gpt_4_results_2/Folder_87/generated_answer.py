
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes_in_range = []
    for i in range(11, min(42, len(int_list))):
        if is_prime(int_list[i]):
            primes_in_range.append(int_list[i])
            
    return sorted(primes_in_range, reverse=True)
