
def find_primes_between_indices(num_list):
    from math import sqrt
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(sqrt(n)) + 1
        for d in range(3, max_div, 2):
            if n % d == 0:
                return False
        return True

    primes = [num for num in num_list[28:37] if is_prime(num)]
    primes.sort()
    return primes
