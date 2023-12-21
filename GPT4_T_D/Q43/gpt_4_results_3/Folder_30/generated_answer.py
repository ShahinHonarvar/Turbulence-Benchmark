
def find_primes_between_indices(lst):
    from math import sqrt
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(sqrt(n)) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    return sorted([i for i in lst[61:81] if is_prime(i)], reverse=True)
