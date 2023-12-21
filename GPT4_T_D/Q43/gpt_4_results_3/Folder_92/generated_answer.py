
def find_primes_between_indices(lst):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        else:
            return True
            
    return sorted([i for i in lst[7:9] if is_prime(i)])
