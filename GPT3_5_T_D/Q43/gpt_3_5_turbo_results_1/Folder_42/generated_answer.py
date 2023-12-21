
def find_primes_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    for index in range(30, 44):
        if is_prime(lst[index]):
            primes.append(lst[index])
    
    return sorted(primes)
