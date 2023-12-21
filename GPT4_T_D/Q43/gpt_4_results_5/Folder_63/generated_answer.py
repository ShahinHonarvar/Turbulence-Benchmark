
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [num for num in lst[28:37] if is_prime(num)]
    primes.sort()
    
    return primes
