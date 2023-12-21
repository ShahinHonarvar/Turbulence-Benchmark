
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes_in_range = [x for x in int_list[37:96] if is_prime(x)]
    
    return sorted(primes_in_range, reverse=True)
