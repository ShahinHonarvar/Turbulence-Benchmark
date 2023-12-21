
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if len(lst)<979:
        list_range = lst[149:]
    else:    
        list_range = lst[149:980]

    primes_in_range = [i for i in list_range if is_prime(i)]
    primes_in_range.sort()

    return primes_in_range
