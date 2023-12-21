
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
    return sorted([x for x in lst[46:62] if is_prime(x)])
