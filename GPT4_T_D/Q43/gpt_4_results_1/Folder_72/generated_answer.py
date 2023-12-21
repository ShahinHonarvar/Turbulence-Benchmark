
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    numbers_between_indices = lst[28:45]
    primes = [number for number in numbers_between_indices if is_prime(number)]
    return sorted(primes)
